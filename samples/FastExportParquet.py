# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to FastExport into a Parquet file.

import json
import os
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
        with con.cursor () as cur2:
            sTableName = "FastExportParquet"
            try:
                sRequest = "DROP TABLE " + sTableName
                print (sRequest)
                cur.execute (sRequest)
            except Exception as ex:
                print ("Ignoring", str (ex).split ("\n") [0])

            sRequest = "CREATE TABLE " + sTableName + " (c1 INTEGER NOT NULL, c2 VARCHAR(10))"
            print (sRequest)
            cur.execute (sRequest)

            try:
                sInsert = "INSERT INTO " + sTableName + " VALUES (?, ?)"
                print (sInsert)
                cur.execute (sInsert, [
                    [1, None],
                    [2, "x2"],
                    [3, "x3"],
                    [4, "x4"],
                    [5, None],
                    [6, "x6"],
                    [7, "x7"],
                    [8, "x8"],
                    [9, None],
                ])

                sFileName = "dataPy.parquet"
                sSelect = "{fn teradata_try_fastexport}{fn teradata_write_parquet(" + sFileName + ")}SELECT * FROM " + sTableName
                print (sSelect)
                cur.execute (sSelect)
                try:
                    read_parquet_file (sFileName)

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_warnings}" + sSelect
                    print (sRequest)
                    cur2.execute (sRequest)
                    [ print (row) for row in cur2.fetchall () ]

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_errors}" + sSelect
                    print (sRequest)
                    cur2.execute (sRequest)
                    [ print (row) for row in cur2.fetchall () ]

                    sRequest = "{fn teradata_nativesql}{fn teradata_logon_sequence_number}" + sSelect
                    print (sRequest)
                    cur2.execute (sRequest)
                    [ print (row) for row in cur2.fetchall () ]

                finally:
                    print ("os.remove(" + sFileName + ")")
                    os.remove (sFileName)

            finally:
                sRequest = "DROP TABLE " + sTableName
                print (sRequest)
                cur.execute (sRequest)
