# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to FastLoad a JSONL file.
# It demonstrates key-order independence and explicit NULL handling.

import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        sTableName = "FastLoadJSONL"

        sRequest = "DROP TABLE " + sTableName
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_1"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_2"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        jsonlFileName = "dataPy.jsonl"
        print (f"Writing {jsonlFileName}")

        lines = [
            '{"c1":1,"c2":"x1","c3":[0.10,-0.20,0.30]}',
            '{"c2":"x2","c1":2,"c3":[0.20,-0.40,0.60]}',
            '{"c3":[0.30,-0.60,0.90],"c1":3,"c2":"x3"}',
            '{"c1":4,"c2":"x4","c3":[0.40,-0.80,1.20]}',
            '{"c1":5,"c2":null,"c3":[0.50,-1.00,1.50]}',
            '{"c1":6,"c2":"x6","c3":[0.60,-1.20,1.80]}',
            '{"c1":7,"c2":"x7","c3":[0.70,-1.40,2.10]}',
            '{"c1":8,"c2":"x8","c3":[0.80,-1.60,2.40]}',
            '{"c1":9,"c2":"x9","c3":[0.90,-1.80,2.70]}',
        ]

        with open (jsonlFileName, "w", encoding="UTF-8") as f:
            for line in lines:
                f.write (line + "\n")

        try:
            sRequest = "CREATE TABLE " + sTableName + " (c1 INTEGER NOT NULL, c2 VARCHAR(10), c3 VECTOR) UNIQUE PRIMARY INDEX (c1)"
            print (sRequest)
            cur.execute (sRequest)

            try:
                print ("con.autocommit = False")
                con.autocommit = False

                try:
                    sInsert = (
                        "{fn teradata_require_fastload}" +
                        "{fn teradata_read_jsonl(" + jsonlFileName + ")}" +
                        "INSERT INTO " + sTableName + " (c1, c2, c3) VALUES (?, ?, ?)"
                    )
                    print (sInsert)
                    cur.execute (sInsert)

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_warnings}" + sInsert
                    print (sRequest)
                    cur.execute (sRequest)
                    [ print (row) for row in cur.fetchall () ]

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_errors}" + sInsert
                    print (sRequest)
                    cur.execute (sRequest)
                    [ print (row) for row in cur.fetchall () ]

                    sRequest = "{fn teradata_nativesql}{fn teradata_logon_sequence_number}" + sInsert
                    print (sRequest)
                    cur.execute (sRequest)
                    [ print (row) for row in cur.fetchall () ]

                    print ("con.commit()")
                    con.commit ()

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_warnings}" + sInsert
                    print (sRequest)
                    cur.execute (sRequest)
                    [ print (row) for row in cur.fetchall () ]

                    sRequest = "{fn teradata_nativesql}{fn teradata_get_errors}" + sInsert
                    print (sRequest)
                    cur.execute (sRequest)
                    [ print (row) for row in cur.fetchall () ]

                finally:
                    print ("con.autocommit = True")
                    con.autocommit = True

                sRequest = "SELECT c1, c2, c3 FROM " + sTableName + " ORDER BY 1"
                print (sRequest)
                cur.execute (sRequest)
                [ print (row) for row in cur.fetchall () ]

            finally:
                sRequest = "DROP TABLE " + sTableName
                print (sRequest)
                cur.execute (sRequest, ignoreErrors=3807)

        finally:
            print (f"os.remove({jsonlFileName})")
            try:
                os.remove (jsonlFileName)
            except OSError as e:
                print (f"os.remove failed: {e}")
