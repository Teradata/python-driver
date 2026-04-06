# Copyright 2026 by Teradata Corporation. All rights reserved.

# This sample program demonstrates two different approaches to load data values
# from a Parquet file and insert those data values into a database table.
# This sample program requires the airports.parquet file to be located in the current directory.

import teradatasql
import pyarrow.parquet as pq

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:
        cur.execute ("create volatile table Airports (City varchar(100), Airport varchar(100), AirportCode varchar(10)) on commit preserve rows")

        print ("Slower approach - use pyarrow to parse data values from a Parquet file")
        table = pq.read_table ("airports.parquet")
        listRows = table.to_batches () [0].to_pylist ()
        data = [ [ row ['City'], row ['Airport'], row ['AirportCode'] ] for row in listRows ]
        cur.execute ("insert into Airports (?, ?, ?)", data)

        cur.execute ("select AirportCode, Airport, City from Airports order by AirportCode")
        [ print (row) for row in cur.fetchall () ]

        cur.execute ("delete from Airports")

        print ("Faster approach - the driver loads data values from a Parquet file")
        cur.execute ("{fn teradata_read_parquet(airports.parquet)}insert into Airports (?, ?, ?)")

        cur.execute ("select AirportCode, Airport, City from Airports order by AirportCode")
        [ print (row) for row in cur.fetchall () ]
