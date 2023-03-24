# Copyright 2023 by Teradata Corporation. All rights reserved.

# This sample program demonstrates how to use the teradata_lobselect(S) and teradata_fake_result_sets
# escape functions to obtain LOB locators instead of the default inline LOB values from a result set,
# and then subsequently read the LOB values from the LOB locators.

import binascii
import json
import teradatasql

def ReadLobValueFromLobLocator (con, abyLocator, sTypeName):
    if type (abyLocator) is not bytes:
        raise TypeError ("abyLocator must be bytes not {}".format (type (abyLocator)))
    with con.cursor () as cur:
        sSQL = "{fn teradata_parameter(1," + sTypeName + ")}select ?"
        print (sSQL)
        cur.execute (sSQL, [abyLocator])
        return cur.fetchone () [0]

with teradatasql.connect (host="whomooz", user="guest", password="please") as con:
    with con.cursor() as cur:
        sSQL = "create volatile table voltab (c1 integer, c2 blob, c3 clob, c4 xml, c5 st_geometry, c6 json) on commit preserve rows"
        print (sSQL)
        cur.execute (sSQL)

        sXML = '<?xml version="1.0" encoding="UTF-8"?><foo>bar</foo>'
        sJSON = '{"foo":"bar"}'
        sSQL = "insert into voltab values (1, '{}'xbv, 'clobval', '{}', 'point(1 2)', '{}')".format (binascii.hexlify (b"ABC").decode (), sXML, sJSON)
        print (sSQL)
        cur.execute (sSQL)

        sSQL = "{fn teradata_lobselect(S)}{fn teradata_fake_result_sets}select * from voltab order by 1"
        print (sSQL)
        cur.execute (sSQL)

        aoFakeResultSetRow = cur.fetchone ()
        sResultSetColumnMetadataJSON = aoFakeResultSetRow [7]
        amapResultSetColumnMetadata = json.loads (sResultSetColumnMetadataJSON)
        cur.nextset ()
        aoRealResultSetRow = cur.fetchone ()

        for iColumn in range (len (aoRealResultSetRow)):
            oValue = aoRealResultSetRow [iColumn]
            sTypeName = amapResultSetColumnMetadata [iColumn] ["TypeName"]
            if sTypeName.startswith ("LOCATOR("):
                oValue = ReadLobValueFromLobLocator (con, oValue, sTypeName)
            print ("Column {} {} value: {}".format (iColumn + 1, sTypeName, oValue))
