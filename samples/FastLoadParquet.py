# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to FastLoad a Parquet file.

import os
import teradatasql
import pyarrow as pa
import pyarrow.parquet as pq

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        sTableName = "FastLoadParquet"
        sRequest = "DROP TABLE " + sTableName
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_1"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        sRequest = "DROP TABLE " + sTableName + "_ERR_2"
        print (sRequest)
        cur.execute (sRequest, ignoreErrors=3807)

        # Create Parquet file with sample data
        parquetFileName = "dataPy.parquet"
        print (f"Creating Parquet file: {parquetFileName}")

        # Create data arrays
        data = {
            'c1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'c2': ['test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9']
        }

        # Create Arrow table
        table = pa.table (data)

        # Write Parquet file
        pq.write_table (table, parquetFileName)
        print ("Parquet file created successfully")

        try:
            sRequest = "CREATE TABLE " + sTableName + " (c1 INTEGER, c2 VARCHAR(10))"
            print (sRequest)
            cur.execute (sRequest)

            try:
                print ("con.autocommit = False")
                con.autocommit = False

                try:
                    sInsert = "{fn teradata_require_fastload}{fn teradata_read_parquet(" + parquetFileName + ")}INSERT INTO " + sTableName + " (?, ?)"
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

                sRequest = "SELECT * FROM " + sTableName + " ORDER BY 1"
                print (sRequest)
                cur.execute (sRequest)
                [ print (row) for row in cur.fetchall () ]

            finally:
                sRequest = "DROP TABLE " + sTableName
                print (sRequest)
                cur.execute (sRequest, ignoreErrors=3807)

        finally:
            print (f"os.remove({parquetFileName})")
            try:
                os.remove (parquetFileName)
            except OSError as e:
                print (f"os.remove failed: {e}")
