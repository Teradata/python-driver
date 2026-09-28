# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates how to export a select result into a JSON file.

import json
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(100)) on commit preserve rows")
        cur.execute ("insert into voltab values (?, ?)", [[1, "abc"], [2, None], [3, "xyz"]])
        sFileName = "dataPy.json"
        cur.execute ("{fn teradata_write_json(" + sFileName + ")}select * from voltab order by 1")
        try:
            with open (sFileName, "rt", encoding="UTF8") as f:
                print (json.load (f))
        finally:
            os.remove (sFileName)
