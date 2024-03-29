# Copyright 2023 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to insert a batch of rows with Auto-Generated Key Retrieval (AGKR).

import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:

    with con.cursor () as cur:

        sTableName = "agkrdemo"
        cur.execute ("drop table " + sTableName, ignoreErrors=3807)
        cur.execute ("create table " + sTableName + " (c1 integer generated by default as identity, c2 varchar(100))")
        try:
            print ("Using AGKR option C to return identity column values only")
            cur.execute ("{fn teradata_agkr(C)}insert into " + sTableName + " (c2) values (?)", [
                ["abc"],
                ["def"],
                ["ghi"],
            ])

            print ("Each identity column value is retured in a separate single-row result set")
            while True:
                [ print (row) for row in cur.fetchall () ]
                if not cur.nextset ():
                    break

            print ("Using AGKR option R to return entire inserted rows")
            cur.execute ("{fn teradata_agkr(R)}insert into " + sTableName + " (c2) values (?)", [
                ["jkl"],
                ["mno"],
                ["pqr"],
            ])

            print ("Each inserted row is retured in a separate single-row result set")
            while True:
                [ print (row) for row in cur.fetchall () ]
                if not cur.nextset ():
                    break

            print ("Final contents of table")
            cur.execute ("select * from " + sTableName + " order by 1")
            [ print (row) for row in cur.fetchall () ]

        finally:
            cur.execute ("drop table " + sTableName)
