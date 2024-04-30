# Copyright 2024 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to execute Monitor partition queries.
# The database user must have the MONITOR privilege: GRANT MONITOR TO guest

import itertools
import teradatasql

def executeQuery (con, sQuery, aBindValues):
    with con.cursor () as cur:
        print ()
        print ("Executing Monitor partition query", sQuery)
        cur.execute (sQuery, aBindValues)
        for iResult in itertools.count ():
            print ()
            for iRow, row in enumerate (cur.fetchall ()):
                for iColumn, value in enumerate (row):
                    print ("  Result {} row {} column {} value = {}".format (iResult + 1, iRow + 1, iColumn + 1, value))
            if not cur.nextset ():
                break

p1 = "{fn teradata_parameter(1, SMALLINT)}"
p2 = "{fn teradata_parameter(2, SMALLINT)}"

with teradatasql.connect (host="whomooz", user="guest", password="please", partition="MONITOR") as con:
    executeQuery (con, p1 + "MONITOR VERSION"          , [9])
    executeQuery (con, p1 + "MONITOR PHYSICAL CONFIG"  , [9])
    executeQuery (con, p1 + "MONITOR PHYSICAL RESOURCE", [9])
    executeQuery (con, p1 + "MONITOR PHYSICAL SUMMARY" , [9])
    executeQuery (con, p1 + "MONITOR VIRTUAL CONFIG"   , [9])
    executeQuery (con, p1 + "MONITOR VIRTUAL RESOURCE" , [9])
    executeQuery (con, p1 + "MONITOR VIRTUAL SUMMARY"  , [9])
    executeQuery (con, p1 + "TDWM SUMMARY"             , [9])
    executeQuery (con, p1 + p2 + "TDWM STATISTICS"     , [9, 5])
