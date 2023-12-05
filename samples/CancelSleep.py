# Copyright 2023 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to use the cancel method to interrupt a query
# executing in another thread.

import teradatasql
import threading
import time

def WorkerThread (cur):

    t = threading.current_thread ()

    sql = "select mysleep (10)" # sleep for 10 seconds
    print ("Worker thread", t.ident, sql)
    try:
        cur.execute (sql)
    except Exception as ex:
        print ("Worker thread", t.ident, str (ex).split ("\n") [0])

    # end WorkerThread

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor () as cur:

        tMain = threading.current_thread ()

        sql = "drop function mysleep"
        print ("Main thread", tMain.ident, sql)
        cur.execute (sql, ignoreErrors=5589)

        sql = "create function mysleep (integer) returns integer language c no sql parameter style sql external name 'CS!udfsleep!udfsleep.c!F!udfsleep'"
        print ("Main thread", tMain.ident, sql)
        cur.execute (sql)
        try:
            tWorker = threading.Thread (target=WorkerThread, args=(cur,))
            print ("Main thread", tMain.ident, "starting worker thread")
            tWorker.start ()

            print ("Main thread", tMain.ident, "sleeping for 5 seconds")
            time.sleep (5)

            print ("Main thread", tMain.ident, "calling cancel")
            con.cancel ()
            print ("Main thread", tMain.ident, "completed cancel")

            print ("Main thread", tMain.ident, "waiting for worker thread", tWorker.ident, "to finish")
            tWorker.join ()
            print ("Main thread", tMain.ident, "done waiting for worker thread", tWorker.ident)

        finally:
            sql = "drop function mysleep"
            print ("Main thread", tMain.ident, sql)
            cur.execute (sql)
