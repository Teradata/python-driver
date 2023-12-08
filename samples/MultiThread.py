# Copyright 2023 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to use multiple threads to load data in parallel.

import teradatasql
import threading

def WorkerThread (con, sTableName, aaoData):

    t = threading.current_thread ()

    # Connection objects are thread safe. Threads can share a connection.
    # Cursor objects are not thread safe. Each thread needs its own cursor.

    with con.cursor () as cur:

        sql = "create volatile table " + sTableName + " (c1 integer, c2 varchar(100)) on commit preserve rows"
        print ("Worker thread", t.ident, sql)
        cur.execute (sql)

        sql = "insert into " + sTableName + " values (?, ?)"
        print ("Worker thread", t.ident, sql)
        cur.execute (sql, aaoData)

    # end WorkerThread

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:

    tMain = threading.current_thread ()

    tWorker1 = threading.Thread (target=WorkerThread, args=(con, "voltab1", [
        [1, "abc"],
        [2, "def"],
        [3, "ghi"],
    ]))
    print ("Main thread", tMain.ident, "starting worker thread #1")
    tWorker1.start ()

    tWorker2 = threading.Thread (target=WorkerThread, args=(con, "voltab2", [
        [10, "rst"],
        [20, "uvw"],
        [30, "xyz"],
    ]))
    print ("Main thread", tMain.ident, "starting worker thread #2")
    tWorker2.start ()

    print ("Main thread", tMain.ident, "waiting for worker thread", tWorker1.ident, "to finish")
    tWorker1.join ()
    print ("Main thread", tMain.ident, "done waiting for worker thread", tWorker1.ident)

    print ("Main thread", tMain.ident, "waiting for worker thread", tWorker2.ident, "to finish")
    tWorker2.join ()
    print ("Main thread", tMain.ident, "done waiting for worker thread", tWorker2.ident)

    with con.cursor () as cur:

        sql = "select * from voltab1 order by 1 ; select * from voltab2 order by 1"
        print ("Main thread", tMain.ident, sql)
        cur.execute (sql)
        [ print (row) for row in cur.fetchall () ]
        cur.nextset ()
        [ print (row) for row in cur.fetchall () ]
