# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to insert a batch of rows using a JSON file.
# It also illustrates dual treatment of a nested JSON object: the raw JSON
# string is stored verbatim in the "address" column, while the flattened
# sub-field "city" is stored in a separate column.

import json
import os
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (id integer, name varchar(20), address varchar(200), city varchar(20)) on commit preserve rows")

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

        sFileName = "dataBatchPy.json"
        print (f"Writing {sFileName}")
        with open (sFileName, "w", encoding="UTF-8") as f:
            json.dump (records, f)

        try:
            print ("Inserting data")
            cur.execute ("{fn teradata_read_json(%s)} insert into voltab (id, name, address, city) values (?, ?, ?, ?)" % sFileName)
        finally:
            os.remove (sFileName)

        cur.execute ("select id, name, address, city from voltab order by 1")
        [ print (row) for row in cur.fetchall () ]
