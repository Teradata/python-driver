# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates how to FastExport into a JSONL file.

import json
import os
import teradatasql


def readJSONL (sFileName):
    with open (sFileName, "rt", encoding="UTF8") as f:
        return [json.loads (sLine) for sLine in f]


with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        sTableName = "FastExportJSONL"
        cur.execute ("create table " + sTableName + " (c1 integer, c2 varchar(10))")
        try:
            print ("Inserting data")
            cur.execute ("insert into " + sTableName + " values (?, ?)", [[1, None], [2, "abc"], [3, "xyz"]])

            sFileName = "dataPy.jsonl"
            sSelect = "{fn teradata_try_fastexport}{fn teradata_write_jsonl(" + sFileName + ")}select * from " + sTableName + " order by 1"
            print ("FastExporting table data to file", sFileName)
            cur.execute (sSelect)
            try:
                print ("Reading file", sFileName)
                print (readJSONL (sFileName))
            finally:
                os.remove (sFileName)
        finally:
            cur.execute ("drop table " + sTableName)
