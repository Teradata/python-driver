# Copyright 2026 by Teradata Corporation. All rights reserved.
# TERADATA CORPORATION CONFIDENTIAL AND TRADE SECRET

# This sample program demonstrates fake multi-statement results written to JSON files.

import json
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(100)) on commit preserve rows")
        cur.execute ("insert into voltab values (?, ?)", [[1, "abc"], [2, None], [3, "xyz"]])
        asFileNames = ["dataPy.json", "dataPy_1.json", "dataPy_2.json", "dataPy_3.json", "dataPy_4.json", "dataPy_5.json"]
        cur.execute ("{fn teradata_write_json(" + asFileNames [0] + ")}{fn teradata_fake_result_sets}select * from voltab where c1 < 3 order by 1;select * from voltab where c1 >= 3 order by 1;select 123 as col1, 'abc' as col2")
        try:
            for sFileName in asFileNames:
                with open (sFileName, "rt", encoding="UTF8") as f:
                    rows = json.load (f)
                for row in rows:
                    for sColumnName in ("ColumnMetadata", "ParameterMetadata"):
                        if isinstance (row.get (sColumnName), str):
                            try:
                                row [sColumnName] = json.loads (row [sColumnName])
                            except ValueError:
                                pass
                print (f"{sFileName}:")
                print (json.dumps (rows, indent=2))
        finally:
            for sFileName in asFileNames:
                os.remove (sFileName)
