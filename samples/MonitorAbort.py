# Copyright 2024 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to use the Monitor partition to abort a session.
# The database user must have the MONITOR privilege: GRANT MONITOR TO guest

import teradatasql

def abortSession (nHostNumber, nSessionNumber):
    with teradatasql.connect (host="whomooz", user="guest", password="please", partition="MONITOR") as con:
        with con.cursor () as cur:
            print ("Aborting host number", nHostNumber, "session number", nSessionNumber)
            sCommand = ("ABORT SESSION"
                "{fn teradata_parameter(1, SMALLINT)}" # mon_ver_id
                "{fn teradata_parameter(2, SMALLINT)}" # host_no
                "{fn teradata_parameter(3, INTEGER)}") # session_no
            print ("Executing", sCommand)
            cur.execute (sCommand, [
                9, # mon_ver_id
                nHostNumber,
                nSessionNumber,
                None, # user_name
                "N", # list
                "Y", # logoff
                "N"]) # override

def conciseError (ex):
    asLines = str (ex).split ("\n")
    sOutput = ""
    for i, sLine in enumerate (asLines):
        if i == 0:
            sOutput += sLine
        elif sLine.startswith ("Caused by"):
            sOutput += " " + sLine
    return sOutput

con = teradatasql.connect (host="whomooz", user="guest", password="please")
with con.cursor () as cur:
    sQuery = "SELECT HostNo, SessionNo FROM DBC.SessionInfoV WHERE SessionNo = SESSION"
    print ("Executing", sQuery)
    cur.execute (sQuery)
    row = cur.fetchone ()
    nHostNumber, nSessionNumber = row [0], row [1]

abortSession (nHostNumber, nSessionNumber)

try:
    con.close ()
except Exception as ex:
    s = conciseError (ex)
    if "[Error 503]" in s or "[Error 3000]" in s:
        print ("Ignoring", s)
    else:
        raise # rethrow
