# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to export the results from a multi-statement request into
# multiple Parquet files and obtain info on each statement using fake_result_sets escape function.

import json
import os
import re
import pyarrow.parquet as pq
import teradatasql

def read_parquet_file (sFileName):
    print ("Reading Parquet file", sFileName)
    table = pq.read_table (sFileName)
    col_names = table.schema.names
    n_rows = len (table)
    for i in range (n_rows):
        print ("Row", i + 1, ":")
        for col in col_names:
            val = table [col][i].as_py ()
            print ("  {:<20} = {}".format (col, format_value (val)))
    print ("Row count:", n_rows)

def format_value (val):
    if val is None:
        return "NULL"
    if isinstance (val, (bytes, bytearray)):
        try:
            val = val.decode ("utf-8")
        except UnicodeDecodeError:
            return "0x" + bytes (val).hex ().upper ()
    s = str (val)
    stripped = s.strip ()
    if stripped and stripped [0] in "{[":
        try:
            indent = " " * 25  # 2 spaces + 20 col name width + 3 for " = "
            return json.dumps (json.loads (stripped), indent = 2).replace ("\n", "\n" + indent)
        except (json.JSONDecodeError, ValueError):
            pass
    return s

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(10)) on commit preserve rows")

        print ("Inserting data")
        cur.execute ("insert into voltab values (?, ?)", [
            [1, "x1"],
            [2, "x2"],
            [3, "x3"],
            [4, "x4"],
            [5, "x5"],
            [6, "x6"],
            [7, "x7"],
            [8, "x8"],
            [9, "x9"],
        ])

        # When using fake_result_sets, two Parquet files are produced per statement: fake then real.
        asFileNames = ["dataPy.parquet", "dataPy_1.parquet", "dataPy_2.parquet", "dataPy_3.parquet", "dataPy_4.parquet", "dataPy_5.parquet"]
        print ("Exporting table data to files", asFileNames)
        cur.execute ("{fn teradata_write_parquet(" + asFileNames [0] + ")}{fn teradata_fake_result_sets}select * from voltab where c1 < 5 order by 1 ; select * from voltab where c1 >= 5 order by 1 ; select 'abc' as col1, '12' as col2")

        try:
            print ("\n=== Two Parquet files produced by each statement (fake then real) ===")
            for i, sFileName in enumerate (asFileNames):
                nPostfix = int (re.sub ("\\D", "", re.sub ("^$", "0", re.sub (".*dataPy", "", re.sub ("\\.parquet$", "", sFileName)))))
                if nPostfix % 2 == 0:
                    print ("\n --- Fake result set", nPostfix // 2 + 1, "---")
                else:
                    print ("\n --- Real result set", (nPostfix + 1) // 2, "---")
                read_parquet_file (sFileName)

        finally:
            [ os.remove (sFileName) for sFileName in asFileNames ]
