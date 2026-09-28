# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates how a multi-statement request writes multiple JSONL files.

import json
import os
import teradatasql


def readJSONL (sFileName):
    with open (sFileName, "rt", encoding="UTF8") as f:
        return [json.loads (sLine) for sLine in f]


with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(100)) on commit preserve rows")

        print ("Inserting data")
        cur.execute ("insert into voltab values (?, ?)", [[1, "abc"], [2, None], [3, "xyz"]])

        asFileNames = ["dataPy.jsonl", "dataPy_1.jsonl", "dataPy_2.jsonl"]
        print ("Exporting multi-statement results to files", asFileNames)
        cur.execute ("{fn teradata_write_jsonl(" + asFileNames [0] + ")}select * from voltab where c1 < 3 order by 1;select * from voltab where c1 >= 3 order by 1;select 123 as col1, 'abc' as col2")
        try:
            for sFileName in asFileNames:
                print ("Reading file", sFileName)
                print (readJSONL (sFileName))
        finally:
            for sFileName in asFileNames:
                os.remove (sFileName)
