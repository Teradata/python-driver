# Copyright 2025 by Teradata Corporation. All Rights Reserved.

# This sample program demonstrates how to abort a session.

import teradatasql

def concise (ex):
    asLines = str (ex).splitlines ()
    # eliminate lines beginning with " at "
    asLines = [ line for line in asLines if not line.lstrip ().startswith ("at ") ]
    return "\n  ".join (asLines)

conUser = teradatasql.connect (host="whomooz", user="guest", password="please")
try:
    with conUser.cursor () as curUser:
        curUser.execute ("select 123")
        row = curUser.fetchone ()
        print ("Query result:", row [0])

        nSessionNumber = conUser.nativeSQL ("{fn teradata_session_number}")

        with teradatasql.connect (host="whomooz", user="dbc", password="dbc") as conAdmin:
            with conAdmin.cursor () as curAdmin:
                print ("Aborting session number", nSessionNumber)
                curAdmin.execute ("select AbortSessions (-1, null, " + str (nSessionNumber) + ", 'Y', 'Y')")

        try:
            curUser.execute ("select 456")
            row = curUser.fetchone ()
            print ("Query result:", row [0])
        except Exception as ex:
            print ("Expected error after aborting session:", concise (ex))
finally:
    try:
        conUser.close ()
    except Exception as ex:
        print ("Expected error after aborting session:", concise (ex))
