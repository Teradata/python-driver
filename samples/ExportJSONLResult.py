# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates how to export a select result into a JSONL file.

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

        sFileName = "dataPy.jsonl"
        print ("Exporting table data to file", sFileName)
        cur.execute ("{fn teradata_write_jsonl(" + sFileName + ")}select * from voltab order by 1")

        try:
            print ("Reading file", sFileName)
            print (readJSONL (sFileName))
        finally:
            os.remove (sFileName)
