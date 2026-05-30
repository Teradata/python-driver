# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to FastLoad a JSON file.
# It also illustrates dual treatment of a nested JSON object: the raw JSON
# string is stored verbatim in the "address" column, while the flattened
# sub-field "city" is stored in a separate column.


import json
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        sTableName = "FastLoadJSON"
        sRequest = "DROP TABLE " + sTableName
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_1"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_2"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        # Each record has three top-level keys:
        #   id      -- scalar integer
        #   name    -- scalar string
        #   address -- nested object; its raw JSON string maps to the "address" column
        #              and its sub-field "city" maps to the "city" column.
        records = [
            {"id": 1, "name": "Alice", "address": {"city": "Boston"}},
            {"id": 2, "name": "Bob",   "address": {"city": "Austin"}},
            {"id": 3, "name": "Carol", "address": {"city": "Chicago"}},
            {"id": 4, "name": "Dave",  "address": {"city": "Denver"}},
            {"id": 5, "name": "Erin",  "address": {"city": "Eugene"}},
            {"id": 6, "name": "Frank", "address": {"city": "Fresno"}},
            {"id": 7, "name": "Grace", "address": {"city": "Houston"}},
            {"id": 8, "name": "Hank",  "address": {"city": "Irvine"}},
            {"id": 9, "name": "Iris",  "address": {"city": "Jacksonville"}},
        ]

        jsonFileName = "dataPy.json"
        print (f"Writing {jsonFileName}")
        with open (jsonFileName, "w", encoding="UTF-8") as f:
            json.dump (records, f)

        try:
            sRequest = "CREATE TABLE " + sTableName + " (id INTEGER, name VARCHAR(20), address VARCHAR(200), city VARCHAR(20)) UNIQUE PRIMARY INDEX (id)"
            print (sRequest)
            cur.execute (sRequest)

            try:
                print ("con.autocommit = False")
                con.autocommit = False

                try:
                    # The INSERT column list (id, name, address, city) drives name-based matching:
                    #   ?1 -> id      (scalar)
                    #   ?2 -> name    (scalar)
                    #   ?3 -> address (raw JSON object string -- dual treatment)
                    #   ?4 -> city    (flattened sub-field of address)
                    sInsert = (
                        "{fn teradata_require_fastload}"
                        "{fn teradata_read_json(" + jsonFileName + ")}"
                        "INSERT INTO " + sTableName + " (id, name, address, city) VALUES (?, ?, ?, ?)"
                    )
                    print (sInsert)
                    cur.execute (sInsert)

                    # obtain the warnings and errors for transmitting the data to the database -- the acquisition phase

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

                    # obtain the warnings and errors for the apply phase

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

                sRequest = "SELECT id, name, address, city FROM " + sTableName + " ORDER BY 1"
                print (sRequest)
                cur.execute (sRequest)
                [ print (row) for row in cur.fetchall () ]

            finally:
                sRequest = "DROP TABLE " + sTableName
                print (sRequest)
                cur.execute (sRequest, ignoreErrors=3807)

        finally:
            print (f"os.remove({jsonFileName})")
            try:
                os.remove (jsonFileName)
            except OSError as e:
                print (f"os.remove failed: {e}")
