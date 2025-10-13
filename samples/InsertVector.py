# Copyright 2025 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to insert values into a Vector column.

import numpy as np
import pandas as pd
import teradatasql

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table voltab (c1 integer, c2 vector) on commit preserve rows")

        # Example 1 - bind values as list of lists
        # Vector values are string having VARCHAR format compatible with Vector
        cur.execute ("insert into voltab values (?, ?)", [
            [1, "1.7,1.8,1.9"],
            [2, "2.7,2.8,2.9"],
        ])

        # Example 2 - bind values as list of lists
        # Vector values are one-dimensional numpy arrays, both float32 and float64 are supported
        cur.execute ("insert into voltab values (?, ?)", [
            [3, np.array ([3.7, 3.8, 3.9], dtype=np.float32)],
            [4, np.array ([4.7, 4.8, 4.9], dtype=np.float64)],
        ])

        # Example 3 - bind values as pandas DataFrame constructed from list of lists
        # Vector values are one-dimensional numpy arrays, both float32 and float64 are supported
        df = pd.DataFrame ([
            [5, np.array ([5.7, 5.8, 5.9], dtype=np.float32)],
            [6, np.array ([6.7, 6.8, 6.9], dtype=np.float64)],
        ], columns=["c1", "c2"])
        cur.execute ("insert into voltab values (?, ?)", df)

        # Example 4 - bind values as pandas DataFrame constructed from dictionary
        # Vector values are one-dimensional numpy arrays, both float32 and float64 are supported
        df = pd.DataFrame ({
            "c1": [7, 8],
            "c2": [np.array ([7.7, 7.8, 7.9], dtype=np.float32), np.array ([8.7, 8.8, 8.9], dtype=np.float64)],
        })
        cur.execute ("insert into voltab values (?, ?)", df)

        cur.execute ("set transform group for type vector vector_io_varchar")
        cur.execute ("select * from voltab order by 1")
        [ print (row) for row in cur.fetchall () ]
