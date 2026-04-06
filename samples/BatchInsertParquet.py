# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to insert a batch using a parquet file.

import os
import teradatasql
import pyarrow as pa
import pyarrow.parquet as pq

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 varchar(10)) on commit preserve rows")

        # Create Parquet file with sample data
        parquetFileName = "dataBatchPy.parquet"
        print (f"Creating Parquet file: {parquetFileName}")

        # Create data arrays
        data = {
            'c1': [1, 2, 3, 4, 5, 6, 7, 8, 9],
            'c2': ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9']
        }

        # Create Arrow table
        table = pa.table (data)

        # Write Parquet file
        pq.write_table (table, parquetFileName)
        print ("Parquet file created successfully")

        try:
            print ("Inserting data")
            cur.execute ("{fn teradata_read_parquet(%s)} insert into voltab (?, ?)" % parquetFileName)
        finally:
            print (f"os.remove({parquetFileName})")
            os.remove (parquetFileName)

        cur.execute ("select * from voltab order by 1")
        [ print (row) for row in cur.fetchall () ]
