# Copyright 2023 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to insert BLOB and CLOB values.

import teradatasql

def FormatValue (oValue):
    if isinstance (oValue, str) or isinstance (oValue, bytes):
        s = "{}".format (oValue)
        if len (s) > 20:
            s = s [ : 20] + " ..."
        return s + " (len={})".format (len (oValue))
    else:
        return oValue

with teradatasql.connect (host="whomooz", user="guest", password="please", log="8") as con: # log=8 specifies TIMING log lines
    with con.cursor () as cur:
        sSQL = "create volatile table voltab (c1 integer, c2 blob, c3 clob) on commit preserve rows"
        print (sSQL)
        cur.execute (sSQL)

        abySmallBlob = b'abc'           # bytes value with len=3
        abyLargeBlob = b'ABC' * 25000   # bytes value with len=75000
        sSmallClob   = "xyz"            # str   value with len=3
        sLargeClob   = "XYZ" * 25000    # str   value with len=75000

        sSQL = "insert into voltab values (?, ?, ?)"
        print (sSQL)
        # Small LOB values <= 64K are inserted as inline values, contained in a single request message sent to the database.
        cur.execute (sSQL, [ 1, abySmallBlob, sSmallClob ])

        # TIMING log lines show a single send/receive message round trip:
        #   GOSQL-TIMING NetworkIO.go:426 Receive header Start Response message took 24 ms
        #   GOSQL-TIMING NetworkIO.go:464 Receive Start Response message body took 0 ms, send and receive took 56 ms
        #   GOSIDE-TIMING goside.go:789 createRows call to QueryContext took 56 ms

        print (sSQL)
        # Large LOB values > 64K are inserted as deferred values, and require multiple message round trips to the database.
        cur.execute (sSQL, [ 2, abyLargeBlob, sLargeClob ])

        # TIMING log lines show multiple send/receive message round trips:
        #   GOSQL-TIMING NetworkIO.go:426 Receive header Elicit Request message took 9 ms
        #   GOSQL-TIMING NetworkIO.go:464 Receive Elicit Request message body took 0 ms, send and receive took 22 ms
        #   GOSQL-TIMING NetworkIO.go:426 Receive header Elicit Request message took 38 ms
        #   GOSQL-TIMING NetworkIO.go:464 Receive Elicit Request message body took 0 ms, send and receive took 54 ms
        #   GOSQL-TIMING NetworkIO.go:426 Receive header Start Response message took 27 ms
        #   GOSQL-TIMING NetworkIO.go:464 Receive Start Response message body took 0 ms, send and receive took 29 ms
        #   GOSIDE-TIMING goside.go:789 createRows call to QueryContext took 115 ms

        sSQL = "select * from voltab order by 1"
        print (sSQL)
        cur.execute (sSQL)

        nRow = 0
        while True:
            row = cur.fetchone ()
            if not row:
                break
            nRow += 1
            for iColumn in range (len (row)):
                print ('Row {} Column {} "{}" = {}'.format (nRow, iColumn + 1, cur.description [iColumn][0], FormatValue (row [iColumn])))

        print ("Fetched {} rows".format (nRow))
