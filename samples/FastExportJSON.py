# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates how to FastExport into a JSON file.

import json
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        sTableName = "FastExportJSON"
        cur.execute ("create table " + sTableName + " (c1 integer, c2 varchar(10))")
        try:
            cur.execute ("insert into " + sTableName + " values (?, ?)", [[1, None], [2, "abc"], [3, "xyz"]])
            sFileName = "dataPy.json"
            sSelect = "{fn teradata_try_fastexport}{fn teradata_write_json(" + sFileName + ")}select * from " + sTableName + " order by 1"
            cur.execute (sSelect)
            try:
                with open (sFileName, "rt", encoding="UTF8") as f:
                    print (json.load (f))
            finally:
                os.remove (sFileName)
        finally:
            cur.execute ("drop table " + sTableName)
