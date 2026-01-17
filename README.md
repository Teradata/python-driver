## Teradata SQL Driver for Python

This package enables Python applications to connect to the Teradata Database.

This package implements the [PEP-249 Python Database API Specification 2.0](https://www.python.org/dev/peps/pep-0249/).

This package requires 64-bit Python 3.7 or later and runs on the following operating systems and processor architectures. 32-bit Python is not supported.
* Windows x64 on 64-bit Intel and AMD processors
* macOS on 64-bit ARM processors
* macOS on 64-bit Intel processors
* Linux x64 on 64-bit Intel and AMD processors
* Linux ARM64 on 64-bit ARM processors
* Linux ppc64le on 64-bit Power processors

For community support, please visit [Teradata Community](https://support.teradata.com/community).

For Teradata customer support, please visit [Teradata Customer Service](https://support.teradata.com/).

Please note, this driver may contain beta/preview features ("Beta Features"). As such, by downloading and/or using the driver, in addition to agreeing to the licensing terms below, you acknowledge that the Beta Features are experimental in nature and that the Beta Features are provided "AS IS" and may not be functional on any machine or in any environment.

Copyright 2026 Teradata. All Rights Reserved.

### Table of Contents

* [Features](#Features)
* [Limitations](#Limitations)
* [Installation](#Installation)
* [License](#License)
* [Documentation](#Documentation)
* [Sample Programs](#SamplePrograms)
* [Using the Driver](#Using)
* [Connection Parameters](#ConnectionParameters)
* [FIPS Mode](#FIPSMode)
* [COP Discovery](#COPDiscovery)
* [Stored Password Protection](#StoredPasswordProtection)
* [Logon Authentication Methods](#LogonMethods)
* [Client Attributes](#ClientAttributes)
* [User STARTUP SQL Request](#UserStartup)
* [Session Reconnect](#SessionReconnect)
* [Transaction Mode](#TransactionMode)
* [Auto-Commit](#AutoCommit)
* [Data Types](#DataTypes)
* [Null Values](#NullValues)
* [Character Export Width](#CharacterExportWidth)
* [Module Constructors](#ModuleConstructors)
* [Module Globals](#ModuleGlobals)
* [Module Functions](#ModuleFunctions)
* [Module Exceptions](#ModuleExceptions)
* [Connection Attributes](#ConnectionAttributes)
* [Connection Methods](#ConnectionMethods)
* [Cursor Attributes](#CursorAttributes)
* [Cursor Methods](#CursorMethods)
* [Type Objects](#TypeObjects)
* [Escape Syntax](#EscapeSyntax)
* [FastLoad](#FastLoad)
* [FastExport](#FastExport)
* [CSV Batch Inserts](#CSVBatchInserts)
* [CSV Export Results](#CSVExportResults)
* [Command Line Interface](#CommandLineInterface)
* [Change Log](#ChangeLog)

<a id="Features"></a>

### Features

The *Teradata SQL Driver for Python* is a DBAPI Driver that enables Python applications to connect to the Teradata Database. The driver implements the [PEP-249 Python Database API Specification 2.0](https://www.python.org/dev/peps/pep-0249/).

The driver is a young product that offers a basic feature set. We are working diligently to add features to the driver, and our goal is feature parity with the Teradata JDBC Driver.

At the present time, the driver offers the following features.

* Supported for use with Teradata database 16.20 and later releases.
* [COP Discovery](#COPDiscovery).
* Laddered Concurrent Connect.
* [HTTPS](https://en.wikipedia.org/wiki/HTTPS)/[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) connections with Teradata database 16.20.53.30 and later.
* Encrypted logon.
* [GSS-API](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) logon authentication methods `KRB5` (Kerberos), `LDAP`, `TD2`, and `TDNEGO`.
* [OpenID Connect (OIDC)](https://en.wikipedia.org/wiki/OpenID#OpenID_Connect_(OIDC)) logon authentication methods `BEARER`, `BROWSER`, `CODE`, `CRED`, `JWT`, `ROPC`, and `SECRET`.
* Data encryption provided by TLS for HTTPS connections.
* For non-HTTPS connections, data encryption governed by central administration or enabled via the `encryptdata` connection parameter.
* Recoverable Network Protocol and Redrive.
* Unicode character data transferred via the UTF8 session character set.
* [Auto-commit](#AutoCommit) for ANSI and TERA transaction modes.
* Result set row size up to 1 MB.
* Multi-statement requests that return multiple result sets.
* Most JDBC escape syntax.
* Parameterized SQL requests with question-mark parameter markers.
* Parameterized batch SQL requests with multiple rows of data bound to question-mark parameter markers.
* Auto-Generated Key Retrieval (AGKR) for identity column values and more.
* Large Object (LOB) support for the BLOB and CLOB data types.
* Complex data types such as `XML`, `JSON`, `DATASET STORAGE FORMAT AVRO`, and `DATASET STORAGE FORMAT CSV`.
* ElicitFile protocol support for DDL commands that create external UDFs or stored procedures and upload a file from client to database.
* `CREATE PROCEDURE` and `REPLACE PROCEDURE` commands.
* Stored Procedure Dynamic Result Sets.
* FastLoad and FastExport.
* Monitor partition.

<a id="Limitations"></a>

### Limitations

* The UTF8 session character set is always used. The `charset` connection parameter is not supported.

<a id="Installation"></a>

### Installation

The `teradatasql` package depends on the `pycryptodome` package which is available from PyPI.

Use `pip install` to download and install the driver and its dependencies automatically.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install teradatasql`
Windows        | `py -3 -m pip install teradatasql`

When upgrading to a new version of the driver, you may need to use pip install's `--no-cache-dir` option to force the download of the new version.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install --no-cache-dir -U teradatasql`
Windows        | `py -3 -m pip install --no-cache-dir -U teradatasql`

The `teradatasql` package depends on the `pycryptodome` package, because one of the included sample programs (`TJEncryptPassword.py`) uses `pycryptodome`. The driver itself does not use `pycryptodome`.

If you want to avoid installing `pycryptodome`, you can use the `--no-deps` option of pip install to avoid installing `pycryptodome`. Without `pycryptodome`, you will not be able to run the `TJEncryptPassword.py` sample program.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install --no-deps teradatasql`
Windows        | `py -3 -m pip install --no-deps teradatasql`

<a id="License"></a>

### License

Use of the driver is governed by the [License Agreement for the Teradata SQL Driver for Python](https://github.com/Teradata/python-driver/blob/master/LICENSE).

When the driver is installed, the `LICENSE` and `THIRDPARTYLICENSE` files are placed in the `teradatasql` directory under your Python installation directory.

In addition to the license terms, the driver may contain beta/preview features ("Beta Features"). As such, by downloading and/or using the driver, in addition to the licensing terms, you acknowledge that the Beta Features are experimental in nature and that the Beta Features are provided "AS IS" and may not be functional on any machine or in any environment.

<a id="Documentation"></a>

### Documentation

When the driver is installed, the `README.md` file is placed in the `teradatasql` directory under your Python installation directory. This permits you to view the documentation offline, when you are not connected to the Internet.

The `README.md` file is a plain text file containing the documentation for the driver. While the file can be viewed with any text file viewer or editor, your viewing experience will be best with an editor that understands Markdown format.

<a id="SamplePrograms"></a>

### Sample Programs

Sample programs are provided to demonstrate how to use the driver. When the driver is installed, the sample programs are placed in the `teradatasql/samples` directory under your Python installation directory.

The sample programs are coded with a fake database hostname `whomooz`, username `guest`, and password `please`. Substitute your actual database hostname and credentials before running a sample program.

Program                                                                                                             | Purpose
------------------------------------------------------------------------------------------------------------------- | ---
[AbortSession.py](https://github.com/Teradata/python-driver/blob/master/samples/AbortSession.py)                    | Demonstrates how to abort a session
[AGKRBatchInsert.py](https://github.com/Teradata/python-driver/blob/master/samples/AGKRBatchInsert.py)              | Demonstrates how to insert a batch of rows with Auto-Generated Key Retrieval (AGKR)
[AGKRInsertSelect.py](https://github.com/Teradata/python-driver/blob/master/samples/AGKRInsertSelect.py)            | Demonstrates Insert/Select with Auto-Generated Key Retrieval (AGKR)
[BatchInsert.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsert.py)                      | Demonstrates how to insert a batch of rows
[BatchInsertCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsertCSV.py)                | Demonstrates how to insert a batch of rows from a CSV file
[BatchInsPerf.py](https://github.com/Teradata/python-driver/blob/master/samples/BatchInsPerf.py)                    | Measures time to insert one million rows
[CancelSleep.py](https://github.com/Teradata/python-driver/blob/master/samples/CancelSleep.py)                      | Demonstrates how to use the cancel method to interrupt a query
[CharPadding.py](https://github.com/Teradata/python-driver/blob/master/samples/CharPadding.py)                      | Demonstrates the database's *Character Export Width* behavior
[CommitRollback.py](https://github.com/Teradata/python-driver/blob/master/samples/CommitRollback.py)                | Demonstrates commit and rollback methods with auto-commit off.
[DecimalDigits.py](https://github.com/Teradata/python-driver/blob/master/samples/DecimalDigits.py)                  | Demonstrates how to format decimal.Decimal values.
[DriverDatabaseVersion.py](https://github.com/Teradata/python-driver/blob/master/samples/DriverDatabaseVersion.py)  | Displays the driver version and database version
[ElicitFile.py](https://github.com/Teradata/python-driver/blob/master/samples/ElicitFile.py)                        | Demonstrates C source file upload to create a User-Defined Function (UDF)
[ExportCSVResult.py](https://github.com/Teradata/python-driver/blob/master/samples/ExportCSVResult.py)              | Demonstrates how to export a query result set to a CSV file
[ExportCSVResults.py](https://github.com/Teradata/python-driver/blob/master/samples/ExportCSVResults.py)            | Demonstrates how to export multiple query result sets to CSV files
[FakeExportCSVResults.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeExportCSVResults.py)    | Demonstrates how to export multiple query result sets with the metadata to CSV files
[FakeResultSetCon.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeResultSetCon.py)            | Demonstrates connection parameter for fake result sets
[FakeResultSetEsc.py](https://github.com/Teradata/python-driver/blob/master/samples/FakeResultSetEsc.py)            | Demonstrates escape function for fake result sets
[FastExportCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/FastExportCSV.py)                  | Demonstrates how to FastExport rows from a table to a CSV file
[FastExportTable.py](https://github.com/Teradata/python-driver/blob/master/samples/FastExportTable.py)              | Demonstrates how to FastExport rows from a table
[FastLoadBatch.py](https://github.com/Teradata/python-driver/blob/master/samples/FastLoadBatch.py)                  | Demonstrates how to FastLoad batches of rows
[FastLoadCSV.py](https://github.com/Teradata/python-driver/blob/master/samples/FastLoadCSV.py)                      | Demonstrates how to FastLoad batches of rows from a CSV file
[HelpSession.py](https://github.com/Teradata/python-driver/blob/master/samples/HelpSession.py)                      | Displays session information
[IgnoreErrors.py](https://github.com/Teradata/python-driver/blob/master/samples/IgnoreErrors.py)                    | Demonstrates how to ignore errors
[InsertLob.py](https://github.com/Teradata/python-driver/blob/master/samples/InsertLob.py)                          | Demonstrates how to insert BLOB and CLOB values
[InsertVector.py](https://github.com/Teradata/python-driver/blob/master/samples/InsertVector.py)                    | Demonstrates how to insert Vector values
[InsertXML.py](https://github.com/Teradata/python-driver/blob/master/samples/InsertXML.py)                          | Demonstrates how to insert and retrieve XML values
[LoadCSVFile.py](https://github.com/Teradata/python-driver/blob/master/samples/LoadCSVFile.py)                      | Demonstrates how to load data from a CSV file into a table
[LobLocators.py](https://github.com/Teradata/python-driver/blob/master/samples/LobLocators.py)                      | Demonstrates how to use LOB locators
[MetadataFromPrepare.py](https://github.com/Teradata/python-driver/blob/master/samples/MetadataFromPrepare.py)      | Demonstrates how to prepare a SQL request and obtain SQL statement metadata
[MonitorAbort.py](https://github.com/Teradata/python-driver/blob/master/samples/MonitorAbort.py)                    | Demonstrates how to use the Monitor partition to abort a session
[MonitorQueries.py](https://github.com/Teradata/python-driver/blob/master/samples/MonitorQueries.py)                | Demonstrates how to execute Monitor partition queries
[MultiThread.py](https://github.com/Teradata/python-driver/blob/master/samples/MultiThread.py)                      | Demonstrates how to use multiple threads to load data in parallel
[ParamDataTypes.py](https://github.com/Teradata/python-driver/blob/master/samples/ParamDataTypes.py)                | Demonstrates how to specify data types for parameter marker bind values
[ShowCommand.py](https://github.com/Teradata/python-driver/blob/master/samples/ShowCommand.py)                      | Displays the results from the `SHOW` command
[StoredProc.py](https://github.com/Teradata/python-driver/blob/master/samples/StoredProc.py)                        | Demonstrates how to create and call a SQL stored procedure
[TJEncryptPassword.py](https://github.com/Teradata/python-driver/blob/master/samples/TJEncryptPassword.py)          | Creates encrypted password files

<a id="Using"></a>

### Using the Driver

Your Python script must import the `teradatasql` package in order to use the driver.

    import teradatasql

After importing the `teradatasql` package, your Python script calls the `teradatasql.connect` function to open a connection to the database.

You may specify connection parameters as a JSON string, as `kwargs`, or using a combination of the two approaches. The `teradatasql.connect` function's first argument is an optional JSON string. The `teradatasql.connect` function's second and subsequent arguments are optional `kwargs`.

Connection parameters specified only as `kwargs`:

    con = teradatasql.connect(host="whomooz", user="guest", password="please")

Connection parameters specified only as a JSON string:

    con = teradatasql.connect('{"host":"whomooz","user":"guest","password":"please"}')

Connection parameters specified using a combination:

    con = teradatasql.connect('{"host":"whomooz"}', user="guest", password="please")

When a combination of parameters are specified, connection parameters specified as `kwargs` take precedence over same-named connection parameters specified in the JSON string.

<a id="ConnectionParameters"></a>

### Connection Parameters

The following table lists the connection parameters currently offered by the driver. Connection parameter values are case-sensitive unless stated otherwise.

Our goal is consistency for the connection parameters offered by this driver and the Teradata JDBC Driver, with respect to connection parameter names and functionality. For comparison, Teradata JDBC Driver connection parameters are [documented here](https://downloads.teradata.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#BGBHDDGB).

Parameter               | Default     | Type           | Description
----------------------- | ----------- | -------------- | ---
`account`               |             | string         | <a id="cp_account"></a>               Specifies the database account. Equivalent to the Teradata JDBC Driver `ACCOUNT` connection parameter.
`browser`               |             | string         | <a id="cp_browser"></a>               Specifies the command to open the browser for Browser Authentication when `logmech` is `BROWSER`. Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `BROWSER` connection parameter.<br/>The specified command must include a placeholder token, literally specified as `PLACEHOLDER`, which the driver will replace with the Identity Provider authorization endpoint URL. The `PLACEHOLDER` token is case-sensitive and must be specified in uppercase.<br/>&bull; On Windows, the default command is `cmd /c start "title" "PLACEHOLDER"`. Windows command syntax requires the quoted title to precede the quoted URL.<br/>&bull; On macOS, the default command is `open PLACEHOLDER`. macOS command syntax does not allow the URL to be quoted.
`browser_tab_timeout`   | `"5"`       | quoted integer | <a id="cp_browser_tab_timeout"></a>   Specifies the number of seconds to wait before closing the browser tab after Browser Authentication is completed. The default is 5 seconds. The behavior is under the browser's control, and not all browsers support automatic closing of browser tabs. Typically, the tab used to log on will remain open indefinitely, but the second and subsequent tabs will be automatically closed. Specify `0` (zero) to close the tab immediately. Specify `-1` to turn off automatic closing of browser tabs. Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `BROWSER_TAB_TIMEOUT` connection parameter.
`browser_timeout`       | `"180"`     | quoted integer | <a id="cp_browser_timeout"></a>       Specifies the number of seconds that the driver will wait for Browser Authentication to complete. The default is 180 seconds (3 minutes). Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `BROWSER_TIMEOUT` connection parameter.
`code_append_file`      | `"-out"`    | string         | <a id="cp_code_append_file"></a>      Specifies how to display the verification URL and code. Optional when `logmech` is `CODE` and ignored for other `logmech` values. The default `-out` prints the verification URL and code to stdout. Specify `-err` to print the verification URL and code to stderr. Specify a file name to append the verification URL and code to an existing file or create a new file if the file does not exist. Equivalent to the Teradata JDBC Driver `CODE_APPEND_FILE` connection parameter.
`column_name`           | `"false"`   | quoted boolean | <a id="cp_column_name"></a>           Controls the behavior of cursor `.description` sequence `name` items. Equivalent to the Teradata JDBC Driver `COLUMN_NAME` connection parameter. False specifies that a cursor `.description` sequence `name` item provides the AS-clause name if available, or the column name if available, or the column title. True specifies that a cursor `.description` sequence `name` item provides the column name if available, but has no effect when StatementInfo parcel support is unavailable.
`concurrent_interval`   | `"1000"`    | quoted integer | <a id="cp_concurrent_interval"></a>   Specifies the interval in milliseconds for Laddered Concurrent Connect (LCC) to wait before starting another concurrent connection attempt.
`concurrent_limit`      | `"3"`       | quoted integer | <a id="cp_concurrent_limit"></a>      Limits the number of concurrent connection attempts.
`connect_failure_ttl`   | `"0"`       | quoted integer | <a id="cp_connect_failure_ttl"></a>   Specifies the time-to-live in seconds to remember the most recent connection failure for each IP address/port combination. The driver subsequently skips connection attempts to that IP address/port for the duration of the time-to-live. The default value of zero disables this feature. The recommended value is half the database restart time. Equivalent to the Teradata JDBC Driver `CONNECT_FAILURE_TTL` connection parameter.
`connect_function`      | `"0"`       | quoted integer | <a id="cp_connect_function"></a>      Specifies whether the database should allocate a Logon Sequence Number (LSN) for this session, or associate this session with an existing LSN. Specify `0` for a session with no LSN (the default). Specify `1` to allocate a new LSN for the session. Specify `2` to associate the session with the existing LSN identified by the `logon_sequence_number` connection parameter. The database only permits sessions for the same user to share an LSN. Equivalent to the Teradata JDBC Driver `CONNECT_FUNCTION` connection parameter.
`connect_timeout`       | `"10000"`   | quoted integer | <a id="cp_connect_timeout"></a>       Specifies the timeout in milliseconds for establishing a TCP socket connection. Specify `0` for no timeout. The default is 10 seconds (10000 milliseconds).
`cop`                   | `"true"`    | quoted boolean | <a id="cp_cop"></a>                   Specifies whether COP Discovery is performed. Equivalent to the Teradata JDBC Driver `COP` connection parameter.
`coplast`               | `"false"`   | quoted boolean | <a id="cp_coplast"></a>               Specifies how COP Discovery determines the last COP hostname. Equivalent to the Teradata JDBC Driver `COPLAST` connection parameter. When `coplast` is `false` or omitted, or COP Discovery is turned off, then no DNS lookup occurs for the coplast hostname. When `coplast` is `true`, and COP Discovery is turned on, then a DNS lookup occurs for a coplast hostname.
`database`              |             | string         | <a id="cp_database"></a>              Specifies the initial database to use after logon, instead of the user's default database. Equivalent to the Teradata JDBC Driver `DATABASE` connection parameter.
`dbs_port`              | `"1025"`    | quoted integer | <a id="cp_dbs_port"></a>              Specifies the database port number. Equivalent to the Teradata JDBC Driver `DBS_PORT` connection parameter.
`encryptdata`           | `"false"`   | quoted boolean | <a id="cp_encryptdata"></a>           Controls encryption of data exchanged between the driver and the database. Equivalent to the Teradata JDBC Driver `ENCRYPTDATA` connection parameter.
`error_query_count`     | `"21"`      | quoted integer | <a id="cp_error_query_count"></a>     Specifies how many times the driver will attempt to query FastLoad Error Table 1 after a FastLoad operation. Equivalent to the Teradata JDBC Driver `ERROR_QUERY_COUNT` connection parameter.
`error_query_interval`  | `"500"`     | quoted integer | <a id="cp_error_query_interval"></a>  Specifies how many milliseconds the driver will wait between attempts to query FastLoad Error Table 1. Equivalent to the Teradata JDBC Driver `ERROR_QUERY_INTERVAL` connection parameter.
`error_table_1_suffix`  | `"_ERR_1"`  | string         | <a id="cp_error_table_1_suffix"></a>  Specifies the suffix for the name of FastLoad Error Table 1. Equivalent to the Teradata JDBC Driver `ERROR_TABLE_1_SUFFIX` connection parameter.
`error_table_2_suffix`  | `"_ERR_2"`  | string         | <a id="cp_error_table_2_suffix"></a>  Specifies the suffix for the name of FastLoad Error Table 2. Equivalent to the Teradata JDBC Driver `ERROR_TABLE_2_SUFFIX` connection parameter.
`error_table_database`  |             | string         | <a id="cp_error_table_database"></a>  Specifies the database name for the FastLoad error tables. By default, FastLoad error tables reside in the same database as the destination table being loaded. Equivalent to the Teradata JDBC Driver `ERROR_TABLE_DATABASE` connection parameter.
`fake_result_sets`      | `"false"`   | quoted boolean | <a id="cp_fake_result_sets"></a>      Controls whether a fake result set containing statement metadata precedes each real result set.
`field_quote`           | `"\""`      | string         | <a id="cp_field_quote"></a>           Specifies a single character string used to quote fields in a CSV file.
`field_sep`             | `","`       | string         | <a id="cp_field_sep"></a>             Specifies a single character string used to separate fields in a CSV file. Equivalent to the Teradata JDBC Driver `FIELD_SEP` connection parameter.
`gateway_deadline`      | `"50"`      | quoted integer | <a id="cp_gateway_deadline"></a>      Specifies the Gateway deadline in seconds. The driver automatically closes and re-establishes the database socket connection if the OpenID Connect (OIDC) flow takes longer than this. Should be smaller than the Gateway's denial-of-service protection timeout: `gtwcontrol` setting "connection timeout in seconds" with default 60 seconds. Equivalent to the Teradata JDBC Driver `GATEWAY_DEADLINE` connection parameter.
`govern`                | `"true"`    | quoted boolean | <a id="cp_govern"></a>                Controls FastLoad and FastExport throttling by Teradata workload management rules. When set to `true` (the default), workload management rules may delay a FastLoad or FastExport. When set to `false`, workload management rules will reject rather than delay a FastLoad or FastExport. Equivalent to the Teradata JDBC Driver `GOVERN` connection parameter.
`host`                  |             | string         | <a id="cp_host"></a>                  Specifies the database hostname.
`http_proxy`            |             | string         | <a id="cp_http_proxy"></a>            Specifies the proxy server URL for HTTP connections to TLS certificate verification CRL and OCSP endpoints. The URL must begin with `http://` and must include a colon `:` and port number.
`http_proxy_password`   |             | string         | <a id="cp_http_proxy_password"></a>   Specifies the proxy server password for the proxy server identified by the `http_proxy` parameter. This parameter may only be specified in conjunction with the `http_proxy` parameter. When this parameter is omitted, no proxy server password is provided to the proxy server identified by the `http_proxy` parameter.
`http_proxy_user`       |             | string         | <a id="cp_http_proxy_user"></a>       Specifies the proxy server username for the proxy server identified by the `http_proxy` parameter. This parameter may only be specified in conjunction with the `http_proxy` parameter. When this parameter is omitted, no proxy server username is provided to the proxy server identified by the `http_proxy` parameter.
`https_port`            | `"443"`     | quoted integer | <a id="cp_https_port"></a>            Specifies the database port number for HTTPS/TLS connections. Equivalent to the Teradata JDBC Driver `HTTPS_PORT` connection parameter.
`https_proxy`           |             | string         | <a id="cp_https_proxy"></a>           Specifies the proxy server URL for HTTPS/TLS connections to the database and to Identity Provider endpoints. The URL must begin with `http://` and must include a colon `:` and port number. The driver connects to the proxy server using a non-TLS HTTP connection, then uses the HTTP CONNECT method to establish an HTTPS/TLS connection to the destination. Equivalent to the Teradata JDBC Driver `HTTPS_PROXY` connection parameter.
`https_proxy_password`  |             | string         | <a id="cp_https_proxy_password"></a>  Specifies the proxy server password for the proxy server identified by the `https_proxy` parameter. This parameter may only be specified in conjunction with the `https_proxy` parameter. When this parameter is omitted, no proxy server password is provided to the proxy server identified by the `https_proxy` parameter. Equivalent to the Teradata JDBC Driver `HTTPS_PROXY_PASSWORD` connection parameter.
`https_proxy_user`      |             | string         | <a id="cp_https_proxy_user"></a>      Specifies the proxy server username for the proxy server identified by the `https_proxy` parameter. This parameter may only be specified in conjunction with the `https_proxy` parameter. When this parameter is omitted, no proxy server username is provided to the proxy server identified by the `https_proxy` parameter. Equivalent to the Teradata JDBC Driver `HTTPS_PROXY_USER` connection parameter.
`https_retry`           | `"2"`       | quoted integer | <a id="cp_https_retry"></a>           Specifies the number of HTTPS connection retries for a single-node database. Specify `0` (zero) to turn off HTTPS connection retries. Equivalent to the Teradata JDBC Driver `HTTPS_RETRY` connection parameter.
`jws_algorithm`         | `"RS256"`   | string         | <a id="cp_jws_algorithm"></a>         Specifies the JSON Web Signature (JWS) algorithm to sign the JWT Bearer Token for client authentication. Optional when `logmech` is `BEARER` and ignored for other `logmech` values. The default `RS256` is RSASSA-PKCS1-v1_5 using SHA-256. Specify `RS384` for RSASSA-PKCS1-v1_5 using SHA-384. Specify `RS512` for RSASSA-PKCS1-v1_5 using SHA-512. Equivalent to the Teradata JDBC Driver `JWS_ALGORITHM` connection parameter.
`jws_cert`              |             | string         | <a id="cp_jws_cert"></a>              Specifies the file name of the X.509 certificate PEM file that contains the public key corresponding to the private key from `jws_private_key`. Optional when `logmech` is `BEARER` and ignored for other `logmech` values. When this parameter is specified, the "x5t" header thumbprint is added to the JWT Bearer Token for the Identity Provider to select the public key for JWT signature verification. Some Identity Providers, such as Microsoft Entra ID, require this. When this parameter is omitted, the "x5t" header thumbprint is not added to the JWT Bearer Token. Some Identity Providers do not require the "x5t" header thumbprint. Equivalent to the Teradata JDBC Driver `JWS_CERT` connection parameter.
`jws_private_key`       |             | string         | <a id="cp_jws_private_key"></a>       Specifies the file name of the PEM or JWK file containing the private key to sign the JWT Bearer Token for client authentication. Required when `logmech` is `BEARER` and ignored for other `logmech` values. PEM and JWK file formats are supported. The private key filename must end with the `.pem` or `.jwk` extension. A PEM file must contain the BEGIN/END PRIVATE KEY header and trailer. If a JWK file contains a "kid" (key identifier) parameter, the "kid" header is added to the JWT Bearer Token for the Identity Provider to select the public key for JWT signature verification. Equivalent to the Teradata JDBC Driver `JWS_PRIVATE_KEY` connection parameter.
`lob_support`           | `"true"`    | quoted boolean | <a id="cp_lob_support"></a>           Controls LOB support. Equivalent to the Teradata JDBC Driver `LOB_SUPPORT` connection parameter.
`local_catalog`         | `"false"`   | quoted boolean | <a id="cp_local_catalog"></a>         Controls the catalog name of local objects in result set metadata and parameter metadata. When set to `true` and Virtual System Dictionary (VSD) is available, local objects have the `TD_LOCAL` catalog name. Otherwise, local objects have an empty string for catalog name. This parameter does not affect the catalog name of Open Table Format (OTF) objects, which always have DataLake name as catalog name. Equivalent to the Teradata JDBC Driver `LOCAL_CATALOG` connection parameter.
`log`                   | `"0"`       | quoted integer | <a id="cp_log"></a>                   Controls debug logging. Somewhat equivalent to the Teradata JDBC Driver `LOG` connection parameter. This parameter's behavior is subject to change in the future. This parameter's value is currently defined as an integer in which the 1-bit governs function and method tracing, the 2-bit governs debug logging, the 4-bit governs transmit and receive message hex dumps, and the 8-bit governs timing. Compose the value by adding together 1, 2, 4, and/or 8.
`logdata`               |             | string         | <a id="cp_logdata"></a>               Specifies extra data for the chosen logon authentication method. Equivalent to the Teradata JDBC Driver `LOGDATA` connection parameter.
`logmech`               | `"TD2"`     | string         | <a id="cp_logmech"></a>               Specifies the [logon authentication method](#LogonMethods). Equivalent to the Teradata JDBC Driver `LOGMECH` connection parameter. The database user must have the "logon with null password" permission for `KRB5` Single Sign On (SSO) or any of the [OpenID Connect (OIDC)](https://en.wikipedia.org/wiki/OpenID#OpenID_Connect_(OIDC)) methods `BEARER`, `BROWSER`, `CODE`, `CRED`, `JWT`, `ROPC`, or `SECRET`. [GSS-API](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) methods are `KRB5`, `LDAP`, `TD2`, and `TDNEGO`. Values are case-insensitive.<br/>&bull; `BEARER` uses OIDC Client Credentials Grant with JWT Bearer Token for client authentication.<br/>&bull; `BROWSER` uses Browser Authentication, supported for Windows and macOS.<br/>&bull; `CODE` uses OIDC Device Code Flow, also known as OIDC Device Authorization Grant.<br/>&bull; `CRED` uses OIDC Client Credentials Grant with client_secret_post for client authentication.<br/>&bull; `JWT` uses JSON Web Token.<br/>&bull; `KRB5` uses Kerberos V5.<br/>&bull; `LDAP` uses Lightweight Directory Access Protocol.<br/>&bull; `ROPC` uses OIDC Resource Owner Password Credentials (ROPC).<br/>&bull; `SECRET` uses OIDC Client Credentials Grant with client_secret_basic for client authentication.<br/>&bull; `TD2` uses Teradata Method 2.<br/>&bull; `TDNEGO` automatically selects an appropriate GSS-API logon authentication method. OIDC methods are not selected.
`logon_sequence_number` |             | quoted integer | <a id="cp_logon_sequence_number"></a> Associates this session with an existing Logon Sequence Number (LSN) when `connect_function` is `2`. The database only permits sessions for the same user to share an LSN. An LSN groups multiple sessions together for workload management. Using an LSN is a three-step process. First, establish a control session with `connect_function` as `1`, which allocates a new LSN. Second, obtain the LSN from the control session using the escape function `{fn teradata_logon_sequence_number}`. Third, establish an associated session with `connect_function` as `2` and the logon sequence number. Equivalent to the Teradata JDBC Driver `LOGON_SEQUENCE_NUMBER` connection parameter.
`logon_timeout`         | `"0"`       | quoted integer | <a id="cp_logon_timeout"></a>         Specifies the logon timeout in seconds. Zero means no timeout. Equivalent to the Teradata JDBC Driver `LOGON_TIMEOUT` connection parameter.
`manage_error_tables`   | `"true"`    | quoted boolean | <a id="cp_manage_error_tables"></a>   Controls whether the driver manages the FastLoad error tables.
`max_message_body`      | `"2097000"` | quoted integer | <a id="cp_max_message_body"></a>      Specifies the maximum Response Message size in bytes. Equivalent to the Teradata JDBC Driver `MAX_MESSAGE_BODY` connection parameter.
`oauth_level`           | `"0"`       | quoted integer | <a id="cp_oauth_level"></a>           Controls Single Sign On (SSO) access to Open Table Format (OTF) catalog and storage instances. Equivalent to the Teradata JDBC Driver `OAUTH_LEVEL` connection parameter. If `redrive` is `1` or higher and the database supports Control Data, this specifies which tokens are transmitted to the database with each request, and the database may use the tokens for SSO access to OTF catalog and storage instances. If `redrive` is `0` or the database does not support Control Data, tokens are not transmitted to the database with each request, and tokens will not be available for SSO access to OTF. <br/>&bull; `0` (the default) disables sending tokens to the database. <br/>&bull; `1` sends the token from OIDC authentication to the database for each SQL request. <br/>&bull; `2` sends the OAuth tokens from `oauth_scopes` to the database for each SQL request. <br/>&bull; `3` sends the token from OIDC authentication and the OAuth tokens to the database for each SQL request.
`oauth_scopes`          |             | string         | <a id="cp_oauth_scopes"></a>          Specifies one or more OAuth scopes for SSO access to OTF catalog and storage instances. Multiple scopes are separated by vertical bar `\|` characters. This parameter may only be used with OIDC logon mechanisms for individual users, not for service accounts. When this parameter is specified, after successful OIDC authentication, the driver obtains an additional access token from the Identity Provider for each specified scope. Each additional access token request uses the same OIDC parameters as the initial OIDC authentication; only the scope is varied. Equivalent to the Teradata JDBC Driver `OAUTH_SCOPES` connection parameter.
`oidc_cache_size`       | `"100"`     | quoted integer | <a id="cp_oidc_cache_size"></a>       Specifies the maximum size of the OpenID Connect (OIDC) token cache for Browser Authentication and other OIDC methods. Equivalent to the Teradata JDBC Driver `OIDC_CACHE_SIZE` connection parameter.
`oidc_claim`            | `"email"`   | string         | <a id="cp_oidc_claim"></a>            Specifies the OpenID Connect (OIDC) claim to use for Browser Authentication and other OIDC methods. Equivalent to the Teradata JDBC Driver `OIDC_CLAIM` connection parameter.
`oidc_clientid`         |             | string         | <a id="cp_oidc_clientid"></a>         Specifies the OpenID Connect (OIDC) Client ID to use for Browser Authentication and other OIDC methods. When omitted, the default Client ID comes from the database's TdgssUserConfigFile.xml file. Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `OIDC_CLIENTID` connection parameter.
`oidc_metadata`         |             | string         | <a id="cp_oidc_metadata"></a>         Specifies the Identity Provider metadata URL for OpenID Connect (OIDC). When this connection parameter is omitted, the default metadata URL is provided by the database. This connection parameter is a troubleshooting tool only, and is not intended for normal production usage. Equivalent to the Teradata JDBC Driver `OIDC_METADATA` connection parameter.
`oidc_metadata_cache`   | `"600"`     | quoted integer | <a id="cp_oidc_metadata_cache"></a>   Specifies the lifetime in seconds for entries in the OpenID Connect (OIDC) Authorization Server metadata cache. Equivalent to the Teradata JDBC Driver `OIDC_METADATA_CACHE` connection parameter.
`oidc_prompt`           |             | string         | <a id="cp_oidc_prompt"></a>           Specifies the OpenID Connect (OIDC) prompt value to use for Browser Authentication. Optional when `logmech` is `BROWSER` and ignored for other `logmech` values. Ignored unless `user` is specified as an OIDC login hint. Specify `login` for the Identity Provider to prompt the user for credentials. May not be supported by all Identity Providers. The browser tab may not close automatically after Browser Authentication is completed. Equivalent to the Teradata JDBC Driver `OIDC_PROMPT` connection parameter.
`oidc_redirect_port`    | `"0"`       | string         | <a id="cp_oidc_redirect_port"></a>    Specifies the OIDC redirect port for Browser Authentication (Authorization Code Flow with PKCE). Optional when `logmech` is `BROWSER` and ignored for other `logmech` values. Omitting this parameter is recommended. The default port number `0` (zero) directs the driver to use an ephemeral port. [IETF RFC 8252 - OAuth 2.0 for Native Apps](https://datatracker.ietf.org/doc/html/rfc8252) section 7.3 dictates that an identity provider must allow any port number for the loopback IP redirect URI, to let clients obtain an available ephemeral port from the operating system. Only specify this parameter if your identity provider deviates from IETF RFC 8252 and requires a specific redirect port number. Specify a single port number or specify two port numbers separated by a hyphen as a port range (inclusive). Equivalent to the Teradata JDBC Driver `OIDC_REDIRECT_PORT` connection parameter.
`oidc_refresh`          | `"true"`    | quoted boolean | <a id="cp_oidc_refresh"></a>          Controls whether the driver uses an available refresh token to obtain a new token when the current token expires. Equivalent to the Teradata JDBC Driver `OIDC_REFRESH` connection parameter.
`oidc_refresh_percent`  | `"15"`      | quoted integer | <a id="cp_oidc_refresh_percent"></a>  Specifies the OpenID Connect (OIDC) token minimum remaining lifetime percentage for the driver to reuse a token. The driver will replace a token when its remaining lifetime falls below this percentage. Equivalent to the Teradata JDBC Driver `OIDC_REFRESH_PERCENT` connection parameter.<br/>&bull; Default `15` reuses a token for the first 85% of its lifetime and replaces it when its remaining lifetime falls below 15%.<br/>&bull; Specify `0` to turn off preemptive replacement and use the entire token lifetime.<br/>&bull; Specify `100` to never reuse a token and always obtain a new token.
`oidc_scope`            | `"openid"`  | string         | <a id="cp_oidc_scope"></a>            Specifies the OpenID Connect (OIDC) scope to use for Browser Authentication. Beginning with Teradata Database 17.20.03.11, the default scope can be specified in the database's `TdgssUserConfigFile.xml` file, using the `IdPConfig` element's `Scope` attribute. Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `OIDC_SCOPE` connection parameter.
`oidc_sslmode`          |             | string         | <a id="cp_oidc_sslmode"></a>          Specifies the mode for HTTPS connections to the Identity Provider. Equivalent to the Teradata JDBC Driver `OIDC_SSLMODE` connection parameter. Values are case-insensitive. When this parameter is omitted, the default is the value of the `sslmode` connection parameter.<br/>&bull; `ALLOW` does not perform certificate verification for HTTPS connections to the Identity Provider.<br/>&bull; `VERIFY-CA` verifies that the server certificate is valid and trusted.<br/>&bull; `VERIFY-FULL` verifies that the server certificate is valid and trusted, and verifies that the server certificate matches the Identity Provider hostname.
`oidc_token`            | `"access_token"` | string    | <a id="cp_oidc_token"></a>            Specifies the kind of OIDC token to use for Browser Authentication. Specify `id_token` to use the id_token instead of the access_token. Browser Authentication is supported for Windows and macOS. Equivalent to the Teradata JDBC Driver `OIDC_TOKEN` connection parameter.
`partition`             | `"DBC/SQL"` | string         | <a id="cp_partition"></a>             Specifies the database partition. Equivalent to the Teradata JDBC Driver `PARTITION` connection parameter.
`password`              |             | string         | <a id="cp_password"></a>              Specifies the database password. Equivalent to the Teradata JDBC Driver `PASSWORD` connection parameter.
`proxy_bypass_hosts`    |             | string         | <a id="cp_proxy_bypass_hosts"></a>    Specifies a matching pattern for hostnames and addresses to bypass the proxy server identified by the `http_proxy` and/or `https_proxy` parameter. This parameter may only be specified in conjunction with the `http_proxy` and/or `https_proxy` parameter. Separate multiple hostnames and addresses with a vertical bar `\|` character. Specify an asterisk `*` as a wildcard character. When this parameter is omitted, the default pattern `localhost\|127.*\|[::1]` bypasses the proxy server identified by the `http_proxy` and/or `https_proxy` parameter for common variations of the loopback address. Equivalent to the Teradata JDBC Driver `PROXY_BYPASS_HOSTS` connection parameter.
`request_timeout`       | `"0"`       | quoted integer | <a id="cp_request_timeout"></a>       Specifies the timeout in seconds for executing each SQL request. Zero means no timeout.
`runstartup`            | `"false"`   | quoted boolean | <a id="cp_runstartup"></a>            Controls whether the user's `STARTUP` SQL request is executed after logon. For more information, refer to [User STARTUP SQL Request](#UserStartup). Equivalent to the Teradata JDBC Driver `RUNSTARTUP` connection parameter.
`sessions`              |             | quoted integer | <a id="cp_sessions"></a>              Specifies the number of data transfer connections for FastLoad or FastExport. The default (recommended) lets the database choose the appropriate number of connections. Equivalent to the Teradata JDBC Driver `SESSIONS` connection parameter.
`sip_support`           | `"true"`    | quoted boolean | <a id="cp_sip_support"></a>           Controls whether StatementInfo parcel is used. Equivalent to the Teradata JDBC Driver `SIP_SUPPORT` connection parameter.
`sp_spl`                | `"true"`    | quoted boolean | <a id="cp_sp_spl"></a>                Controls whether stored procedure source code is saved in the database when a SQL stored procedure is created. Equivalent to the Teradata JDBC Driver `SP_SPL` connection parameter.
`sslbase64`             |             | string         | <a id="cp_sslbase64"></a>             Specifies the base64url encoded contents of a PEM file that contains Certificate Authority (CA) certificates for use with `sslmode` or `oidc_sslmode` values `VERIFY-CA` or `VERIFY-FULL`. Equivalent to the Teradata JDBC Driver `SSLBASE64` connection parameter. The base64url encoded value must conform to [IETF RFC 4648 Section 5 - Base 64 Encoding with URL and Filename Safe Alphabet](https://datatracker.ietf.org/doc/html/rfc4648#section-5).<br/>Example Linux command to print the base64url encoded contents of a PEM file:<br/>`base64 -w0 < cert.pem \| tr +/ -_ \| tr -d =`
`sslca`                 |             | string         | <a id="cp_sslca"></a>                 Specifies the file name of a PEM file that contains Certificate Authority (CA) certificates for use with `sslmode` or `oidc_sslmode` values `VERIFY-CA` or `VERIFY-FULL`. Equivalent to the Teradata JDBC Driver `SSLCA` connection parameter.
`sslcapath`             |             | string         | <a id="cp_sslcapath"></a>             Specifies a directory of PEM files that contain Certificate Authority (CA) certificates for use with `sslmode` or `oidc_sslmode` values `VERIFY-CA` or `VERIFY-FULL`. Only files with an extension of `.pem` are used. Other files in the specified directory are not used. Equivalent to the Teradata JDBC Driver `SSLCAPATH` connection parameter.
`sslcipher`             |             | string         | <a id="cp_sslcipher"></a>             Specifies the TLS cipher for HTTPS/TLS connections. Default lets database and driver choose the most appropriate TLS cipher. Omitting this parameter is recommended. Use this parameter only for troubleshooting TLS handshake issues. Equivalent to the Teradata JDBC Driver `SSLCIPHER` connection parameter.
`sslcrc`                | `"ALLOW"`   | string         | <a id="cp_sslcrc"></a>                Controls TLS certificate revocation checking (CRC) for HTTPS/TLS connections. Equivalent to the Teradata JDBC Driver `SSLCRC` connection parameter. Values are case-insensitive.<br/>&bull; `ALLOW` performs CRC for `sslmode` or `oidc_sslmode` `VERIFY-CA` and `VERIFY-FULL`, and provides soft fail CRC for `VERIFY-CA` and `VERIFY-FULL` to ignore CRC communication failures.<br/>&bull; `PREFER` performs CRC for all HTTPS connections, and provides soft fail CRC for `VERIFY-CA` and `VERIFY-FULL` to ignore CRC communication failures.<br/>&bull; `REQUIRE` performs CRC for all HTTPS connections, and requires CRC for `VERIFY-CA` and `VERIFY-FULL`.
`sslcrl`                | `"true"`    | quoted boolean | <a id="cp_sslcrl"></a>                Controls the use of Certificate Revocation List (CRL) for TLS certificate revocation checking for HTTPS/TLS connections. Online Certificate Status Protocol (OCSP) is preferred over CRL, so CRL is used when OSCP is unavailable. Equivalent to the Teradata JDBC Driver `SSLCRL` connection parameter.
`sslmode`               | `"PREFER"`  | string         | <a id="cp_sslmode"></a>               Specifies the mode for connections to the database. Equivalent to the Teradata JDBC Driver `SSLMODE` connection parameter. Values are case-insensitive.<br/>&bull; `DISABLE` disables HTTPS/TLS connections and uses only non-TLS connections.<br/>&bull; `ALLOW` uses non-TLS connections unless the database requires HTTPS/TLS connections.<br/>&bull; `PREFER` uses HTTPS/TLS connections unless the database does not offer HTTPS/TLS connections.<br/>&bull; `REQUIRE` uses only HTTPS/TLS connections.<br/>&bull; `VERIFY-CA` uses only HTTPS/TLS connections and verifies that the server certificate is valid and trusted.<br/>&bull; `VERIFY-FULL` uses only HTTPS/TLS connections, verifies that the server certificate is valid and trusted, and verifies that the server certificate matches the database hostname.
`sslnamedgroups`        |             | string         | <a id="cp_sslnamedgroups"></a>        Specifies the TLS key exchange named groups for HTTPS/TLS connections. Multiple named groups are separated by commas. Default lets database and driver choose the most appropriate named group. Omitting this parameter is recommended. Use this parameter only for troubleshooting TLS handshake issues. Equivalent to the Teradata JDBC Driver `SSLNAMEDGROUPS` connection parameter.
`sslocsp`               | `"true"`    | quoted boolean | <a id="cp_sslocsp"></a>               Controls the use of Online Certificate Status Protocol (OCSP) for TLS certificate revocation checking for HTTPS/TLS connections. Equivalent to the Teradata JDBC Driver `SSLOCSP` connection parameter.
`sslprotocol`           | `"TLSv1.2"` | string         | <a id="cp_sslprotocol"></a>           Specifies the TLS protocol for HTTPS/TLS connections. Omitting this parameter is recommended. Use this parameter only for troubleshooting TLS handshake issues. Equivalent to the Teradata JDBC Driver `SSLPROTOCOL` connection parameter.
`teradata_values`       | `"true"`    | quoted boolean | <a id="cp_teradata_values"></a>       Controls whether `str` or a more specific Python data type is used for certain result set column value types. Refer to the [Data Types](#DataTypes) table below for details.
`tmode`                 | `"DEFAULT"` | string         | <a id="cp_tmode"></a>                 Specifies the [transaction mode](#TransactionMode). Equivalent to the Teradata JDBC Driver `TMODE` connection parameter. Possible values are `DEFAULT` (the default), `ANSI`, or `TERA`.
`user`                  |             | string         | <a id="cp_user"></a>                  Specifies the database username. Equivalent to the Teradata JDBC Driver `USER` connection parameter.

<a id="FIPSMode"></a>

### FIPS Mode

Platform             | FIPS Mode | Description
---------------------|-----------|---
Windows              | Automatic | Always uses [Microsoft Go](https://github.com/microsoft/go). Always uses [Windows Cryptography API: Next Generation (CNG)](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal). Automatic FIPS mode based on Windows FIPS policy.
macOS                | Manual    | Always uses [Microsoft Go](https://github.com/microsoft/go). Always uses macOS [CryptoKit](https://developer.apple.com/documentation/cryptokit). Enable FIPS mode with environment variable `GODEBUG=fips140=on`
Linux x64 and ARM64  | Automatic | Uses [Microsoft Go](https://github.com/microsoft/go) and Linux `libcrypto.so` if Linux FIPS mode is enabled. Uses [standard Go](https://go.dev/dl/) if FIPS mode is disabled.
Linux ppc64le        | Manual    | Always uses [standard Go](https://go.dev/dl/). Enable FIPS mode with environment variable `GODEBUG=fips140=on`

<a id="COPDiscovery"></a>

### COP Discovery

The driver provides Communications Processor (COP) discovery behavior when the `cop` connection parameter is `true` or omitted. COP Discovery is turned off when the `cop` connection parameter is `false`.

A database system can be composed of multiple database nodes. One or more of the database nodes can be configured to run the database Gateway process. Each database node that runs the database Gateway process is termed a Communications Processor, or COP. COP Discovery refers to the procedure of identifying all the available COP hostnames and their IP addresses. COP hostnames can be defined in DNS, or can be defined in the client system's `hosts` file. Teradata strongly recommends that COP hostnames be defined in DNS, rather than the client system's `hosts` file. Defining COP hostnames in DNS provides centralized administration, and enables centralized changes to COP hostnames if and when the database is reconfigured.

The `coplast` connection parameter specifies how COP Discovery determines the last COP hostname.
* When `coplast` is `false` or omitted, or COP Discovery is turned off, then the driver will not perform a DNS lookup for the coplast hostname.
* When `coplast` is `true`, and COP Discovery is turned on, then the driver will first perform a DNS lookup for a coplast hostname to obtain the IP address of the last COP hostname before performing COP Discovery. Subsequently, during COP Discovery, the driver will stop searching for COP hostnames when either an unknown COP hostname is encountered, or a COP hostname is encountered whose IP address matches the IP address of the coplast hostname.

Specifying `coplast` as `true` can improve performance with DNS that is slow to respond for DNS lookup failures, and is necessary for DNS that never returns a DNS lookup failure.

When performing COP Discovery, the driver starts with cop1, which is appended to the database hostname, and then proceeds with cop2, cop3, ..., copN. The driver supports domain-name qualification for COP Discovery and the coplast hostname. Domain-name qualification is recommended, because it can improve performance by avoiding unnecessary DNS lookups for DNS search suffixes.

The following table illustrates the DNS lookups performed for a hypothetical three-node database system named "whomooz".

&nbsp; | No domain name qualification | With domain name qualification<br/>(Recommended)
------ | ---------------------------- | ---
Application-specified<br/>database hostname | `whomooz` | `whomooz.domain.com`
Default: COP Discovery turned on, and `coplast` is `false` or omitted,<br/>perform DNS lookups until unknown COP hostname is encountered | `whomoozcop1`&rarr;`10.0.0.1`<br/>`whomoozcop2`&rarr;`10.0.0.2`<br/>`whomoozcop3`&rarr;`10.0.0.3`<br/>`whomoozcop4`&rarr;undefined | `whomoozcop1.domain.com`&rarr;`10.0.0.1`<br/>`whomoozcop2.domain.com`&rarr;`10.0.0.2`<br/>`whomoozcop3.domain.com`&rarr;`10.0.0.3`<br/>`whomoozcop4.domain.com`&rarr;undefined
COP Discovery turned on, and `coplast` is `true`,<br/>perform DNS lookups until COP hostname is found whose IP address matches the coplast hostname, or unknown COP hostname is encountered | `whomoozcoplast`&rarr;`10.0.0.3`<br/>`whomoozcop1`&rarr;`10.0.0.1`<br/>`whomoozcop2`&rarr;`10.0.0.2`<br/>`whomoozcop3`&rarr;`10.0.0.3` | `whomoozcoplast.domain.com`&rarr;`10.0.0.3`<br/>`whomoozcop1.domain.com`&rarr;`10.0.0.1`<br/>`whomoozcop2.domain.com`&rarr;`10.0.0.2`<br/>`whomoozcop3.domain.com`&rarr;`10.0.0.3`
COP Discovery turned off and round-robin DNS,<br/>perform one DNS lookup that returns multiple IP addresses | `whomooz`&rarr;`10.0.0.1`, `10.0.0.2`, `10.0.0.3` | `whomooz.domain.com`&rarr;`10.0.0.1`, `10.0.0.2`, `10.0.0.3`

Round-robin DNS rotates the list of IP addresses automatically to provide load distribution. Round-robin is only possible with DNS, not with the client system `hosts` file.

The driver supports the definition of multiple IP addresses for COP hostnames and non-COP hostnames.

For the first connection to a particular database system, the driver generates a random number to index into the list of COPs. For each subsequent connection, the driver increments the saved index until it wraps around to the first position. This behavior provides load distribution across all discovered COPs.

The driver masks connection failures to down COPs, thereby hiding most connection failures from the client application. An exception is thrown to the application only when all the COPs are down for that database. If a COP is down, the next COP in the sequence (including a wrap-around to the first COP) receives extra connections that were originally destined for the down COP. When multiple IP addresses are defined in DNS for a COP, the driver will attempt to connect to each of the COP's IP addresses, and the COP is considered down only when connection attempts fail to all of the COP's IP addresses.

If COP Discovery is turned off, or no COP hostnames are defined in DNS, the driver connects directly to the hostname specified in the `host` connection parameter. This permits load distribution schemes other than the COP Discovery approach. For example, round-robin DNS or a TCP/IP load distribution product can be used. COP Discovery takes precedence over simple database hostname lookup. To use an alternative load distribution scheme, either ensure that no COP hostnames are defined in DNS, or turn off COP Discovery with `cop` as `false`.

<a id="StoredPasswordProtection"></a>

### Stored Password Protection

#### Overview

Stored Password Protection enables an application to provide a connection password in encrypted form to the driver.

An encrypted password may be specified in the following contexts:
* A login password specified as the `password` connection parameter.
* A login password specified within the `logdata` connection parameter.

If the password, however specified, begins with the prefix `ENCRYPTED_PASSWORD(` then the specified password must follow this format:

`ENCRYPTED_PASSWORD(file:`*PasswordEncryptionKeyFileName*`,file:`*EncryptedPasswordFileName*`)`

Each filename must be preceded by the `file:` prefix. The *PasswordEncryptionKeyFileName* must be separated from the *EncryptedPasswordFileName* by a single comma.

The *PasswordEncryptionKeyFileName* specifies the name of a file that contains the password encryption key and associated information. The *EncryptedPasswordFileName* specifies the name of a file that contains the encrypted password and associated information. The two files are described below.

Stored Password Protection is offered by this driver, the Teradata JDBC Driver, and the Teradata SQL Driver for R. These drivers use the same file format.

#### Program TJEncryptPassword

`TJEncryptPassword.py` is a sample program to create encrypted password files for use with Stored Password Protection. When the driver is installed, the sample programs are placed in the `teradatasql/samples` directory under your Python installation directory.

This program works in conjunction with Stored Password Protection offered by the driver. This program creates the files containing the password encryption key and encrypted password, which can be subsequently specified via the `ENCRYPTED_PASSWORD(` syntax.

You are not required to use this program to create the files containing the password encryption key and encrypted password. You can develop your own software to create the necessary files. You may also use the [`TJEncryptPassword.java`](https://downloads.teradata.com/doc/connectivity/jdbc/reference/current/samp/TJEncryptPassword.java.txt) sample program that is available with the [Teradata JDBC Driver Reference](https://downloads.teradata.com/doc/connectivity/jdbc/reference/current/frameset.html). The only requirement is that the files must match the format expected by the driver, which is documented below.

This program encrypts the password and then immediately decrypts the password, in order to verify that the password can be successfully decrypted. This program mimics the password decryption of the driver, and is intended to openly illustrate its operation and enable scrutiny by the community.

The encrypted password is only as safe as the two files. You are responsible for restricting access to the files containing the password encryption key and encrypted password. If an attacker obtains both files, the password can be decrypted. The operating system file permissions for the two files should be as limited and restrictive as possible, to ensure that only the intended operating system userid has access to the files.

The two files can be kept on separate physical volumes, to reduce the risk that both files might be lost at the same time. If either or both of the files are located on a network volume, then an encrypted wire protocol can be used to access the network volume, such as sshfs, encrypted NFSv4, or encrypted SMB 3.0.

This program accepts eight command-line arguments:

Argument                      | Example              | Description
----------------------------- | -------------------- | ---
Transformation                | `AES/CBC/NoPadding`  | Specifies the transformation in the form *Algorithm*`/`*Mode*`/`*Padding*. Supported transformations are listed in a table below.
KeySizeInBits                 | `256`                | Specifies the algorithm key size, which governs the encryption strength.
MAC                           | `HmacSHA256`         | Specifies the message authentication code (MAC) algorithm `HmacSHA1` or `HmacSHA256`.
PasswordEncryptionKeyFileName | `PassKey.properties` | Specifies a filename in the current directory, a relative pathname, or an absolute pathname. The file is created by this program. If the file already exists, it will be overwritten by the new file.
EncryptedPasswordFileName     | `EncPass.properties` | Specifies a filename in the current directory, a relative pathname, or an absolute pathname. The filename or pathname that must differ from the PasswordEncryptionKeyFileName. The file is created by this program. If the file already exists, it will be overwritten by the new file.
Hostname                      | `whomooz`            | Specifies the database hostname.
Username                      | `guest`              | Specifies the database username.
Password                      | `please`             | Specifies the database password to be encrypted. Unicode characters in the password can be specified with the `\u`*XXXX* escape sequence.

#### Example Commands

The TJEncryptPassword program uses the driver to log on to the specified database using the encrypted password, so the driver must have been installed with the `pip install teradatasql` command.

The following commands assume that the `TJEncryptPassword.py` program file is located in the current directory. When the driver is installed, the sample programs are placed in the `teradatasql/samples` directory under your Python installation directory. Change your current directory to the `teradatasql/samples` directory under your Python installation directory.

The following example commands illustrate using a 256-bit AES key, and using the HmacSHA256 algorithm.

Platform       | Command
-------------- | ---
macOS or Linux | `python TJEncryptPassword.py AES/CBC/NoPadding 256 HmacSHA256 PassKey.properties EncPass.properties whomooz guest please`
Windows        | `py -3 TJEncryptPassword.py AES/CBC/NoPadding 256 HmacSHA256 PassKey.properties EncPass.properties whomooz guest please`

#### Password Encryption Key File Format

You are not required to use the TJEncryptPassword program to create the files containing the password encryption key and encrypted password. You can develop your own software to create the necessary files, but the files must match the format expected by the driver.

The password encryption key file is a text file in Java Properties file format, using the ISO 8859-1 character encoding.

The file must contain the following string properties:

Property                                          | Description
------------------------------------------------- | ---
`version=1`                                       | The version number must be `1`. This property is required.
`transformation=`*Algorithm*`/`*Mode*`/`*Padding* | Specifies the transformation in the form *Algorithm*`/`*Mode*`/`*Padding*. Supported transformations are listed in a table below. This property is required.
`algorithm=`*Algorithm*                           | This value must correspond to the *Algorithm* portion of the transformation. This property is required.
`match=`*MatchValue*                              | The password encryption key and encrypted password files must contain the same match value. The match values are compared to ensure that the two specified files are related to each other, serving as a "sanity check" to help avoid configuration errors. This property is required.
`key=`*HexDigits*                                 | This value is the password encryption key, encoded as hex digits. This property is required.
`mac=`*MACAlgorithm*                              | Specifies the message authentication code (MAC) algorithm `HmacSHA1` or `HmacSHA256`. Stored Password Protection performs Encrypt-then-MAC for protection from a padding oracle attack. This property is required.
`mackey=`*HexDigits*                              | This value is the MAC key, encoded as hex digits. This property is required.

The TJEncryptPassword program uses a timestamp as a shared match value, but a timestamp is not required. Any shared string can serve as a match value. The timestamp is not related in any way to the encryption of the password, and the timestamp cannot be used to decrypt the password.

#### Encrypted Password File Format

The encrypted password file is a text file in Java Properties file format, using the ISO 8859-1 character encoding.

The file must contain the following string properties:

Property                                          | Description
------------------------------------------------- | ---
`version=1`                                       | The version number must be `1`. This property is required.
`match=`*MatchValue*                              | The password encryption key and encrypted password files must contain the same match value. The match values are compared to ensure that the two specified files are related to each other, serving as a "sanity check" to help avoid configuration errors. This property is required.
`password=`*HexDigits*                            | This value is the encrypted password, encoded as hex digits. This property is required.
`params=`*HexDigits*                              | This value contains the cipher algorithm parameters, if any, encoded as hex digits. Some ciphers need algorithm parameters that cannot be derived from the key, such as an initialization vector. This property is optional, depending on whether the cipher algorithm has associated parameters.
`hash=`*HexDigits*                                | This value is the expected message authentication code (MAC), encoded as hex digits. After encryption, the expected MAC is calculated using the ciphertext, transformation name, and algorithm parameters if any. Before decryption, the driver calculates the MAC using the ciphertext, transformation name, and algorithm parameters if any, and verifies that the calculated MAC matches the expected MAC. If the calculated MAC differs from the expected MAC, then either or both of the files may have been tampered with. This property is required.

While `params` is technically optional, an initialization vector is required by all three block cipher modes `CBC`, `CFB`, and `OFB` that are supported by the driver. ECB (Electronic Codebook) does not require `params`, but ECB is not supported by the driver.

#### Transformation, Key Size, and MAC

A transformation is a string that describes the set of operations to be performed on the given input, to produce transformed output. A transformation specifies the name of a cryptographic algorithm such AES, followed by a feedback mode and padding scheme.

The driver supports the following transformations and key sizes.

Transformation              | Key Size
--------------------------- | ---
`AES/CBC/NoPadding`         | 128
`AES/CBC/NoPadding`         | 192
`AES/CBC/NoPadding`         | 256
`AES/CBC/PKCS5Padding`      | 128
`AES/CBC/PKCS5Padding`      | 192
`AES/CBC/PKCS5Padding`      | 256
`AES/CFB/NoPadding`         | 128
`AES/CFB/NoPadding`         | 192
`AES/CFB/NoPadding`         | 256
`AES/CFB/PKCS5Padding`      | 128
`AES/CFB/PKCS5Padding`      | 192
`AES/CFB/PKCS5Padding`      | 256
`AES/OFB/NoPadding`         | 128
`AES/OFB/NoPadding`         | 192
`AES/OFB/NoPadding`         | 256
`AES/OFB/PKCS5Padding`      | 128
`AES/OFB/PKCS5Padding`      | 192
`AES/OFB/PKCS5Padding`      | 256

Stored Password Protection uses a symmetric encryption algorithm such as AES, in which the same secret key is used for encryption and decryption of the password. Stored Password Protection does not use an asymmetric encryption algorithm such as RSA, with separate public and private keys.

CBC (Cipher Block Chaining) is a block cipher encryption mode. With CBC, each ciphertext block is dependent on all plaintext blocks processed up to that point. CBC is suitable for encrypting data whose total byte count exceeds the algorithm's block size, and is therefore suitable for use with Stored Password Protection.

Stored Password Protection hides the password length in the encrypted password file by extending the length of the UTF8-encoded password with trailing null bytes. The length is extended to the next 512-byte boundary.

* A block cipher with no padding, such as `AES/CBC/NoPadding`, may only be used to encrypt data whose byte count after extension is a multiple of the algorithm's block size. The 512-byte boundary is compatible with many block ciphers. AES, for example, has a block size of 128 bits (16 bytes), and is therefore compatible with the 512-byte boundary.
* A block cipher with padding, such as `AES/CBC/PKCS5Padding`, can be used to encrypt data of any length. However, CBC with padding is vulnerable to a "padding oracle attack", so Stored Password Protection performs Encrypt-then-MAC for protection from a padding oracle attack. MAC algorithms `HmacSHA1` and `HmacSHA256` are supported.
* The driver does not support block ciphers used as byte-oriented ciphers via modes such as `CFB8` or `OFB8`.

The strength of the encryption depends on your choice of cipher algorithm and key size.

* AES uses a 128-bit (16 byte), 192-bit (24 byte), or 256-bit (32 byte) key.

#### Sharing Files with the Teradata JDBC Driver

This driver and the Teradata JDBC Driver can share the files containing the password encryption key and encrypted password, if you use a transformation, key size, and MAC algorithm that is supported by both drivers.

* Recommended choices for compatibility are `AES/CBC/NoPadding` and `HmacSHA256`.
* Use a 256-bit key if your Java environment has the Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files from Oracle.
* Use a 128-bit key if your Java environment does not have the Unlimited Strength Jurisdiction Policy Files.
* Use `HmacSHA1` for compatibility with JDK 1.4.2.

#### File Locations

For the `ENCRYPTED_PASSWORD(` syntax of the driver, each filename must be preceded by the `file:` prefix.
The *PasswordEncryptionKeyFileName* must be separated from the *EncryptedPasswordFileName* by a single comma. The files can be located in the current directory, specified with a relative path, or specified with an absolute path.


Example for files in the current directory:

    ENCRYPTED_PASSWORD(file:JohnDoeKey.properties,file:JohnDoePass.properties)

Example with relative paths:

    ENCRYPTED_PASSWORD(file:../dir1/JohnDoeKey.properties,file:../dir2/JohnDoePass.properties)

Example with absolute paths on Windows:

    ENCRYPTED_PASSWORD(file:c:/dir1/JohnDoeKey.properties,file:c:/dir2/JohnDoePass.properties)

Example with absolute paths on Linux:

    ENCRYPTED_PASSWORD(file:/dir1/JohnDoeKey.properties,file:/dir2/JohnDoePass.properties)

#### Processing Sequence

The two filenames specified for an encrypted password must be accessible to the driver and must conform to the properties file formats described above. The driver raises an exception if the file is not accessible, or the file does not conform to the required file format.

The driver verifies that the match values in the two files are present, and match each other. The driver raises an exception if the match values differ from each other. The match values are compared to ensure that the two specified files are related to each other, serving as a "sanity check" to help avoid configuration errors. The TJEncryptPassword program uses a timestamp as a shared match value, but a timestamp is not required. Any shared string can serve as a match value. The timestamp is not related in any way to the encryption of the password, and the timestamp cannot be used to decrypt the password.

Before decryption, the driver calculates the MAC using the ciphertext, transformation name, and algorithm parameters if any, and verifies that the calculated MAC matches the expected MAC. The driver raises an exception if the calculated MAC differs from the expected MAC, to indicate that either or both of the files may have been tampered with.

Finally, the driver uses the decrypted password to log on to the database.

<a id="LogonMethods"></a>

### Logon Authentication Methods

The following table describes the logon authentication methods selected by the `logmech` connection parameter.

`logmech` | Description | Usage and Requirements
----------|-------------|---
`BEARER`  | OIDC Client Credentials Grant with JWT Bearer Token for client authentication | This method is intended for automated logon by service accounts.<br/>`user`, `password`, `logdata`, and `oauth_scopes` must all be omitted when using this method.<br/>`jws_private_key` is required when using this method. `jws_cert` is also needed for Identity Providers that require an "x5t" header thumbprint.<br/>`oidc_clientid` is commonly used to override the default Client ID when using this method.<br/>`oidc_claim`, `oidc_scope`, `oidc_token`, and `jws_algorithm` are optional parameters when using this method.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`BROWSER` | Browser Authentication, also known as OIDC Authorization Code Flow with Proof Key for Code Exchange (PKCE) | This method is intended for interactive logon by individual users.<br/>`password` and `logdata` must be omitted when using this method.<br/>`user` is optional when using this method. When `user` is specified, it is used as the OIDC login hint and it is included in the OIDC token cache key for token retrieval.<br/>`browser`, `browser_tab_timeout`, `browser_timeout`, `oauth_scopes`, `oidc_claim`, `oidc_clientid`, `oidc_prompt`, `oidc_scope`, and `oidc_token` are optional parameters when using this method.<br/>Browser Authentication is supported for Windows and macOS. Browser Authentication is not supported for other operating systems.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`CODE`    | OIDC Device Code Flow, also known as OIDC Device Authorization Grant | This method is intended for interactive logon by individual users.<br/>`password` and `logdata` must be omitted when using this method.<br/>`user` is optional when using this method. When `user` is specified, it is used as the OIDC login hint and it is included in the OIDC token cache key for token retrieval.<br/>`code_append_file`, `oauth_scopes`, `oidc_claim`, `oidc_clientid`, `oidc_scope`, and `oidc_token` are optional parameters when using this method.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`CRED`    | OIDC Client Credentials Grant with client_secret_post for client authentication | This method is intended for automated logon by service accounts.<br/>`user`, `password`, `oauth_scopes`, `oidc_clientid`, and `oidc_scope` must all be omitted when using this method.<br/>`logdata` must contain the Client Credentials Grant request HTTP POST Form Data encoded as Content-Type application/x-www-form-urlencoded.<br/>`oidc_claim` and `oidc_token` are optional parameters when using this method.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`JWT`     | JSON Web Token (JWT) | `logdata` must contain `token=` followed by the JSON Web Token.<br/>The database user must have the "logon with null password" permission.<br/>Your application must obtain a valid JWT from an Identity Provider. The database must be configured to trust JWTs issued by your Identity Provider. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`KRB5`    | GSS-API Kerberos V5 | Requires a significant number of administration tasks on the machine that is running the driver.<br/>For Kerberos Single Sign On (SSO), the database user must have the "logon with null password" permission.
`LDAP`    | GSS-API Lightweight Directory Access Protocol (LDAP) | Requires a significant administration effort to set up the LDAP environment. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.<br/>Once they are complete, LDAP can be used without any additional work required on the machine that is running the driver.
`ROPC`    | OIDC Resource Owner Password Credentials (ROPC) | This method is intended for interactive logon by individual users.<br/>`logdata` must be omitted when using this method.<br/>`user` and `password` are required when using this method.<br/>`oauth_scopes`, `oidc_claim`, `oidc_clientid`, `oidc_scope`, and `oidc_token` are optional parameters when using this method.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`SECRET`  | OIDC Client Credentials Grant with client_secret_basic for client authentication | This method is intended for automated logon by service accounts.<br/>`user`, `password`, and `oauth_scopes` must all be omitted when using this method.<br/>`logdata` must contain the client secret.<br/>`oidc_clientid` is commonly used to override the default Client ID when using this method.<br/>`oidc_claim`, `oidc_scope`, and `oidc_token` are optional parameters when using this method.<br/>The database user must have the "logon with null password" permission.<br/>The database must be configured with Identity Provider information for Federated Authentication. These tasks are covered in the reference Teradata Vantage&trade; Security Administration.
`TD2`     | GSS-API Teradata Method 2 | Does not require any special setup, and can be used immediately.
`TDNEGO`  | GSS-API Teradata Negotiating Mechanism | Automatically selects an appropriate GSS-API logon authentication method. OIDC methods are not selected.

<a id="ClientAttributes"></a>

### Client Attributes

Client Attributes record a variety of information about the client system and client software in the system tables `DBC.SessionTbl` and `DBC.EventLog`. Client Attributes are intended to be a replacement for the information recorded in the `LogonSource` column of the system tables `DBC.SessionTbl` and `DBC.EventLog`.

The Client Attributes are recorded at session logon time. Subsequently, the system views `DBC.SessionInfoV` and `DBC.LogOnOffV` can be queried to obtain information about the client system and client software on a per-session basis. Client Attribute values may be recorded in the database in either mixed-case or in uppercase, depending on the session character set and other factors. Analysis of recorded Client Attributes must flexibly accommodate either mixed-case or uppercase values.

Warning: The information in this section is subject to change in future releases of the driver. Client Attributes can be "mined" for information about client system demographics; however, any applications that parse Client Attribute values must be changed if Client Attribute formats are changed in the future.

Client Attributes are not intended to be used for workload management. Instead, query bands are intended for workload management. Any use of Client Attributes for workload management may break if Client Attributes are changed, or augmented, in the future.

Client Attribute            | Source   | Description
--------------------------- | -------- | ---
`MechanismName`             | database | The connection's logon mechanism; for example, TD2, LDAP, etc.
`ClientIpAddress`           | database | The client IP address, as determined by the database
`ClientTcpPortNumber`       | database | The connection's client TCP port number, as determined by the database
`ClientIPAddrByClient`      | driver   | The client IP address, as determined by the driver
`ClientPortByClient`        | driver   | The connection's client TCP port number, as determined by the driver
`ClientInterfaceKind`       | driver   | The value `P` to indicate Python, available beginning with Teradata Database 17.20.03.19
`ClientInterfaceVersion`    | driver   | The driver version, available beginning with Teradata Database 17.20.03.19
`ClientProgramName`         | driver   | The client program name, followed by a streamlined call stack
`ClientSystemUserId`        | driver   | The client user name
`ClientOsName`              | driver   | The client operating system name
`ClientProcThreadId`        | driver   | The client process ID
`ClientVmName`              | driver   | Python runtime information
`ClientSecProdGrp`          | driver   | Go crypto library version and native crypto API/library if in use
`ClientCoordName`           | driver   | The proxy server hostname and port number when a proxy server is used for a database connection
`ClientTerminalId`          | driver   | The proxy server hostname and port number when a proxy server is used for an Identity Provider
`ClientSessionDesc`         | driver   | TLS cipher information is available in this column as a list of name=value pairs, each terminated by a semicolon. Individual values can be accessed using the `NVP` system function.
&nbsp; | `C` | Y/N indicates whether the `sslcipher` connection parameter was specified
&nbsp; | `D` | the database TLS cipher
&nbsp; | `I` | the Identity Provider TLS cipher
`ClientTdHostName`          | driver   | The database hostname as specified by the application, without any COP suffix
`ClientCOPSuffixedHostName` | driver   | The COP-suffixed database hostname chosen by the driver
`ServerIPAddrByClient`      | driver   | The database node's IP address, as determined by the driver
`ServerPortByClient`        | driver   | The destination port number of the TCP connection to the database node, as determined by the driver
`ClientConfType`            | driver   | The confidentiality type, as determined by the driver
&nbsp;                      | `V`      | TLS used for encryption, with full certificate verification
&nbsp;                      | `C`      | TLS used for encryption, with Certificate Authority (CA) verification
&nbsp;                      | `R`      | TLS used for encryption, with no certificate verification
&nbsp;                      | `E`      | TLS was not attempted, and TDGSS used for encryption
&nbsp;                      | `U`      | TLS was not attempted, and TDGSS encryption depends on central administration
&nbsp;                      | `F`      | TLS was attempted, but the TLS handshake failed, so this is a fallback to using TDGSS for encryption
&nbsp;                      | `H`      | SSLMODE was set to PREFER, but a non-TLS connection was made, and TDGSS encryption depends on central administration
`ServerConfType`            | database | The confidentiality type, as determined by the database
&nbsp;                      | `T`      | TLS used for encryption
&nbsp;                      | `E`      | TDGSS used for encryption
&nbsp;                      | `U`      | Data transfer is unencrypted
`ClientConfVersion`         | database | The TLS version as determined by the database, if this is an HTTPS/TLS connection
`ClientConfCipherSuite`     | database | The TLS cipher as determined by the database, if this is an HTTPS/TLS connection
`ClientEnvName`             | driver   | The OIDC metadata URL for a connection using an OIDC logon authentication mechanism
`ClientJobId`               | driver   | The OIDC client ID for a connection using an OIDC logon authentication mechanism
`ClientJobName`             | driver   | The OIDC scope for a connection using an OIDC logon authentication mechanism
`ClientJobData`             | driver   | The OIDC login hint for a connection using an OIDC logon authentication mechanism
`ClientUserOperId`          | driver   | The OIDC token kind, OIDC claim name, and claim value for a connection using an OIDC logon authentication mechanism
`ClientWorkload`            | driver   | The scopes for acquired OAuth tokens, separated by vertical bar `\|` characters
`ClientAttributesEx`        | driver   | Additional Client Attributes are available in the `ClientAttributesEx` column as a list of name=value pairs, each terminated by a semicolon. Individual values can be accessed using the `NVP` system function.
&nbsp;                      | `AS`     | the application connection's endpoint session number
&nbsp;                      | `BA`     | Y/N indicator for Browser Authentication
&nbsp;                      | `CCS`    | the client character set
&nbsp;                      | `CERT`   | the database TLS certificate status (see [table below](#CertStatus))
&nbsp;                      | `CF`     | the `connect_function` connection parameter
&nbsp;                      | `CRC`    | the `sslcrc` connection parameter
&nbsp;                      | `CRL`    | Y/N indicator for `sslcrl` connection parameter
&nbsp;                      | `CS`     | the control session's endpoint session number
&nbsp;                      | `DL`     | this connection's database logon sequence number
&nbsp;                      | `DP`     | the `dbs_port` connection parameter
&nbsp;                      | `EL`     | this connection's endpoint logon sequence number
&nbsp;                      | `ENC`    | Y/N indicator for `encryptdata` connection parameter
&nbsp;                      | `ES`     | endpoint session number if connected to an endpoint such as Unity, Session Manager, or Business Continuity Manager; database session number otherwise
&nbsp;                      | `FIPS`   | Y/N indicator for FIPS mode
&nbsp;                      | `GD`     | the Go distribution M ([Microsoft Go](https://github.com/microsoft/go)) or S ([standard Go](https://go.dev/dl/))
&nbsp;                      | `GO`     | the Go version
&nbsp;                      | `GOV`    | the `govern` connection parameter
&nbsp;                      | `HP`     | the `https_port` connection parameter
&nbsp;                      | `HR`     | the `https_retry` connection parameter and number of HTTPS retries
&nbsp;                      | `IDPC`   | the Identity Provider TLS certificate status (see [table below](#CertStatus))
&nbsp;                      | `JH`     | JWT header parameters to identify signature key
&nbsp;                      | `JWS`    | the JSON Web Signature (JWS) algorithm
&nbsp;                      | `LM`     | the logon authentication method
&nbsp;                      | `LOB`    | Y/N indicator for LOB support
&nbsp;                      | `OA`     | the `oauth_level` connection parameter
&nbsp;                      | `OAC`    | sequence of comma-separated OAuth token reuse counts
&nbsp;                      | `OAR`    | sequence of Y/N values to indicate OAuth refresh token availability
&nbsp;                      | `OC`     | OIDC token cache status O (off) M (miss) H (hit) X (expired)
&nbsp;                      | `OCSP`   | Y/N indicator for `sslocsp` connection parameter
&nbsp;                      | `OSL`    | Numeric level corresponding to `oidc_sslmode`
&nbsp;                      | `OSM`    | the `oidc_sslmode` connection parameter
&nbsp;                      | `PART`   | the `partition` connection parameter
&nbsp;                      | `PYTHON` | the Python version
&nbsp;                      | `RP`     | the OIDC redirect port number for Browser Authentication, prefix E indicates ephemeral port
&nbsp;                      | `RT`     | Y/N indicator for OIDC refresh token available
&nbsp;                      | `SC`     | socket connect attempts and failures
&nbsp;                      | `SCS`    | the session character set
&nbsp;                      | `SIP`    | Y/N indicator for StatementInfo parcel support
&nbsp;                      | `SSL`    | Numeric level corresponding to `sslmode`
&nbsp;                      | `SSLM`   | the `sslmode` connection parameter
&nbsp;                      | `SSLP`   | the `sslprotocol` connection parameter
&nbsp;                      | `TC`     | OIDC token reuse count
&nbsp;                      | `TM`     | the transaction mode indicator A (ANSI) or T (TERA)
&nbsp;                      | `TT`     | OIDC token time-to-live in seconds
&nbsp;                      | `TVD`    | the database TLS protocol version
&nbsp;                      | `TVI`    | the Identity Provider TLS protocol version
&nbsp;                      | `TZ`     | the current time zone

<a id="CertStatus"></a>

The `CERT` and `IDPC` attributes indicate the TLS certificate status of an HTTPS/TLS connection. When the attribute indicates the TLS certificate is valid (`V`) or invalid (`I`), then additional TLS certificate status details are provided as a series of comma-separated two-letter codes.

Code | Description
-----|---
`U`  | the TLS certificate status is unavailable
`V`  | the TLS certificate status is valid
`I`  | the TLS certificate status is invalid
`BU` | sslbase64 is unavailable for server certificate verification
`BA` | server certificate was accepted by sslbase64
`BR` | server certificate was rejected by sslbase64
`PU` | sslca PEM file is unavailable for server certificate verification
`PA` | server certificate was verified using sslca PEM file
`PR` | server certificate was rejected using sslca PEM file
`DU` | sslcapath PEM directory is unavailable for server certificate verification
`DA` | server certificate was verified using sslcapath PEM directory
`DR` | server certificate was rejected using sslcapath PEM directory
`TA` | server certificate was verified by the system
`TR` | server certificate was rejected by the system
`CY` | server certificate passed VERIFY-CA check
`CN` | server certificate failed VERIFY-CA check
`HU` | server hostname is unavailable for server certificate matching, because database IP address was specified
`HY` | server hostname matches server certificate
`HN` | server hostname does not match server certificate
`RU` | resolved server hostname is unavailable for server certificate matching, because database IP address was specified
`RY` | resolved server hostname matches server certificate
`RN` | resolved server hostname does not match server certificate
`IY` | IP address matches server certificate
`IN` | IP address does not match server certificate
`FY` | server certificate passed VERIFY-FULL check
`FN` | server certificate failed VERIFY-FULL check
`SU` | certificate revocation check status is unavailable
`SG` | certificate revocation check status is good
`SR` | certificate revocation check status is revoked

#### LogonSource Column

The `LogonSource` column is obsolete and has been superseded by Client Attributes. The `LogonSource` column may be deprecated and subsequently removed in future releases of the database.

When the driver establishes a connection to the database, the driver composes a string value that is stored in the `LogonSource` column of the system tables `DBC.SessionTbl` and `DBC.EventLog`. The `LogonSource` column is included in system views such as `DBC.SessionInfoV` and `DBC.LogOnOffV`. All `LogonSource` values are recorded in the database in uppercase.

The driver follows the format documented in the Teradata Data Dictionary, section "System Views Columns Reference", for network-attached `LogonSource` values. Network-attached `LogonSource` values have eight fields, separated by whitespace. The database composes fields 1 through 3, and the driver composes fields 4 through 8.

Field | Source   | Description
----- | -------- | ---
1     | database | The string `(TCP/IP)` to indicate the connection type
2     | database | The connection's client TCP port number, in hexadecimal
3     | database | The client IP address, as determined by the database
4     | driver   | The database hostname as specified by the application, without any COP suffix
5     | driver   | The client process ID
6     | driver   | The client user name
7     | driver   | The client program name
8     | driver   | The string `01 LSS` to indicate the `LogonSource` string version `01`

<a id="UserStartup"></a>

### User STARTUP SQL Request

`CREATE USER` and `MODIFY USER` commands provide `STARTUP` clauses for specifying SQL commands to establish initial session settings. The following table lists several of the SQL commands that may be used to establish initial session settings.

Category                 | SQL command
------------------------ | ---
Diagnostic settings      | `DIAGNOSTIC` ... `FOR SESSION`
Session query band       | `SET QUERY_BAND` ... `FOR SESSION`
Unicode Pass Through     | `SET SESSION CHARACTER SET UNICODE PASS THROUGH ON`
Transaction isolation    | `SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL`
Collation sequence       | `SET SESSION COLLATION`
Temporal qualifier       | `SET SESSION CURRENT VALIDTIME AND CURRENT TRANSACTIONTIME`
Date format              | `SET SESSION DATEFORM`
Function tracing         | `SET SESSION FUNCTION TRACE`
Session time zone        | `SET TIME ZONE`

For example, the following command sets a `STARTUP` SQL request for user `susan` to establish read-uncommitted transaction isolation after logon.

    MODIFY USER susan AS STARTUP='SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL RU'

The driver's `runstartup` connection parameter must be `true` to execute the user's `STARTUP` SQL request after logon. The default for `runstartup` is `false`. If the `runstartup` connection parameter is omitted or `false`, then the user's `STARTUP` SQL request will not be executed.

<a id="SessionReconnect"></a>

### Session Reconnect

Your application's connection can be disconnected from the database session in various ways outside the control of the driver, such as
* a network cable being unplugged
* a network communication failure
* an administrator terminating the session with the Monitor partition command `Abort Session`
* an administrator terminating the session with the Gateway command `Kill Session`
* a database restart

When Session Reconnect is enabled, the driver will attempt to reconnect the connection to the database session after a communication failure.

Session Reconnect is enabled when one or more of the following conditions are satisfied:
* Recoverable Network Protocol is in effect
* and/or connection parameter `reconnect_count` is specified (if omitted, the default is 11 attempts)
* and/or connection parameter `reconnect_interval` is specified (if omitted, the default is 30 seconds)

| Maximum possible elapsed time for reconnect attempts
| ---
| (*ReconnectCount* - 1) &times; *ReconnectInterval*

Recoverable Network Protocol (RNP) and Redrive are enabled through a combination of database and driver connection parameters; specifically, the database `dbscontrol` fields `RedriveProtection` (67), `RedriveDefaultParticipation` (68), and `DisableRecoverableNetProtocol` (77), and the driver connection parameter `redrive` with level 2 or higher.
* When RNP and Redrive are enabled, then Session Reconnect works for a variety of failure events, including transient network failures.
* Without Recoverable Network Protocol, Session Reconnect only supports reconnection after a database restart; it does not support reconnection after other events, such as transient network failures.

Session Reconnect | RNP and Redrive | Communication failure handling
----------------- | --------------- | ---
Disabled          | Disabled        | The operation in progress fails, the driver closes the connection and returns an error to the application.
Enabled           | Disabled        | The operation in progress fails, the driver attempts to reconnect and returns an error to the application.<br/>If the reconnect is unsuccessful, the driver closes the connection.<br/>If the reconnect is successful, the database discards a significant part of the session state:<br/>&bull; The current transaction is rolled back.<br/>&bull; All open result sets are discarded.<br/>&bull; All volatile tables are discarded.<br/>&bull; All materialized global temp tables are discarded.<br/>The application must be prepared to accommodate the possible loss of session state at any point in time.
Enabled           | Enabled         | The operation in progress fails and the driver attempts to reconnect.<br/>If the reconnect is unsuccessful, the driver closes the connection.<br/>If the reconnect is successful, the operation is redriven automatically, the session's state is preserved, and no error is returned to the application.

Reconnect is never attempted if a communication failure occurs while the application is closing the connection.

The database enforces a limited time period for reconnecting to a session after a database restart. The amount of time is set using the database administrator program `gtwcontrol`. The standard value is 20 minutes. The database will reject all reconnect attempts after the time period expires.

<a id="TransactionMode"></a>

### Transaction Mode

The `tmode` connection parameter enables an application to specify the transaction mode for the connection.

`tmode`   | Description
--------- | ---
`ANSI`    | Provides American National Standards Institute (ANSI) transaction semantics. This mode is recommended.
`TERA`    | Provides legacy Teradata transaction semantics. This mode is only recommended for legacy applications that require Teradata transaction semantics.
`DEFAULT` | Provides the default transaction mode configured for the database, which may be either ANSI or TERA mode. This is the default when the `tmode` connection parameter is omitted.

While ANSI mode is generally recommended, please note that every application is different, and some applications may need to use TERA mode. The following differences between ANSI and TERA mode might affect a typical user or application:
1. Silent truncation of inserted data occurs in TERA mode, but not ANSI mode. In ANSI mode, the database returns an error instead of truncating data.
2. Tables created in ANSI mode are `MULTISET` by default. Tables created in TERA mode are `SET` tables by default.
3. For tables created in ANSI mode, character columns are `CASESPECIFIC` by default. For tables created in TERA mode, character columns are `NOT CASESPECIFIC` by default.
4. In ANSI mode, character literals are `CASESPECIFIC`. In TERA mode, character literals are `NOT CASESPECIFIC`.

The last two behavior differences, taken together, may cause character data comparisons (such as in `WHERE` clause conditions) to be case-insensitive in TERA mode, but case-sensitive in ANSI mode. This, in turn, can produce different query results in ANSI mode versus TERA mode. Comparing two `NOT CASESPECIFIC` expressions is case-insensitive regardless of mode, and comparing a `CASESPECIFIC` expression to another expression of any kind is case-sensitive regardless of mode. You may explicitly `CAST` an expression to be `CASESPECIFIC` or `NOT CASESPECIFIC` to obtain the character data comparison required by your application.

The Teradata Reference / *SQL Request and Transaction Processing* recommends that ANSI mode be used for all new applications. The primary benefit of using ANSI mode is that inadvertent data truncation is avoided. In contrast, when using TERA mode, silent data truncation can occur when data is inserted, because silent data truncation is a feature of TERA mode.

A drawback of using ANSI mode is that you can only call stored procedures that were created using ANSI mode, and you cannot call stored procedures that were created using TERA mode. It may not be possible to switch over to ANSI mode exclusively, because you may have some legacy applications that require TERA mode to work properly. You can work around this drawback by creating your stored procedures twice, in two different users/databases, once using ANSI mode, and once using TERA mode.

Refer to the Teradata Reference / *SQL Request and Transaction Processing* for complete information regarding the differences between ANSI and TERA transaction modes.

<a id="AutoCommit"></a>

### Auto-Commit

The driver provides auto-commit on and off functionality for both ANSI and TERA mode.

When a connection is first established, it begins with the default auto-commit setting, which is on. When auto-commit is on, the driver is solely responsible for managing transactions, and the driver commits each SQL request that is successfully executed. An application should not execute any transaction management SQL commands when auto-commit is on. An application should not call the `commit` method or the `rollback` method when auto-commit is on.

An application can manage transactions itself by setting the connection's `.autocommit` attribute to `False` to turn off auto-commit.

    con.autocommit = False

When auto-commit is off, the driver leaves the current transaction open after each SQL request is executed, and the application is responsible for committing or rolling back the transaction by calling the `commit` or the `rollback` method, respectively.

Auto-commit remains turned off until the application turns it back on by setting the connection's `.autocommit` attribute to `True`.

    con.autocommit = True

Best practices recommend that an application avoid executing database-vendor-specific transaction management commands such as `BT`, `ET`, `ABORT`, `COMMIT`, or `ROLLBACK`, because such commands differ from one vendor to another. (They even differ between Teradata's two modes ANSI and TERA.) Instead, best practices recommend that an application only call the standard methods `commit` and `rollback` for transaction management.
1. When auto-commit is on in ANSI mode, the driver automatically executes `COMMIT` after every successful SQL request.
2. When auto-commit is off in ANSI mode, the driver does not automatically execute `COMMIT`. When the application calls the `commit` method, then the driver executes `COMMIT`.
3. When auto-commit is on in TERA mode, the driver does not execute `BT` or `ET`, unless the application explicitly executes `BT` or `ET` commands itself, which is not recommended.
4. When auto-commit is off in TERA mode, the driver executes `BT` before submitting the application's first SQL request of a new transaction. When the application calls the `commit` method, then the driver executes `ET` until the transaction is complete.

As part of the wire protocol between the database and Teradata client interface software (such as this driver), each message transmitted from the database to the client has a bit designated to indicate whether the session has a transaction in progress or not. Thus, the client interface software is kept informed as to whether the session has a transaction in progress or not.

In TERA mode with auto-commit off, when the application uses the driver to execute a SQL request, if the session does not have a transaction in progress, then the driver automatically executes `BT` before executing the application's SQL request. Subsequently, in TERA mode with auto-commit off, when the application uses the driver to execute another SQL request, and the session already has a transaction in progress, then the driver has no need to execute `BT` before executing the application's SQL request.

In TERA mode, `BT` and `ET` pairs can be nested, and the database keeps track of the nesting level. The outermost `BT`/`ET` pair defines the transaction scope; inner `BT`/`ET` pairs have no effect on the transaction because the database does not provide actual transaction nesting. To commit the transaction, `ET` commands must be repeatedly executed until the nesting is unwound. The Teradata wire protocol bit (mentioned earlier) indicates when the nesting is unwound and the transaction is complete. When the application calls the `commit` method in TERA mode, the driver repeatedly executes `ET` commands until the nesting is unwound and the transaction is complete.

In rare cases, an application may not follow best practices and may explicitly execute transaction management commands. Such an application must turn off auto-commit before executing transaction management commands such as `BT`, `ET`, `ABORT`, `COMMIT`, or `ROLLBACK`. The application is responsible for executing the appropriate commands for the transaction mode in effect. TERA mode commands are `BT`, `ET`, and `ABORT`. ANSI mode commands are `COMMIT` and `ROLLBACK`. An application must take special care when opening a transaction in TERA mode with auto-commit off. In TERA mode with auto-commit off, when the application executes a SQL request, if the session does not have a transaction in progress, then the driver automatically executes `BT` before executing the application's SQL request. Therefore, the application should not begin a transaction by executing `BT`.

    # TERA mode example showing undesirable BT/ET nesting
    con.autocommit = False
    cur.execute("BT") # BT automatically executed by the driver before this, and produces a nested BT
    cur.execute("insert into mytable1 values(1, 2)")
    cur.execute("insert into mytable2 values(3, 4)")
    cur.execute("ET") # unwind nesting
    cur.execute("ET") # complete transaction

    # TERA mode example showing how to avoid BT/ET nesting
    con.autocommit = False
    cur.execute("insert into mytable1 values(1, 2)") # BT automatically executed by the driver before this
    cur.execute("insert into mytable2 values(3, 4)")
    cur.execute("ET") # complete transaction

Please note that neither previous example shows best practices. Best practices recommend that an application only call the standard methods `commit` and `rollback` for transaction management.

    # Example showing best practice
    con.autocommit = False
    cur.execute("insert into mytable1 values(1, 2)")
    cur.execute("insert into mytable2 values(3, 4)")
    con.commit()

<a id="DataTypes"></a>

### Data Types

The table below lists the database data types supported by the driver, and indicates the corresponding Python data type returned in result set rows.

Database data type                 | Result set Python data type       | With `teradata_values` as `false`
---------------------------------- | --------------------------------- | ---
`BIGINT`                           | `int`                             |
`BLOB`                             | `bytes`                           |
`BYTE`                             | `bytes`                           |
`BYTEINT`                          | `int`                             |
`CHAR`                             | `str`                             |
`CLOB`                             | `str`                             |
`DATE`                             | `datetime.date`                   | `str`
`DECIMAL`                          | `decimal.Decimal`                 | `str`
`FLOAT`                            | `float`                           |
`INTEGER`                          | `int`                             |
`INTERVAL YEAR`                    | `str`                             |
`INTERVAL YEAR TO MONTH`           | `str`                             |
`INTERVAL MONTH`                   | `str`                             |
`INTERVAL DAY`                     | `str`                             |
`INTERVAL DAY TO HOUR`             | `str`                             |
`INTERVAL DAY TO MINUTE`           | `str`                             |
`INTERVAL DAY TO SECOND`           | `str`                             |
`INTERVAL HOUR`                    | `str`                             |
`INTERVAL HOUR TO MINUTE`          | `str`                             |
`INTERVAL HOUR TO SECOND`          | `str`                             |
`INTERVAL MINUTE`                  | `str`                             |
`INTERVAL MINUTE TO SECOND`        | `str`                             |
`INTERVAL SECOND`                  | `str`                             |
`NUMBER`                           | `decimal.Decimal`                 | `str`
`PERIOD(DATE)`                     | `str`                             |
`PERIOD(TIME)`                     | `str`                             |
`PERIOD(TIME WITH TIME ZONE)`      | `str`                             |
`PERIOD(TIMESTAMP)`                | `str`                             |
`PERIOD(TIMESTAMP WITH TIME ZONE)` | `str`                             |
`SMALLINT`                         | `int`                             |
`TIME`                             | `datetime.time`                   | `str`
`TIME WITH TIME ZONE`              | `datetime.time` with `tzinfo`     | `str`
`TIMESTAMP`                        | `datetime.datetime`               | `str`
`TIMESTAMP WITH TIME ZONE`         | `datetime.datetime` with `tzinfo` | `str`
`VARBYTE`                          | `bytes`                           |
`VARCHAR`                          | `str`                             |
`XML`                              | `str`                             |

The table below lists the parameterized SQL bind-value Python data types supported by the driver, and indicates the corresponding database data type transmitted to the server.

Bind-value Python data type       | Database data type
--------------------------------- | ---
`bytes`                           | `VARBYTE`
`datetime.date`                   | `DATE`
`datetime.datetime`               | `TIMESTAMP`
`datetime.datetime` with `tzinfo` | `TIMESTAMP WITH TIME ZONE`
`datetime.time`                   | `TIME`
`datetime.time` with `tzinfo`     | `TIME WITH TIME ZONE`
`datetime.timedelta`              | `VARCHAR` format compatible with `INTERVAL DAY TO SECOND`
`decimal.Decimal`                 | `NUMBER`
`float`                           | `FLOAT`
`int`                             | `BIGINT`
`numpy.ndarray` (one-dimensional) | `VARCHAR` format compatible with `VECTOR`
`str`                             | `VARCHAR`

Transforms are used for SQL `ARRAY` data values, and they can be transferred to and from the database as `VARCHAR` values.

Transforms are used for structured UDT data values, and they can be transferred to and from the database as `VARCHAR` values.

<a id="NullValues"></a>

### Null Values

SQL `NULL` values received from the database are returned in result set rows as Python `None` values.

A Python `None` value bound to a question-mark parameter marker is transmitted to the database as a `NULL` `VARCHAR` value.

The database does not provide automatic or implicit conversion of a `NULL` `VARCHAR` value to a different destination data type.
* For `NULL` column values in a batch, the driver will automatically convert the `NULL` values to match the data type of the non-`NULL` values in the same column.
* For solitary `NULL` values, your application may need to explicitly specify the data type with the `teradata_parameter` escape function, in order to avoid database error 3532 for non-permitted data type conversion.

Given a table with a destination column of `BYTE(4)`, the database would reject the following SQL with database error 3532 "Conversion between BYTE data and other types is illegal."

    cur.execute("update mytable set bytecolumn = ?", [None]) # fails with database error 3532

To avoid database error 3532 in this situation, your application must use the the `teradata_parameter` escape function to specify the data type for the question-mark parameter marker.

    cur.execute("{fn teradata_parameter(1, BYTE(4))}update mytable set bytecolumn = ?", [None])

<a id="CharacterExportWidth"></a>

### Character Export Width

The driver always uses the UTF8 session character set, and the `charset` connection parameter is not supported. Be aware of the database's *Character Export Width* behavior that adds trailing space padding to fixed-width `CHAR` data type result set column values when using the UTF8 session character set.

The database `CHAR(`_n_`)` data type is a fixed-width data type (holding _n_ characters), and the database reserves a fixed number of bytes for the `CHAR(`_n_`)` data type in response spools and in network message traffic.

UTF8 is a variable-width character encoding scheme that requires a varying number of bytes for each character. When the UTF8 session character set is used, the database reserves the maximum number of bytes that the `CHAR(`_n_`)` data type could occupy in response spools and in network message traffic. When the UTF8 session character set is used, the database appends padding characters to the tail end of `CHAR(`_n_`)` values smaller than the reserved maximum size, so that the `CHAR(`_n_`)` values all occupy the same fixed number of bytes in response spools and in network message traffic.

Work around this drawback by using `CAST` or `TRIM` in SQL `SELECT` statements, or in views, to convert fixed-width `CHAR` data types to `VARCHAR`.

Given a table with fixed-width `CHAR` columns:

`CREATE TABLE MyTable (c1 CHAR(10), c2 CHAR(10))`

Original query that produces trailing space padding:

`SELECT c1, c2 FROM MyTable`

Modified query with either `CAST` or `TRIM` to avoid trailing space padding:

`SELECT CAST(c1 AS VARCHAR(10)), TRIM(TRAILING FROM c2) FROM MyTable`

Or wrap query in a view with `CAST` or `TRIM` to avoid trailing space padding:

`CREATE VIEW MyView (c1, c2) AS SELECT CAST(c1 AS VARCHAR(10)), TRIM(TRAILING FROM c2) FROM MyTable`

`SELECT c1, c2 FROM MyView`

This technique is also demonstrated in sample program `CharPadding.py`.

<a id="ModuleConstructors"></a>

### Module Constructors

`teradatasql.connect(` *JSONConnectionString* `,` *Parameters...* `)`

Creates a connection to the database and returns a Connection object.

The first parameter is an optional JSON string that defaults to `None`. The second and subsequent arguments are optional `kwargs`. Specify connection parameters as a JSON string, as `kwargs`, or a combination of the two.

When a combination of parameters are specified, connection parameters specified as `kwargs` take precedence over same-named connection parameters specified in the JSON string.

---

`teradatasql.factory(` *JSONConnectionString* `,` *Parameters...* `)`

Creates and returns a connection factory function. Subsequently call the connection factory function with no arguments to obtain a Connection object.

The first parameter is an optional JSON string that defaults to `None`. The second and subsequent arguments are optional `kwargs`. Specify connection parameters as a JSON string, as `kwargs`, or a combination of the two.

When a combination of parameters are specified, connection parameters specified as `kwargs` take precedence over same-named connection parameters specified in the JSON string.

---

`teradatasql.Date(` *Year* `,` *Month* `,` *Day* `)`

Creates and returns a `datetime.date` value.

---

`teradatasql.DateFromTicks(` *Seconds* `)`

Creates and returns a `datetime.date` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

---

`teradatasql.Time(` *Hour* `,` *Minute* `,` *Second* `)`

Creates and returns a `datetime.time` value.

---

`teradatasql.TimeFromTicks(` *Seconds* `)`

Creates and returns a `datetime.time` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

---

`teradatasql.Timestamp(` *Year* `,` *Month* `,` *Day* `,` *Hour* `,` *Minute* `,` *Second* `)`

Creates and returns a `datetime.datetime` value.

---

`teradatasql.TimestampFromTicks(` *Seconds* `)`

Creates and returns a `datetime.datetime` value corresponding to the specified number of seconds after 1970-01-01 00:00:00.

<a id="ModuleFunctions"></a>

### Module Functions

`teradatasql.main(` *SequenceOfStrings* `)`

Provides programmatic access to the command line interface.

<a id="ModuleGlobals"></a>

### Module Globals

`teradatasql.__version__`

The package version number.

---

`teradatasql.apilevel`

String constant `"2.0"` indicating that the driver implements the [PEP-249 Python Database API Specification 2.0](https://www.python.org/dev/peps/pep-0249/).

---

`teradatasql.threadsafety`

Integer constant `2` indicating that threads may share this module, and threads may share connections, but threads must not share cursors.

---

`teradatasql.paramstyle`

String constant `"qmark"` indicating that prepared SQL requests use question-mark parameter markers.

<a id="ModuleExceptions"></a>

### Module Exceptions

`teradatasql.Error` is the base class for other exceptions.
* `teradatasql.InterfaceError` is raised for errors related to the driver. Not supported yet.
* `teradatasql.DatabaseError` is raised for errors related to the database.
  * `teradatasql.DataError` is raised for data value errors such as division by zero. Not supported yet.
  * `teradatasql.IntegrityError` is raised for referential integrity violations. Not supported yet.
  * `teradatasql.OperationalError` is raised for errors related to the database's operation.
  * `teradatasql.ProgrammingError` is raised for SQL object existence errors and SQL syntax errors. Not supported yet.

<a id="ConnectionAttributes"></a>

### Connection Attributes

`.autocommit`

Read/write `bool` attribute for the connection's auto-commit setting. Defaults to `True` meaning auto-commit is turned on.

<a id="ConnectionMethods"></a>

### Connection Methods

`.cancel()`

Attempts to cancel the currently executing SQL request, if one is currently executing. Does nothing if called when no SQL request is executing.

This method must be called from a thread other than the thread which is blocked while executing the SQL request.

---

`.close()`

Closes the Connection.

---

`.commit()`

Commits the current transaction.

---

`.cursor()`

Creates and returns a new Cursor object for the Connection.

---

`.nativeSQL(` *SQLRequest* `)`

Returns the specified SQL request text after conversion to native Teradata SQL. Equivalent to the JDBC API `Connection.nativeSQL` method.

The `{fn teradata_nativesql}` escape clause is automatically prepended to the SQL request before processing.

---

`.rollback()`

Rolls back the current transaction.

<a id="CursorAttributes"></a>

### Cursor Attributes

`.activityname`

Read-only `str` attribute indicating the activity name of the current SQL statement, such as `Select`, `Insert`, or `Update`.

The value `unknown` indicates the database provided an activity type code that the driver does not recognize.

---

`.activitytype`

Read-only `int` attribute indicating the activity type code of the current SQL statement, such as `1` for Select, `2` for Insert, or `3` for Update.

Activity type codes are documented in the [Activity Type section of the Teradata Call-Level Interface Version 2 Reference](https://docs.teradata.com/r/Enterprise_IntelliFlex_Lake_VMware/Teradata-Call-Level-Interface-Version-2-Reference-for-Workstation-Attached-Systems-17.20/Parcels/Common-Parcel-Fields/Activity-Type).

---

`.arraysize`

Read/write `int` attribute specifying the number of rows to fetch at a time with the `.fetchmany()` method. Defaults to `1` meaning fetch a single row at a time.

---

`.columntypename`

Read-only attribute consisting of a sequence of result set column type names, available after a SQL request is executed.

---

`.connection`

Read-only attribute indicating the Cursor's parent Connection object.

---

`.description`

Read-only attribute consisting of a sequence of seven-item sequences that each describe a result set column, available after a SQL request is executed.
* `.description[`*Column*`][0]` provides the column name.
* `.description[`*Column*`][1]` provides the column type code as an object comparable to one of the Type Objects listed below.
* `.description[`*Column*`][2]` provides the column display size in characters. Not implemented yet.
* `.description[`*Column*`][3]` provides the column size in bytes.
* `.description[`*Column*`][4]` provides the column precision if applicable, or `None` otherwise.
* `.description[`*Column*`][5]` provides the column scale if applicable, or `None` otherwise.
* `.description[`*Column*`][6]` provides the column nullability as `True` or `False`.

---

`.rowcount`

Read-only `int` attribute indicating the number of rows returned from, or affected by, the current SQL statement.

<a id="CursorMethods"></a>

### Cursor Methods

`.callproc(` *ProcedureName* `,` *OptionalSequenceOfParameterValues* `)`

Calls the stored procedure specified by *ProcedureName*.
Provide the second argument as a sequence of `IN` and `INOUT` parameter values to bind the values to question-mark parameter markers in the SQL request.
Specifying parameter values as a mapping is not supported.
Returns a result set consisting of the `INOUT` parameter output values, if any, followed by any dynamic result sets.

`OUT` parameters are not supported by this method. Use `.execute` to call a stored procedure with `OUT` parameters.

---

`.close()`

Closes the Cursor.

---

`.execute(` *SQLRequest* `,` *OptionalSequenceOfParameterValues* `, ignoreErrors=` *OptionalSequenceOfIgnoredErrorCodes* `)`

Executes the SQL request.
If a sequence of parameter values is provided as the second argument, the values will be bound to question-mark parameter markers in the SQL request.
Parameter values may also be specified as a pandas DataFrame.
Specifying parameter values as a mapping is not supported.

The `ignoreErrors` parameter is optional. The ignored error codes must be specified as a sequence of integers.

---

`.executemany(` *SQLRequest* `,` *SequenceOfSequencesOfParameterValues* `, ignoreErrors=` *OptionalSequenceOfIgnoredErrorCodes* `)`

Executes the SQL request as an iterated SQL request for the batch of parameter values.
The batch of parameter values must be specified as a sequence of sequences.
Parameter values may also be specified as a pandas DataFrame.
Specifying parameter values as a mapping is not supported.

The `ignoreErrors` parameter is optional. The ignored error codes must be specified as a sequence of integers.

---

`.fetchall()`

Fetches all remaining rows of the current result set.
Returns a sequence of sequences of column values.

---

`.fetchmany(` *OptionalRowCount* `)`

Fetches the next series of rows of the current result set.
The argument specifies the number of rows to fetch. If no argument is provided, then the Cursor's `.arraysize` attribute will determine the number of rows to fetch.
Returns a sequence of sequences of column values, or an empty sequence to indicate that all rows have been fetched.

---

`.fetchone()`

Fetches the next row of the current result set.
Returns a sequence of column values, or `None` to indicate that all rows have been fetched.

---

`.nextset()`

Advances to the next result set.
Returns `True` if another result set is available, or `None` to indicate that all result sets have been fetched.

---

`.setinputsizes(` *SequenceOfTypesOrSizes* `)`

Has no effect.

---

`.setoutputsize(` *Size* `,` *OptionalColumnIndex* `)`

Has no effect.

<a id="TypeObjects"></a>

### Type Objects

`teradatasql.BINARY`

Identifies a SQL `BLOB`, `BYTE`, or `VARBYTE` column as a binary data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.BINARY`

---

`teradatasql.DATETIME`

Identifies a SQL `DATE`, `TIME`, `TIME WITH TIME ZONE`, `TIMESTAMP`, or `TIMESTAMP WITH TIME ZONE` column as a date/time data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.DATETIME`

---

`teradatasql.NUMBER`

Identifies a SQL `BIGINT`, `BYTEINT`, `DECIMAL`, `FLOAT`, `INTEGER`, `NUMBER`, or `SMALLINT` column as a numeric data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.NUMBER`

---

`teradatasql.STRING`

Identifies a SQL `CHAR`, `CLOB`, `INTERVAL`, `PERIOD`, or `VARCHAR` column as a character data type when compared with the Cursor's description attribute.

`.description[`*Column*`][1] == teradatasql.STRING`

<a id="EscapeSyntax"></a>

### Escape Syntax

The driver accepts most of the JDBC escape clauses offered by the Teradata JDBC Driver.

#### Date and Time Literals

Date and time literal escape clauses are replaced by the corresponding SQL literal before the SQL request text is transmitted to the database.

Literal Type | Format
------------ | ------
Date         | `{d '`*yyyy-mm-dd*`'}`
Time         | `{t '`*hh:mm:ss*`'}`
Timestamp    | `{ts '`*yyyy-mm-dd hh:mm:ss*`'}`
Timestamp    | `{ts '`*yyyy-mm-dd hh:mm:ss.f*`'}`

For timestamp literal escape clauses, the decimal point and fractional digits may be omitted, or 1 to 6 fractional digits *f* may be specified after a decimal point.

#### Scalar Functions

Scalar function escape clauses are replaced by the corresponding SQL expression before the SQL request text is transmitted to the database.

<a id="esc_numeric"></a>

Numeric Function                       | Returns
-------------------------------------- | ---
`{fn ABS(`*number*`)}`                 | Absolute value of *number*
`{fn ACOS(`*float*`)}`                 | Arccosine, in radians, of *float*
`{fn ASIN(`*float*`)}`                 | Arcsine, in radians, of *float*
`{fn ATAN(`*float*`)}`                 | Arctangent, in radians, of *float*
`{fn ATAN2(`*y*`,`*x*`)}`              | Arctangent, in radians, of *y* / *x*
`{fn CEILING(`*number*`)}`             | Smallest integer greater than or equal to *number*
`{fn COS(`*float*`)}`                  | Cosine of *float* radians
`{fn COT(`*float*`)}`                  | Cotangent of *float* radians
`{fn DEGREES(`*number*`)}`             | Degrees in *number* radians
`{fn EXP(`*float*`)}`                  | *e* raised to the power of *float*
`{fn FLOOR(`*number*`)}`               | Largest integer less than or equal to *number*
`{fn LOG(`*float*`)}`                  | Natural (base *e*) logarithm of *float*
`{fn LOG10(`*float*`)}`                | Base 10 logarithm of *float*
`{fn MOD(`*integer1*`,`*integer2*`)}`  | Remainder for *integer1* / *integer2*
`{fn PI()}`                            | The constant pi, approximately equal to 3.14159...
`{fn POWER(`*number*`,`*integer*`)}`   | *number* raised to *integer* power
`{fn RADIANS(`*number*`)}`             | Radians in *number* degrees
`{fn RAND(`*seed*`)}`                  | A random float value such that 0 &le; value < 1, and *seed* is ignored
`{fn ROUND(`*number*`,`*places*`)}`    | *number* rounded to *places*
`{fn SIGN(`*number*`)}`                | -1 if *number* is negative; 0 if *number* is 0; 1 if *number* is positive
`{fn SIN(`*float*`)}`                  | Sine of *float* radians
`{fn SQRT(`*float*`)}`                 | Square root of *float*
`{fn TAN(`*float*`)}`                  | Tangent of *float* radians
`{fn TRUNCATE(`*number*`,`*places*`)}` | *number* truncated to *places*

<a id="esc_string"></a>

String Function                                                | Returns
-------------------------------------------------------------- | ---
`{fn ASCII(`*string*`)}`                                       | ASCII code of the first character in *string*
`{fn CHAR(`*code*`)}`                                          | Character with ASCII *code*
`{fn CHAR_LENGTH(`*string*`)}`                                 | Length in characters of *string*
`{fn CHARACTER_LENGTH(`*string*`)}`                            | Length in characters of *string*
`{fn CONCAT(`*string1*`,`*string2*`)}`                         | String formed by concatenating *string1* and *string2*
`{fn DIFFERENCE(`*string1*`,`*string2*`)}`                     | A number from 0 to 4 that indicates the phonetic similarity of *string1* and *string2* based on their Soundex codes, such that a larger return value indicates greater phonetic similarity; 0 indicates no similarity, 4 indicates strong similarity
`{fn INSERT(`*string1*`,`*position*`,`*length*`,`*string2*`)}` | String formed by replacing the *length*-character segment of *string1* at *position* with *string2*, available beginning with Teradata Database 15.0
`{fn LCASE(`*string*`)}`                                       | String formed by replacing all uppercase characters in *string* with their lowercase equivalents
`{fn LEFT(`*string*`,`*count*`)}`                              | Leftmost *count* characters of *string*
`{fn LENGTH(`*string*`)}`                                      | Length in characters of *string*
`{fn LOCATE(`*string1*`,`*string2*`)}`                         | Position in *string2* of the first occurrence of *string1*, or 0 if *string2* does not contain *string1*
`{fn LTRIM(`*string*`)}`                                       | String formed by removing leading spaces from *string*
`{fn OCTET_LENGTH(`*string*`)}`                                | Length in octets (bytes) of *string*
`{fn POSITION(`*string1*` IN `*string2*`)}`                    | Position in *string2* of the first occurrence of *string1*, or 0 if *string2* does not contain *string1*
`{fn REPEAT(`*string*`,`*count*`)}`                            | String formed by repeating *string* *count* times, available beginning with Teradata Database 15.0
`{fn REPLACE(`*string1*`,`*string2*`,`*string3*`)}`            | String formed by replacing all occurrences of *string2* in *string1* with *string3*
`{fn RIGHT(`*string*`,`*count*`)}`                             | Rightmost *count* characters of *string*, available beginning with Teradata Database 15.0
`{fn RTRIM(`*string*`)}`                                       | String formed by removing trailing spaces from *string*
`{fn SOUNDEX(`*string*`)}`                                     | Soundex code for *string*
`{fn SPACE(`*count*`)}`                                        | String consisting of *count* spaces
`{fn SUBSTRING(`*string*`,`*position*`,`*length*`)}`           | The *length*-character segment of *string* at *position*
`{fn UCASE(`*string*`)}`                                       | String formed by replacing all lowercase characters in *string* with their uppercase equivalents

<a id="esc_system"></a>

System Function                         | Returns
--------------------------------------- | ---
`{fn DATABASE()}`                       | Current default database name
`{fn IFNULL(`*expression*`,`*value*`)}` | *expression* if *expression* is not NULL, or *value* if *expression* is NULL
`{fn USER()}`                           | Logon user name, which may differ from the current authorized user name after `SET QUERY_BAND` sets a proxy user

<a id="esc_timedate"></a>

Time/Date Function                                                 | Returns
------------------------------------------------------------------ | ---
`{fn CURDATE()}`                                                   | Current date
`{fn CURRENT_DATE()}`                                              | Current date
`{fn CURRENT_TIME()}`                                              | Current time
`{fn CURRENT_TIMESTAMP()}`                                         | Current date and time
`{fn CURTIME()}`                                                   | Current time
`{fn DAYOFMONTH(`*date*`)}`                                        | Integer from 1 to 31 indicating the day of month in *date*
`{fn EXTRACT(YEAR FROM `*value*`)}`                                | The year component of the date and/or time *value*
`{fn EXTRACT(MONTH FROM `*value*`)}`                               | The month component of the date and/or time *value*
`{fn EXTRACT(DAY FROM `*value*`)}`                                 | The day component of the date and/or time *value*
`{fn EXTRACT(HOUR FROM `*value*`)}`                                | The hour component of the date and/or time *value*
`{fn EXTRACT(MINUTE FROM `*value*`)}`                              | The minute component of the date and/or time *value*
`{fn EXTRACT(SECOND FROM `*value*`)}`                              | The second component of the date and/or time *value*
`{fn HOUR(`*time*`)}`                                              | Integer from 0 to 23 indicating the hour of *time*
`{fn MINUTE(`*time*`)}`                                            | Integer from 0 to 59 indicating the minute of *time*
`{fn MONTH(`*date*`)}`                                             | Integer from 1 to 12 indicating the month of *date*
`{fn NOW()}`                                                       | Current date and time
`{fn SECOND(`*time*`)}`                                            | Integer from 0 to 59 indicating the second of *time*
`{fn TIMESTAMPADD(SQL_TSI_YEAR,`*count*`,`*timestamp*`)}`          | Timestamp formed by adding *count* years to *timestamp*
`{fn TIMESTAMPADD(SQL_TSI_MONTH,`*count*`,`*timestamp*`)}`         | Timestamp formed by adding *count* months to *timestamp*
`{fn TIMESTAMPADD(SQL_TSI_DAY,`*count*`,`*timestamp*`)}`           | Timestamp formed by adding *count* days to *timestamp*
`{fn TIMESTAMPADD(SQL_TSI_HOUR,`*count*`,`*timestamp*`)}`          | Timestamp formed by adding *count* hours to *timestamp*
`{fn TIMESTAMPADD(SQL_TSI_MINUTE,`*count*`,`*timestamp*`)}`        | Timestamp formed by adding *count* minutes to *timestamp*
`{fn TIMESTAMPADD(SQL_TSI_SECOND,`*count*`,`*timestamp*`)}`        | Timestamp formed by adding *count* seconds to *timestamp*
`{fn TIMESTAMPDIFF(SQL_TSI_YEAR,`*timestamp1*`,`*timestamp2*`)}`   | Number of years by which *timestamp2* exceeds *timestamp1*
`{fn TIMESTAMPDIFF(SQL_TSI_MONTH,`*timestamp1*`,`*timestamp2*`)}`  | Number of months by which *timestamp2* exceeds *timestamp1*
`{fn TIMESTAMPDIFF(SQL_TSI_DAY,`*timestamp1*`,`*timestamp2*`)}`    | Number of days by which *timestamp2* exceeds *timestamp1*
`{fn TIMESTAMPDIFF(SQL_TSI_HOUR,`*timestamp1*`,`*timestamp2*`)}`   | Number of hours by which *timestamp2* exceeds *timestamp1*
`{fn TIMESTAMPDIFF(SQL_TSI_MINUTE,`*timestamp1*`,`*timestamp2*`)}` | Number of minutes by which *timestamp2* exceeds *timestamp1*
`{fn TIMESTAMPDIFF(SQL_TSI_SECOND,`*timestamp1*`,`*timestamp2*`)}` | Number of seconds by which *timestamp2* exceeds *timestamp1*
`{fn YEAR(`*date*`)}`                                              | The year of *date*

<a id="esc_conversion"></a>

#### Conversion Functions

Conversion function escape clauses are replaced by the corresponding SQL expression before the SQL request text is transmitted to the database.

Conversion Function                                             | Returns
--------------------------------------------------------------- | ---
`{fn CONVERT(`*value*`, SQL_BIGINT)}`                           | *value* converted to SQL `BIGINT`
`{fn CONVERT(`*value*`, SQL_BINARY(`*size*`))}`                 | *value* converted to SQL `BYTE(`*size*`)`
`{fn CONVERT(`*value*`, SQL_CHAR(`*size*`))}`                   | *value* converted to SQL `CHAR(`*size*`)`
`{fn CONVERT(`*value*`, SQL_DATE)}`                             | *value* converted to SQL `DATE`
`{fn CONVERT(`*value*`, SQL_DECIMAL(`*precision*`,`*scale*`))}` | *value* converted to SQL `DECIMAL(`*precision*`,`*scale*`)`
`{fn CONVERT(`*value*`, SQL_DOUBLE)}`                           | *value* converted to SQL `DOUBLE PRECISION`, a synonym for `FLOAT`
`{fn CONVERT(`*value*`, SQL_FLOAT)}`                            | *value* converted to SQL `FLOAT`
`{fn CONVERT(`*value*`, SQL_INTEGER)}`                          | *value* converted to SQL `INTEGER`
`{fn CONVERT(`*value*`, SQL_LONGVARBINARY)}`                    | *value* converted to SQL `VARBYTE(64000)`
`{fn CONVERT(`*value*`, SQL_LONGVARCHAR)}`                      | *value* converted to SQL `LONG VARCHAR`
`{fn CONVERT(`*value*`, SQL_NUMERIC)}`                          | *value* converted to SQL `NUMBER`
`{fn CONVERT(`*value*`, SQL_SMALLINT)}`                         | *value* converted to SQL `SMALLINT`
`{fn CONVERT(`*value*`, SQL_TIME(`*scale*`))}`                  | *value* converted to SQL `TIME(`*scale*`)`
`{fn CONVERT(`*value*`, SQL_TIMESTAMP(`*scale*`))}`             | *value* converted to SQL `TIMESTAMP(`*scale*`)`
`{fn CONVERT(`*value*`, SQL_TINYINT)}`                          | *value* converted to SQL `BYTEINT`
`{fn CONVERT(`*value*`, SQL_VARBINARY(`*size*`))}`              | *value* converted to SQL `VARBYTE(`*size*`)`
`{fn CONVERT(`*value*`, SQL_VARCHAR(`*size*`))}`                | *value* converted to SQL `VARCHAR(`*size*`)`

<a id="esc_like"></a>

#### LIKE Predicate Escape Character

Within a `LIKE` predicate's *pattern* argument, the characters `%` (percent) and `_` (underscore) serve as wildcards.
To interpret a particular wildcard character literally in a `LIKE` predicate's *pattern* argument, the wildcard character must be preceded by an escape character, and the escape character must be indicated in the `LIKE` predicate's `ESCAPE` clause.

`LIKE` predicate escape character escape clauses are replaced by the corresponding SQL clause before the SQL request text is transmitted to the database.

`{escape '`*EscapeCharacter*`'}`

The escape clause must be specified immediately after the `LIKE` predicate that it applies to.

<a id="esc_outerjoin"></a>

#### Outer Joins

Outer join escape clauses are replaced by the corresponding SQL clause before the SQL request text is transmitted to the database.

`{oj `*TableName* *OptionalCorrelationName* `LEFT OUTER JOIN `*TableName* *OptionalCorrelationName* `ON `*JoinCondition*`}`

`{oj `*TableName* *OptionalCorrelationName* `RIGHT OUTER JOIN `*TableName* *OptionalCorrelationName* `ON `*JoinCondition*`}`

`{oj `*TableName* *OptionalCorrelationName* `FULL OUTER JOIN `*TableName* *OptionalCorrelationName* `ON `*JoinCondition*`}`

<a id="esc_call"></a>

#### Stored Procedure Calls

Stored procedure call escape clauses are replaced by the corresponding SQL clause before the SQL request text is transmitted to the database.

`{call `*ProcedureName*`}`

`{call `*ProcedureName*`(`*CommaSeparatedParameterValues...*`)}`

<a id="esc_nativesql"></a>

#### Native SQL

When a SQL request contains the native SQL escape clause, all escape clauses are replaced in the SQL request text, and the modified SQL request text is returned to the application as a result set containing a single row and a single VARCHAR column. The SQL request text is not transmitted to the database, and the SQL request is not executed. The native SQL escape clause mimics the functionality of the JDBC API `Connection.nativeSQL` method.

`{fn teradata_nativesql}`

This escape clause is automatically prepended to the SQL request when the connection `.nativeSQL` method is called.

<a id="esc_connection"></a>

#### Connection Functions

The following table lists connection function escape clauses that are intended for use with the native SQL escape clause `{fn teradata_nativesql}` or the connection `.nativeSQL` method.

These functions provide information about the connection, or control the behavior of the connection.
Functions that provide information return locally-cached information and avoid a round-trip to the database.
Connection function escape clauses are replaced by the returned information before the SQL request text is transmitted to the database.

Connection Function                           | Returns
--------------------------------------------- | ---
`{fn teradata_amp_count}`                     | Number of AMPs of the database system
`{fn teradata_connected}`                     | `true` or `false` indicating whether this connection has logged on
`{fn teradata_database_version}`              | Version number of the database
`{fn teradata_driver_version}`                | Version number of the driver
`{fn teradata_get_errors}`                    | Errors from the most recent batch operation
`{fn teradata_get_warnings}`                  | Warnings from an operation that completed with warnings
`{fn teradata_getloglevel}`                   | Current log level
`{fn teradata_go_runtime}`                    | Go runtime version for the Teradata GoSQL Driver
`{fn teradata_logon_sequence_number}`         | Session's Logon Sequence Number, if available
`{fn teradata_program_name}`                  | Executable program name
`{fn teradata_provide(config_response)}`      | Config Response parcel contents in JSON format
`{fn teradata_provide(connection_id)}`        | Connection's unique identifier within the process
`{fn teradata_provide(default_connection)}`   | `false` indicating this is not a stored procedure default connection
`{fn teradata_provide(dhke)}`                 | Number of round trips for non-TLS Diffie-Hellman key exchange (DHKE) or `0` for TLS with database DHKE bypass
`{fn teradata_provide(gateway_config)}`       | Gateway Config parcel contents in JSON format
`{fn teradata_provide(governed)}`             | `true` or `false` indicating the `govern` connection parameter setting
`{fn teradata_provide(host_id)}`              | Session's host ID
`{fn teradata_provide(java_charset_name)}`    | `UTF8`
`{fn teradata_provide(lob_support)}`          | `true` or `false` indicating this connection's LOB support
`{fn teradata_provide(local_address)}`        | Local address of the connection's TCP socket
`{fn teradata_provide(local_port)}`           | Local port of the connection's TCP socket
`{fn teradata_provide(original_hostname)}`    | Original specified database hostname
`{fn teradata_provide(redrive_active)}`       | `true` or `false` indicating whether this connection has Redrive active
`{fn teradata_provide(remote_address)}`       | Hostname (if available) and IP address of the connected database node
`{fn teradata_provide(remote_port)}`          | TCP port number of the database
`{fn teradata_provide(rnp_active)}`           | `true` or `false` indicating whether this connection has Recoverable Network Protocol active
`{fn teradata_provide(session_charset_code)}` | Session character set code `191`
`{fn teradata_provide(session_charset_name)}` | Session character set name `UTF8`
`{fn teradata_provide(sip_support)}`          | `true` or `false` indicating this connection's StatementInfo parcel support
`{fn teradata_provide(transaction_mode)}`     | Session's transaction mode, `ANSI` or `TERA`
`{fn teradata_provide(uses_check_workload)}`  | `true` or `false` indicating whether this connection uses `CHECK WORKLOAD`
`{fn teradata_session_number}`                | Database session number if connected to a database Gateway or endpoint session number if connected to an endpoint such as Unity, Session Manager, or Business Continuity Manager
`{fn teradata_socket_info}`                   | Information about the TCP socket connection to the database. Format is subject to change. Do not rely on the specific format of the information.

<a id="esc_request"></a>

#### Request-Scope Functions

The following table lists request-scope function escape clauses that are intended for use with the Cursor `.execute` or `.executemany` methods.

These functions control the behavior of the corresponding Cursor, and are limited in scope to the particular SQL request in which they are specified.
Request-scope function escape clauses are removed before the SQL request text is transmitted to the database.

Request-Scope Function                                 | Effect
------------------------------------------------------ | ---
`{fn teradata_agkr(`*Option*`)}`                       | Executes the SQL request with Auto-Generated Key Retrieval (AGKR) *Option* `C` (identity column value) or `R` (entire row)
`{fn teradata_array_transform_off}`                    | Turns off the From-SQL transform for SQL Array values for this SQL request with Request Processing Option `S` (prepare)
`{fn teradata_array_transform_on}`                     | Turns on the From-SQL transform for SQL Array values for this SQL request (the default)
`{fn teradata_clobtranslate(`*Option*`)}`              | Executes the SQL request with CLOB translate *Option* `U` (unlocked) or the default `L` (locked)
`{fn teradata_error_query_count(`*Number*`)}`          | Specifies how many times the driver will attempt to query FastLoad Error Table 1 after a FastLoad operation. Takes precedence over the `error_query_count` connection parameter.
`{fn teradata_error_query_interval(`*Milliseconds*`)}` | Specifies how many milliseconds the driver will wait between attempts to query FastLoad Error Table 1. Takes precedence over the `error_query_interval` connection parameter.
`{fn teradata_error_table_1_suffix(`*Suffix*`)}`       | Specifies the suffix to append to the name of FastLoad error table 1. Takes precedence over the `error_table_1_suffix` connection parameter.
`{fn teradata_error_table_2_suffix(`*Suffix*`)}`       | Specifies the suffix to append to the name of FastLoad error table 2. Takes precedence over the `error_table_2_suffix` connection parameter.
`{fn teradata_error_table_database(`*DbName*`)}`       | Specifies the parent database name for FastLoad error tables 1 and 2. Takes precedence over the `error_table_database` connection parameter.
`{fn teradata_failfast}`                               | Reject ("fail fast") this SQL request rather than delay by a workload management rule or throttle
`{fn teradata_fake_result_sets}`                       | A fake result set containing statement metadata precedes each real result set. Takes precedence over the `fake_result_sets` connection parameter.
`{fn teradata_fake_result_sets_off}`                   | Turns off fake result sets for this SQL request. Takes precedence over the `fake_result_sets` connection parameter.
`{fn teradata_field_quote(`*String*`)}`                | Specifies a single-character string used to quote fields in a CSV file. Takes precedence over the `field_quote` connection parameter.
`{fn teradata_field_sep(`*String*`)}`                  | Specifies a single-character string used to separate fields in a CSV file. Takes precedence over the `field_sep` connection parameter.
`{fn teradata_govern_off}`                             | Teradata workload management rules will reject rather than delay a FastLoad or FastExport. Takes precedence over the `govern` connection parameter.
`{fn teradata_govern_on}`                              | Teradata workload management rules may delay a FastLoad or FastExport. Takes precedence over the `govern` connection parameter.
`{fn teradata_lobselect(`*Option*`)}`                  | Executes the SQL request with LOB select *Option* `S` (spool-scoped LOB locators), `T` (transaction-scoped LOB locators), or the default `I` (inline materialized LOB values)
`{fn teradata_manage_error_tables_off}`                | Turns off FastLoad error table management for this request. Takes precedence over the `manage_error_tables` connection parameter.
`{fn teradata_manage_error_tables_on}`                 | Turns on FastLoad error table management for this request. Takes precedence over the `manage_error_tables` connection parameter.
`{fn teradata_parameter(`*Index*`,`*DataType*`)`       | Transmits parameter *Index* bind values as *DataType*
`{fn teradata_provide(request_scope_column_name_off)}` | Provides the default column name behavior for this SQL request. Takes precedence over the `column_name` connection parameter.
`{fn teradata_provide(request_scope_lob_support_off)}` | Turns off LOB support for this SQL request. Takes precedence over the `lob_support` connection parameter.
`{fn teradata_provide(request_scope_refresh_rsmd)}`    | Executes the SQL request with the default request processing option `B` (both)
`{fn teradata_provide(request_scope_sip_support_off)}` | Turns off StatementInfo parcel support for this SQL request. Takes precedence over the `sip_support` connection parameter.
`{fn teradata_read_csv(`*CSVFileName*`)}`              | Executes a batch insert using the bind parameter values read from the specified CSV file for either a SQL batch insert or a FastLoad
`{fn teradata_request_timeout(`*Seconds*`)}`           | Specifies the timeout for executing the SQL request. Zero means no timeout. Takes precedence over the `request_timeout` connection parameter.
`{fn teradata_require_fastexport}`                     | Specifies that FastExport is required for the SQL request
`{fn teradata_require_fastload}`                       | Specifies that FastLoad is required for the SQL request
`{fn teradata_rpo(`*RequestProcessingOption*`)}`       | Executes the SQL request with *RequestProcessingOption* `S` (prepare), `E` (execute), or the default `B` (both)
`{fn teradata_sessions(`*Number*`)}`                   | Specifies the *Number* of data transfer connections for FastLoad or FastExport. Takes precedence over the `sessions` connection parameter.
`{fn teradata_try_fastexport}`                         | Tries to use FastExport for the SQL request
`{fn teradata_try_fastload}`                           | Tries to use FastLoad for the SQL request
`{fn teradata_udt_transforms_off}`                     | Turns off From-SQL transforms for User Defined Type (UDT) values for this SQL request with Request Processing Option `S` (prepare)
`{fn teradata_udt_transforms_on}`                      | Turns on From-SQL transforms for User Defined Type (UDT) values for this SQL request (the default)
`{fn teradata_untrusted}`                              | Marks the SQL request as untrusted; not implemented yet
`{fn teradata_values_off}`                             | Turns off `teradata_values` for this SQL request. Takes precedence over the `teradata_values` connection parameter. Refer to the [Data Types](#DataTypes) table for details.
`{fn teradata_values_on}`                              | Turns on `teradata_values` for this SQL request. Takes precedence over the `teradata_values` connection parameter. Refer to the [Data Types](#DataTypes) table for details.
`{fn teradata_write_csv(`*CSVFileName*`)}`             | Exports one or more result sets from a SQL request or a FastExport to the specified CSV file or files

The `teradata_field_sep` and `teradata_field_quote` escape functions have a single-character string argument. The string argument must follow SQL literal syntax. The string argument may be enclosed in single-quote (`'`) characters or double-quote (`"`) characters.

To represent a single-quote character in a string enclosed in single-quote characters, you must repeat the single-quote character.

    {fn teradata_field_quote('''')}

To represent a double-quote character in a string enclosed in double-quote characters, you must repeat the double-quote character.

    {fn teradata_field_quote("""")}

<a id="FastLoad"></a>

### FastLoad

The driver offers FastLoad, which opens multiple database connections to transfer data in parallel.

Please be aware that this is an early release of the FastLoad feature. Think of it as a beta or preview version. It works, but does not yet offer all the features that JDBC FastLoad offers. FastLoad is still under active development, and we will continue to enhance it in subsequent builds.

FastLoad has limitations and cannot be used in all cases as a substitute for SQL batch insert:
* FastLoad can only load into an empty permanent table.
* FastLoad cannot load additional rows into a table that already contains rows.
* FastLoad cannot load into a volatile table or global temporary table.
* FastLoad cannot load duplicate rows into a `MULTISET` table with a primary index.
* Do not use FastLoad to load only a few rows, because FastLoad opens extra connections to the database, which is time consuming.
* Only use FastLoad to load many rows (at least 100,000 rows) so that the row-loading performance gain exceeds the overhead of opening additional connections.
* FastLoad does not support all database data types. For example, `BLOB` and `CLOB` are not supported.
* FastLoad requires StatementInfo parcel support to be enabled.
* FastLoad requires read access to the DBC.SessionInfoV view to obtain the database Logon Sequence Number of the FastLoad job.
* FastLoad locks the destination table.
* If Online Archive encounters a table being loaded with FastLoad, online archiving of that table will be bypassed.

Your application can bind a single row of data for FastLoad, but that is not recommended because the overhead of opening additional connections causes FastLoad to be slower than a regular SQL `INSERT` for a single row.

How to use FastLoad:
* Auto-commit should be turned off before beginning a FastLoad.
* FastLoad is intended for binding many rows at a time. Each batch of rows must be able to fit into memory.
* When auto-commit is turned off, your application can insert multiple batches in a loop for the same FastLoad.
* Each column's data type must be consistent across every row in every batch over the entire FastLoad.
* The column values of the first row of the first batch dictate what the column data types must be in all subsequent rows and all subsequent batches of the FastLoad.

FastLoad opens multiple data transfer connections to the database. FastLoad evenly distributes each batch of rows across the available data transfer connections, and uses overlapped I/O to send and receive messages in parallel.

To use FastLoad, your application must prepend one of the following escape functions to the `INSERT` statement:
* `{fn teradata_try_fastload}` tries to use FastLoad for the `INSERT` statement, and automatically executes the `INSERT` as a regular SQL statement when the `INSERT` is not compatible with FastLoad.
* `{fn teradata_require_fastload}` requires FastLoad for the `INSERT` statement, and fails with an error when the `INSERT` is not compatible with FastLoad.

Your application can prepend other optional escape functions to the `INSERT` statement:
* `{fn teradata_sessions(`n`)}` specifies the number of data transfer connections to be opened, and is capped at the number of AMPs. The default is the smaller of 8 or the number of AMPs. We recommend avoiding this function to let the driver ask the database how many data transfer connections should be used.
* `{fn teradata_error_table_1_suffix(`suffix`)}` specifies the suffix to append to the name of FastLoad error table 1. The default suffix is `_ERR_1`.
* `{fn teradata_error_table_2_suffix(`suffix`)}` specifies the suffix to append to the name of FastLoad error table 2. The default suffix is `_ERR_2`.
* `{fn teradata_error_table_database(`dbname`)}` specifies the parent database name for FastLoad error tables 1 and 2. By default, the FastLoad error tables reside in the same database as the destination table.
* `{fn teradata_govern_on}` or `{fn teradata_govern_off}` specifies whether Teradata workload management rules may delay or reject the FastLoad. Takes precedence over the `govern` connection parameter.

After beginning a FastLoad, your application can obtain the Logon Sequence Number (LSN) assigned to the FastLoad by prepending the following escape functions to the `INSERT` statement:
* `{fn teradata_nativesql}{fn teradata_logon_sequence_number}` returns the string form of an integer representing the Logon Sequence Number (LSN) for the FastLoad. Returns an empty string if the request is not a FastLoad.

FastLoad does not stop for data errors such as constraint violations or unique primary index violations. After inserting each batch of rows, your application must obtain warning and error information by prepending the following escape functions to the `INSERT` statement:
* `{fn teradata_nativesql}{fn teradata_get_warnings}` returns in one string all warnings generated by FastLoad for the request.
* `{fn teradata_nativesql}{fn teradata_get_errors}` returns in one string all data errors observed by FastLoad for the most recent batch. The data errors are obtained from FastLoad error table 1, for problems such as constraint violations, data type conversion errors, and unavailable AMP conditions.

Your application ends FastLoad by committing or rolling back the current transaction. After commit or rollback, your application must obtain warning and error information by prepending the following escape functions to the `INSERT` statement:
* `{fn teradata_nativesql}{fn teradata_get_warnings}` returns in one string all warnings generated by FastLoad for the commit or rollback. The warnings are obtained from FastLoad error table 2, for problems such as duplicate rows.
* `{fn teradata_nativesql}{fn teradata_get_errors}` returns in one string all data errors observed by FastLoad for the commit or rollback. The data errors are obtained from FastLoad error table 2, for problems such as unique primary index violations.

Warning and error information remains available until the next batch is inserted or until the commit or rollback. Each batch execution clears the prior warnings and errors. Each commit or rollback clears the prior warnings and errors.

#### FastLoad and Vector Columns

The database can use both the `Vector_IO` and `Vector_IO_VARCHAR` transforms for the same SQL `INSERT` request. In contrast, the database has a limitation such that FastLoad can only use a single transform at a time. FastLoad can use either the `Vector_IO` or the `Vector_IO_VARCHAR` transform but cannot use both transforms for the same FastLoad job.
* With `{fn teradata_try_fastload}` the driver will use FastLoad when your application binds either `VARBYTE` or `VARCHAR` values to Vector columns, but not both. The driver will fall back to SQL `INSERT` if your application binds both `VARBYTE` and `VARCHAR` values to Vector columns in the same request.
* With `{fn teradata_require_fastload}` the driver returns an error when your application binds both `VARBYTE` and `VARCHAR` values to Vector columns in the same request.

<a id="FastExport"></a>

### FastExport

The driver offers FastExport, which opens multiple database connections to transfer data in parallel.

Please be aware that this is an early release of the FastExport feature. Think of it as a beta or preview version. It works, but does not yet offer all the features that JDBC FastExport offers. FastExport is still under active development, and we will continue to enhance it in subsequent builds.

FastExport has limitations and cannot be used in all cases as a substitute for SQL queries:
* FastExport cannot query a volatile table or global temporary table.
* FastExport supports single-statement SQL `SELECT`, and supports multi-statement requests composed of multiple SQL `SELECT` statements only.
* FastExport supports question-mark parameter markers in `WHERE` clause conditions. However, the database does not permit the equal `=` operator for primary or unique secondary indexes, and will return database error 3695 "A Single AMP Select statement has been issued in FastExport".
* Do not use FastExport to fetch only a few rows, because FastExport opens extra connections to the database, which is time consuming.
* Only use FastExport to fetch many rows (at least 100,000 rows) so that the row-fetching performance gain exceeds the overhead of opening additional connections.
* FastExport does not support all database data types. For example, `BLOB` and `CLOB` are not supported.
* For best efficiency, do not use `GROUP BY` and `ORDER BY` clauses with FastExport.
* FastExport's result set ordering behavior may differ from a regular SQL query. In particular, a query containing an ordered analytic function may not produce an ordered result set. Use an `ORDER BY` clause to guarantee result set order.
* FastExport requires read access to the DBC.SessionInfoV view to obtain the database Logon Sequence Number of the FastExport job.

FastExport opens multiple data transfer connections to the database. FastExport uses overlapped I/O to send and receive messages in parallel.

To use FastExport, your application must prepend one of the following escape functions to the query:
* `{fn teradata_try_fastexport}` tries to use FastExport for the query, and automatically executes the query as a regular SQL query when the query is not compatible with FastExport.
* `{fn teradata_require_fastexport}` requires FastExport for the query, and fails with an error when the query is not compatible with FastExport.

Your application can prepend other optional escape functions to the query:
* `{fn teradata_sessions(`n`)}` specifies the number of data transfer connections to be opened, and is capped at the number of AMPs. The default is the smaller of 8 or the number of AMPs. We recommend avoiding this function to let the driver ask the database how many data transfer connections should be used.
* `{fn teradata_govern_on}` or `{fn teradata_govern_off}` specifies whether Teradata workload management rules may delay or reject the FastExport. Takes precedence over the `govern` connection parameter.

After beginning a FastExport, your application can obtain the Logon Sequence Number (LSN) assigned to the FastExport by prepending the following escape functions to the query:
* `{fn teradata_nativesql}{fn teradata_logon_sequence_number}` returns the string form of an integer representing the Logon Sequence Number (LSN) for the FastExport. Returns an empty string if the request is not a FastExport.

<a id="CSVBatchInserts"></a>

### CSV Batch Inserts

The driver can read batch insert bind values from a CSV (comma separated values) file. This feature can be used with SQL batch inserts and with FastLoad.

To specify batch insert bind values in a CSV file, the application prepends the escape function `{fn teradata_read_csv(`*CSVFileName*`)}` to the `INSERT` statement.

The application can specify batch insert bind values in a CSV file, or specify bind parameter values, but not both together. The driver returns an error if both are specified together.

Considerations when using a CSV file:
* Each record is on a separate line of the CSV file. Records are delimited by line breaks (CRLF). The last record in the file may or may not have an ending line break.
* The first line of the CSV file is a header line. The header line lists the column names separated by the field separator (e.g. `col1,col2,col3`).
* The field separator defaults to the comma character (`,`). You can specify a different field separator character with the `field_sep` connection parameter or with the `teradata_field_sep` escape function. The specified field separator character must match the actual separator character used in the CSV file.
* Each field can optionally be enclosed by the field quote character, which defaults to the double-quote character (e.g. `"abc",123,efg`). You can specify a different field quote character with the `field_quote` connection parameter or with the `teradata_field_quote` escape function. The field quote character must match the actual field quote character used in the CSV file.
* The field separator and field quote characters cannot be set to the same value. The field separator and field quote characters must be legal UTF-8 characters and cannot be line feed (`\n`) or carriage return (`\r`).
* Field quote characters are only permitted in fields enclosed by field quote characters. Field quote characters must not appear inside unquoted fields (e.g. not allowed `ab"cd"ef,1,abc`).
* To include a field quote character in a quoted field, the field quote character must be repeated (e.g. `"abc""efg""dh",123,xyz`).
* Line breaks, field quote characters, and field separators may be included in a quoted field (e.g. `"abc,efg\ndh",123,xyz`).
* Specify a `NULL` value in the CSV file with an empty value between commas (e.g. `1,,456`).
* A zero-length quoted string specifies a zero-length non-`NULL` string, not a `NULL` value (e.g. `1,"",456`).
* Not all data types are supported. For example, `BLOB`, `BYTE`, and `VARBYTE` are not supported.
* A field length greater than 64KB is transmitted to the database as a `DEFERRED CLOB` for a SQL batch insert. A field length greater than 64KB is not supported with FastLoad.

Limitations when using CSV batch inserts:
* Bound parameter values cannot be specified in the execute method when using the escape function `{fn teradata_read_csv(`*CSVFileName*`)}`.
* The CSV file must contain at least one valid record in addition to the header line containing the column names.
* For FastLoad, the insert operation will fail if the CSV file is improperly formatted and a parser error occurs.
* For SQL batch insert, some records may be inserted before a parsing error occurs. A list of the parser errors will be returned. Each parser error will include the line number (starting at line 1) and the column number (starting at zero).
* Using a CSV file with FastLoad has the same limitations and is used the same way as described in the [FastLoad](#FastLoad) section.

<a id="CSVExportResults"></a>

### CSV Export Results

The driver can export query results to CSV files. This feature can be used with SQL query results, with calls to stored procedures, and with FastExport.

To export a result set to a CSV file, the application prepends the escape function `{fn teradata_write_csv(`*CSVFileName*`)}` to the SQL request text.

If the query returns multiple result sets, each result set will be written to a separate file. The file name is varied by inserting the string "_N" between the specified file name and file type extension (e.g. `fileName.csv`, `fileName_1.csv`, `fileName_2.csv`). If no file type extension is specified, then the suffix "_N" is appended to the end of the file name (e.g. `fileName`, `fileName_1`, `fileName_2`).

A stored procedure call that produces multiple dynamic result sets behaves like other SQL requests that return multiple result sets. The stored procedures's output parameter values are exported as the first CSV file.

Example of a SQL request that returns multiple results:

`{fn teradata_write_csv(myFile.csv)}select 'abc' ; select 123`

CSV File Name | Content
------------- | ---
myFile.csv    | First result set
myFile_1.csv  | Second result set

To obtain the metadata for each result set, use the escape function `{fn teradata_fake_result_sets}`. A fake result set containing the metadata will be written to a file preceding each real result set.

Example of a query that returns multiple result sets with metadata:

`{fn teradata_fake_result_sets}{fn teradata_write_csv(myFile.csv)}select 'abc' ; select 123`

CSV File Name | Content
------------- | ---
myFile.csv    | Fake result set containing the metadata for the first result set
myFile_1.csv  | First result set
myFile_2.csv  | Fake result set containing the metadata for the second result set
myFile_3.csv  | Second result set

Exported CSV files have the following characteristics:
* Each record is on a separate line of the CSV file. Records are delimited by line breaks (CRLF).
* Column values are separated by the field separator character, which defaults to the comma character (`,`). You can specify a different field separator character with the `field_sep` connection parameter or with the `teradata_field_sep` escape function.
* The first line of the CSV file is a header line. The header line lists the column names separated by the field separator (e.g. `col1,col2,col3`).
* When necessary, column values are enclosed by the field quote character, which defaults to the double-quote character (`"`). You can specify a different field quote character with the `field_quote` connection parameter or with the `teradata_field_quote` escape function.
* The field separator and field quote characters cannot be set to the same value. The field separator and field quote characters must be legal UTF-8 characters and cannot be line feed (`\n`) or carriage return (`\r`).
* If a column value contains line breaks, field quote characters, and/or field separators in a field, the value is quoted with the field quote character.
* If a column value contains a field quote character, the value is quoted and the field quote character is repeated. For example, column value `abc"def` is exported as `"abc""def"`.
* A `NULL` value is exported to the CSV file as an empty value between field separators (e.g. `123,,456`).
* A non-`NULL` zero-length character value is exported as a zero-length quoted string (e.g. `123,"",456`).

Limitations when exporting to CSV files:
* When the application chooses to export results to a CSV file, the results are not available for the application to fetch in memory.
* A warning is returned if the application specifies an export CSV file for a SQL statement that does not produce a result set.
* Exporting a CSV file with FastExport has the same limitations and is used the same way as described in the [FastExport](#FastExport) section.
* Not all data types are supported. For example, `BLOB`, `BYTE`, and `VARBYTE` are not supported and if one of these column types are present in the result set, an error will be returned.
* `CLOB`, `XML`, `JSON`, and `DATASET STORAGE FORMAT CSV` data types are supported for SQL query results and are exported as string values, but these data types are not supported by FastExport.

<a id="CommandLineInterface"></a>

### Command Line Interface

The `teradatasql` module provides a command line interface via the `python -m` option.

Running the `teradatasql` module without additional arguments prints a usage message.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql`
Windows        | `py -3 -m teradatasql`

Any number of arguments can follow the `teradatasql` module name on the command line, and arguments can be repeated on the command line.

The command line interface can print the `teradatasql` version number.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql version`
Windows        | `py -3 -m teradatasql version`

Specify connection parameters to connect to a database.

Connection parameters begin with `host=` and consist of comma-separated key`=`value pairs. A repeated comma `,,` in a connection parameter value is treated as a single literal comma.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql host=whomooz,user=guest,password=please`
Windows        | `py -3 -m teradatasql host=whomooz,user=guest,password=please`

This feature serves as a database connectivity test.

SQL requests can be executed after a database connection is established.

Platform       | Command
-------------- | ---
macOS or Linux | `python -m teradatasql host=whomooz,user=guest,password=please "select * from DBC.DBCInfo"`
Windows        | `py -3 -m teradatasql host=whomooz,user=guest,password=please "select * from DBC.DBCInfo"`

<a id="ChangeLog"></a>

### Change Log

`20.0.0.50` - January 16, 2026
* GOSQL-312 escape functions teradata_array_transform_off/on and teradata_udt_transforms_off/on
* PYDBAPI-158 Module constructor teradatasql.factory to return connection factory function

`20.0.0.49` - January 15, 2026
* GOSQL-300 accept port range for oidc_redirect_port connection parameter
* GOSQL-302 add state parameter to Authorization Code Flow
* GOSQL-310 more StatementInfo parcel fields in fake result set JSON column and parameter metadata

`20.0.0.48` - December 9, 2025
* GOSQL-226 connection parameter local_catalog=true/false default false
* GOSQL-227 fake_result_sets support for OTF catalog name in StatementInfo parcel
* GOSQL-280 Switch to golang.org/x/crypto version 0.45.0
* GOSQL-287 Switch to Go 1.25.5
* GOSQL-290 avoid panic for reconnect after session aborted by administrator

`20.0.0.47` - November 17, 2025
* GOSQL-278 connection parameter ws_endpoint
* PYDBAPI-151 command line interface to manage compute resources

`20.0.0.46` - November 12, 2025
* GOSQL-273 allow host=-none in token mode
* GOSQL-277 escape function teradata_web_service
* GOSQL-279 teradata_write_csv support for FastExport No Spool mode

`20.0.0.44` - October 13, 2025
* PYDBAPI-148 numpy float32 array and float64 array bind values for Vector columns
* PYDBAPI-150 pandas DataFrame bind values for execute and executemany methods
* Build DLL and shared library with Go 1.25.2

`20.0.0.43` - October 9, 2025
* Documentation correction for oidc_redirect_port

`20.0.0.42` - October 9, 2025
* GOSQL-262 add section anchor tags to README files
* GOSQL-264 connection parameter oidc_redirect_port

`20.0.0.41` - September 25, 2025
* GOSQL-255 exclude from revocation checking last certificate in chain if self-signed
* GOSQL-256 token mode
* PYDBAPI-143 experimental Beta feature 32-bit Python for Windows x86
* PYDBAPI-144 experimental Beta feature 32-bit Python for Linux Intel x86

`20.0.0.40` - September 5, 2025
* GOSQL-243 panic recovery with stack traces for top-level APIs
* Build DLL and shared library with Go 1.25.1
* Build DLL with MinGW 15.2.0
* Switch to golang.org/x/crypto version 0.41.0

`20.0.0.39` - September 2, 2025
* GOSQL-242 catch and wrap panic from deserialization

`20.0.0.38` - August 25, 2025
* GOSQL-239 Avoid database Error 3119 after cancel of CREATE PROCEDURE statement

`20.0.0.37` - August 21, 2025
* GOSQL-238 Avoid panic: runtime error: slice bounds out of range from getParcelHeadersFromMessage

`20.0.0.36` - August 20, 2025
* GOSQL-237 Avoid error for missing file /proc/sys/crypto/fips_enabled

`20.0.0.35` - August 19, 2025
* GOSQL-228 Windows automatic FIPS mode
* GOSQL-229 Linux x64 and ARM automatic FIPS mode
* GOSQL-236 macOS FIPS mode with environment variable GODEBUG=fips140=on
* Build DLL and shared library with Go 1.24.6

`20.0.0.34` - August 5, 2025
* GOSQL-215 oauth_scopes connection parameter for OTF catalog and storage SSO
* GOSQL-216 OIDC token refresh

`20.0.0.33` - July 7, 2025
* GOSQL-30 Recoverable Network Protocol and Redrive

`20.0.0.32` - June 11, 2025
* FastLoad to Vector column using transform Vector_IO or Vector_IO_VARCHAR

`20.0.0.31` - June 2, 2025
* Build DLL and shared library with standard Go 1.24.3
* Added import Crypto.Hash.HMAC to sample program TJEncryptPassword.py

`20.0.0.30` - April 25, 2025
* GOSQL-32 DBCCONS partition

`20.0.0.29` - April 22, 2025
* GOSQL-221 connection parameter https_retry
* GOSQL-222 connection parameter sslbase64

`20.0.0.28` - April 5, 2025
* GOSQL-219 sslnamedgroups connection parameter
* GOSQL-220 connection parameter oidc_prompt
* support for Linux ppc64le on 64-bit Power processors
* streamlined teradatasql package description to avoid Azure DevOps artifact metadata limit

`20.0.0.27` - April 1, 2025
* GOSQL-207 OIDC token cache for improved Browser Authentication UX

`20.0.0.26` - March 17, 2025
* Vector data type support for FastLoad
* Build DLL and shared library with standard Go 1.24.1
* Environment variable GODEBUG=fips140=on directs the Go Cryptographic Module to operate in FIPS 140-3 mode, default is off
* No longer uses OpenSSL on Linux, to avoid panic: opensslcrypto: FIPS mode requested (system FIPS mode) but not available in OpenSSL
* client attribute ClientSecProdGrp no longer indicates OpenSSL library on Linux
* Switch to golang.org/x/crypto version 0.36.0

`20.0.0.25` - February 25, 2025
* FIPS support
* proxy server support for FastLoad and FastExport
* GOSQL-182 transmit additional Client Attributes
* client attribute ClientSecProdGrp also indicates OpenSSL library on Linux
* Build DLL and shared library with Microsoft Go 1.24 using build tag goexperiment.systemcrypto for FIPS support
* Requires macOS 12.4 Monterey or later and ends support for older versions of macOS
* Requires Linux kernel version 3.2 or later and ends support for older versions of Linux

`20.0.0.24` - February 3, 2025
* default Linux Kerberos libraries /usr/lib64/libgssapi_krb5.so and /usr/lib64/libgssapi_krb5.so.2

`20.0.0.23` - January 27, 2025
* client attribute ClientSecProdGrp indicates Go crypto library version
* Build DLL and shared library with Go 1.23.5
* Build DLL and shared library with golang.org/x/crypto v0.32.0
* Requires macOS 11 Big Sur or later and ends support for older versions of macOS

`20.0.0.22` - January 6, 2025
* Debug logging for Kerberos library dynamic loading and linking

`20.0.0.21` - December 12, 2024
* Provide driver version number and session number in Teradata Security exceptions
* Add commands to teradatasql module command line interface
* Add connection method `.nativeSQL`

`20.0.0.20` - October 25, 2024
* GOSQL-212 handle Microsoft Entra OIDC Authorization Code Response redirect error parameters
* Add escape function `{fn teradata_provide(dhke)}`
* Improve teradatasql module command line interface

`20.0.0.19` - October 11, 2024
* GOSQL-211 enable logon to database without DHKE bypass after logon to database having DHKE bypass
* Add escape function `{fn teradata_connected}`
* Add teradatasql module `__version__` attribute
* Add teradatasql module command line interface
* Add cursor attribute `columntypename`

`20.0.0.18` - October 7, 2024
* Omit port suffix from HTTP Host: header when using default port 80 for HTTP or 443 for HTTPS
* Build DLL and shared library with Go 1.22.4 (downgrade) to avoid [Go 1.22.5 performance regression issue #68587](https://github.com/golang/go/issues/68587)

`20.0.0.17` - October 1, 2024
* GOSQL-196 Go TeraGSS logmech=JWT bypass DHKE for HTTPS connections
* GOSQL-210 provide Server Name Indication (SNI) field in the TLS client hello
* Build macOS shared library with golang-fips go1.22.5-3-openssl-fips

`20.0.0.16` - September 27, 2024
* GOSQL-177 asynchronous request support
* GOSQL-178 Go TeraGSS logmech=TD2 bypass DHKE for HTTPS connections

`20.0.0.15` - July 31, 2024
* GOSQL-205 Stored Password Protection for http(s)_proxy_password connection parameters
* GOSQL-206 CRC client attribute
* Build DLL and shared library with Go 1.22.5

`20.0.0.14` - July 26, 2024
* GOSQL-203 Go module
* Build DLL and shared library with Go 1.21.9
* Requires macOS 10.15 Catalina or later and ends support for older versions of macOS

`20.0.0.13` - June 24, 2024
* GOSQL-198 oidc_sslmode connection parameter
* GOSQL-199 sslcrc=ALLOW and PREFER soft fail CRC for VERIFY-CA and VERIFY-FULL
* GOSQL-200 sslcrc=REQUIRE requires CRC for VERIFY-CA and VERIFY-FULL

`20.0.0.12` - April 30, 2024
* GOSQL-31 Monitor partition

`20.0.0.11` - April 25, 2024
* GOSQL-193 Device Code Flow and Client Credentials Flow

`20.0.0.10` - April 10, 2024
* GOSQL-185 Use FIPS-140 Compliant Modules
* Build DLL and shared library with Go 1.20.14
* Build DLL and shared library with Microsoft Go for Windows, Linux Intel, Linux ARM
* Build shared library with golang-fips for macOS Intel, macOS ARM

`20.0.0.9` - April 2, 2024
* Include teradatasql.arm.so in package

`20.0.0.8` - March 18, 2024
* GOSQL-121 Linux ARM support
* GOSQL-184 remove DES and DESede
* PYDBAPI-124 remove DES and DESede
* PYDBAPI-131 cursor attributes activitytype and activityname

`20.0.0.7` - February 1, 2024
* GOSQL-189 improved error messages for missing or invalid logmech value
* GOSQL-190 Go TeraGSS accommodate DH/CI bypass flag in JWT token header

`20.0.0.6` - January 19, 2024
* GOSQL-183 TLS certificate verification for Identity Provider endpoints

`20.0.0.5` - January 17, 2024
* GOSQL-151 proxy server support

`20.0.0.4` - January 9, 2024
* Build DLL and shared library with Go 1.20.12

`20.0.0.2` - December 8, 2023
* Improved exception message for query timeout
* New sample programs CancelSleep.py and MultiThread.py

`20.0.0.1` - November 16, 2023
* Build DLL and shared library with Go 1.20.11

`20.0.0.0` - November 7, 2023
* TDGSS-7022 Go TeraGSS Phase 1
* TDGSS-7232 Go TeraGSS Phase 2
* TDGSS-7233 Go TeraGSS Phase 3
* TDGSS-8123 Integrate Go TeraGSS with the GoSQL Driver phase 1
* TDGSS-8345 Go TeraGSS Phase 4
* TDGSS-9050 Integrate Go TeraGSS with the GoSQL Driver phase 2
* GOSQL-148 TDNEGO logon mechanism for Go TeraGSS
* GOSQL-158 switch to Go TeraGSS
* GOSQL-181 improve TDNEGO interoperability with Kerberos

`17.20.0.32` - October 23, 2023
* GOSQL-179 fake result sets add SPParameterDirection to ColumnMetadata and ParameterMetadata
* GOSQL-180 fake result sets add stored procedure IN parameters to ParameterMetadata

`17.20.0.31` - September 27, 2023
* GOSQL-176 better error message for missing host connection parameter

`17.20.0.30` - September 19, 2023
* GOSQL-175 avoid panic: cannot create context from nil parent
* PYDBAPI-122 provide py.typed file
* PYDBAPI-123 autocommit property for TeradataConnection

`17.20.0.29` - September 5, 2023
* Build DLL and shared library with Go 1.19.12
* Requires 64-bit Python 3.7 or later and ends support for older versions of Python
* Added sample program InsertLob.py

`17.20.0.28` - July 21, 2023
* Build DLL and shared library with Go 1.19.11
* UTC match values for sample program `TJEncryptPassword.py`

`17.20.0.27` - June 23, 2023
* Additional changes for GOSQL-128 use OIDC scope from Gateway Config parcel

`17.20.0.26` - June 15, 2023
* GOSQL-165 Auto-Generated Key Retrieval (AGKR)
* GOSQL-167 use loopback IP address for OIDC redirect

`17.20.0.25` - June 2, 2023
* GOSQL-142 sp_spl connection parameter
* fake result set columns StatementNumber and WarningCode are now INTEGER

`17.20.0.24` - May 23, 2023
* GOSQL-41 escape function teradata_provide(request_scope_column_name_off)
* GOSQL-124 runstartup connection parameter

`17.20.0.23` - May 19, 2023
* GOSQL-157 logon_timeout connection parameter

`17.20.0.22` - May 16, 2023
* Build DLL and shared library with Go 1.19.9

`17.20.0.21` - May 15, 2023
* GOSQL-128 use OIDC scope from Gateway Config parcel

`17.20.0.20` - May 5, 2023
* GOSQL-155 teradata_provide(gateway_config) teradata_provide(governed) teradata_provide(uses_check_workload)

`17.20.0.19` - March 30, 2023
* GOSQL-129 TLS certificate revocation checking with CRL
* GOSQL-130 TLS certificate revocation checking with OCSP (not OCSP stapling)
* GOSQL-132 sslcrc connection parameter

`17.20.0.18` - March 27, 2023
* GOSQL-146 FastLoad and FastExport Unicode Pass Through support

`17.20.0.17` - March 24, 2023
* Build DLL and shared library with Go 1.19.7
* GOSQL-136 escape functions teradata_manage_error_tables_off and teradata_manage_error_tables_on
* GOSQL-139 allow alternate LOCATOR(type) syntax for teradata_parameter escape function
* GOSQL-145 connection parameters error_query_count, error_query_interval, error_table_1_suffix, error_table_2_suffix, error_table_database, manage_error_tables, sessions

`17.20.0.16` - February 21, 2023
* GOSQL-138 avoid panic for aborted session

`17.20.0.15` - February 16, 2023
* GOSQL-137 limit the max number of records in a CSV batch

`17.20.0.14` - January 19, 2023
* GOSQL-24 Asynchronous abort SQL request execution
* GOSQL-134 escape function teradata_request_timeout
* GOSQL-135 connection parameter request_timeout
* PYDBAPI-114 Connection.cancel method to cancel executing SQL request

`17.20.0.13` - January 17, 2023
* GOSQL-133 return FastLoad errors for FastLoad with teradata_read_csv

`17.20.0.12` - December 2, 2022
* Build DLL and shared library with Go 1.19.3
* GOSQL-126 escape functions teradata_values_off and teradata_values_on

`17.20.0.11` - November 1, 2022
* GOSQL-125 FastLoad FastExport govern support for fake_result_sets=true
* GOSQL-127 substitute dash for unavailable program name in Client Attributes

`17.20.0.10` - October 27, 2022
* GOSQL-67 FastLoad FastExport workload management
* GOSQL-120 govern connection parameter
* GOSQL-123 conditional use of Statement Independence depending on database setting

`17.20.0.9` - October 25, 2022
* Build DLL and shared library with Go 1.18.7

`17.20.0.8` - October 19, 2022
* GOSQL-122 case-insensitive VERIFY-FULL

`17.20.0.7` - September 27, 2022
* Avoid Kerberos logon failure

`17.20.0.6` - September 19, 2022
* Build DLL and shared library with Go 1.18.6

`17.20.0.5` - September 15, 2022
* Additional changes for GOSQL-119 avoid nil pointer dereference for FastExport CSV error

`17.20.0.4` - September 14, 2022
* GOSQL-87 support Mac ARM without Rosetta
* GOSQL-119 avoid nil pointer dereference for FastExport CSV error

`17.20.0.3` - September 6, 2022
* GOSQL-118 teradata_write_csv support for queries containing commas

`17.20.0.2` - August 23, 2022
* GOSQL-117 browser_tab_timeout connection parameter

`17.20.0.1` - August 11, 2022
* Build DLL and shared library with Go 1.18.5

`17.20.0.0` - June 16, 2022
* GOSQL-74 FastLoad support for connection parameter fake_result_sets=true

`17.10.0.16` - June 6, 2022
* GOSQL-106 indicate unavailable TLS certificate status with ClientAttributesEx CERT=U

`17.10.0.15` - June 2, 2022
* Switch to TeraGSS 17.20.00.04 and OpenSSL 1.1.1l
* Requires macOS 10.14 Mojave or later and ends support for older versions of macOS

`17.10.0.14` - May 18, 2022
* GOSQL-104 FastExport reports invalid CSV path name for first query but not subsequent
* GOSQL-105 Avoid driver failure when database warning length is invalid

`17.10.0.13` - May 16, 2022
* GOSQL-53 browser and logmech=BROWSER connection parameters
* GOSQL-56 Implement Federated Authentication feature in GoSQL Driver
* PYDBAPI-77 Implement Federated Authentication feature in Python driver

`17.10.0.12` - April 15, 2022
* GOSQL-71 TLS certificate verification
* GOSQL-98 remove escape function teradata_setloglevel

`17.10.0.11` - April 7, 2022
* GOSQL-82 Escape functions teradata_field_sep and teradata_field_quote
* GOSQL-97 FastLoad/FastExport accommodate extra whitespace in SQL request

`17.10.0.10` - March 24, 2022
* GOSQL-95 case-insensitive sslmode connection parameter values
* GOSQL-96 avoid CVE security vulnerabilities present in Go 1.17 and earlier
* Build DLL and shared library with Go 1.18
* Requires macOS 10.13 High Sierra or later and ends support for older versions of macOS

`17.10.0.9` - March 18, 2022
* GOSQL-94 thread-safe connect failure cache

`17.10.0.8` - March 9, 2022
* GOSQL-84 accommodate 64-bit Activity Count
* GOSQL-92 FastLoad returns error 512 when first column value is NULL

`17.10.0.7` - February 23, 2022
* GOSQL-91 Avoid Error 8019 by always sending Config Request message

`17.10.0.6` - February 4, 2022
* GOSQL-26 provide stored procedure creation errors
* GOSQL-73 Write CSV files
* GOSQL-88 Append streamlined client call stack to ClientProgramName

`17.10.0.5` - January 10, 2022
* GOSQL-86 provide UDF compilation errors

`17.10.0.4` - December 13, 2021
* GOSQL-20 TLS support
* GOSQL-29 Laddered Concurrent Connect
* PYDBAPI-82 Implement Laddered Concurrent Connect in Python driver

`17.10.0.3` - November 30, 2021
* GOSQL-12 Centralized administration for data encryption
* GOSQL-25 Assign Response message error handling
* GOSQL-27 Enhance checks for missing logon parameters
* GOSQL-65 improve terasso error messages
* GOSQL-66 transmit Client Attributes to DBS during logon
* PYDBAPI-58 Centralized administration (from database) of Data Encryption
* Build DLL and shared library with Go 1.15.15

`17.10.0.2` - July 2, 2021
* GOSQL-33 CALL to stored procedure INOUT and OUT parameter output values
* GOSQL-35 Statement Independence
* GOSQL-72 Read CSV files
* PYDBAPI-39 JSON, CSV, and Avro data type support
* PYDBAPI-83 Escape Syntax for FLOAT Data Type

`17.10.0.1` - June 9, 2021
* Corrected documentation formatting for PyPI

`17.10.0.0` - June 8, 2021
* GOSQL-75 trim whitespace from SQL request text

`17.0.0.8` - December 18, 2020
* Documentation changes

`17.0.0.7` - December 18, 2020
* GOSQL-13 add support for FastExport protocol

`17.0.0.6` - October 9, 2020
* GOSQL-68 cross-process COP hostname load distribution

`17.0.0.5` - August 26, 2020
* GOSQL-64 improve error checking for FastLoad escape functions

`17.0.0.4` - August 18, 2020
* GOSQL-62 prevent nativesql from executing FastLoad
* GOSQL-63 prevent FastLoad panic

`17.0.0.3` - July 30, 2020
* Build DLL and shared library with Go 1.14.6

`17.0.0.2` - June 10, 2020
* GOSQL-60 CLOBTranslate=Locked workaround for DBS DR 194293

`17.0.0.1` - June 4, 2020
* GOSQL-61 FastLoad accommodate encryptdata true

`16.20.0.62` - May 12, 2020
* GOSQL-58 support multiple files for Elicit File protocol
* GOSQL-59 FastLoad accommodate dbscontrol change of COUNT(*) return type

`16.20.0.61` - Apr 30, 2020
* GOSQL-57 Deferred LOB values larger than 1MB

`16.20.0.60` - Mar 27, 2020
* GOSQL-22 enable insert of large LOB values over 64KB
* GOSQL-52 teradata_try_fastload consider bind value data types
* GOSQL-54 enforce Decimal value maximum precision 38
* PYDBAPI-37 Teradata Data Types Support up to 14.10 including LOB data

`16.20.0.59` - Jan 8, 2020
* GOSQL-51 FastLoad fails when table is dropped and recreated
* PYDBAPI-72 bind value performance improvement
* PYDBAPI-73 DBAPI fails to insert 16383 rows

`16.20.0.58` - Dec 11, 2019
* PYDBAPI-71 execute and executemany ignoreErrors parameter

`16.20.0.57` - Dec 10, 2019
* GOSQL-50 provide FastLoad duplicate row errors with auto-commit on

`16.20.0.56` - Dec 4, 2019
* PYDBAPI-70 raise error for closed cursor usage

`16.20.0.55` - Nov 26, 2019
* GOSQL-15 add database connection parameter
* PYDBAPI-66 Better exception when running on 32-bit Python

`16.20.0.54` - Nov 21, 2019
* GOSQL-49 FastLoad support for additional connection parameters

`16.20.0.53` - Nov 15, 2019
* GOSQL-36 segment and iterate parameter batches per batch row limit
* GOSQL-43 segment and iterate parameter batches per request message size limit for FastLoad

`16.20.0.52` - Oct 18, 2019
* Sample programs for fake result sets

`16.20.0.51` - Oct 16, 2019
* GOSQL-46 LDAP password special characters

`16.20.0.50` - Oct 7, 2019
* PYDBAPI-68 improve performance for batch bind values

`16.20.0.49` - Oct 3, 2019
* GOSQL-45 FastLoad interop with Stored Password Protection

`16.20.0.48` - Sep 6, 2019
* GOSQL-14 add support for FastLoad protocol
* GOSQL-34 negative scale for Number values
* PYDBAPI-29 Data Transfer - FastLoad Protocol

`16.20.0.47` - Aug 27, 2019
* GOSQL-40 Skip executing empty SQL request text
* PYDBAPI-67 teradatasql.connect JSON connection string optional

`16.20.0.46` - Aug 16, 2019
* GOSQL-39 COP Discovery interop with Kerberos

`16.20.0.45` - Aug 12, 2019
* GOSQL-38 timestamp prefix log messages

`16.20.0.44` - Aug 7, 2019
* GOSQL-4 Support COP discovery
* PYDBAPI-36 COP Discovery

`16.20.0.43` - Jul 29, 2019
* GOSQL-18 Auto-commit
* PYDBAPI-61 commit and rollback methods

`16.20.0.42` - Jun 7, 2019
* PYDBAPI-65 sample program `BatchInsert.py`

`16.20.0.41` - Feb 14, 2019
* PYDBAPI-57 fetchmany may return "rows are closed" instead of empty result set

`16.20.0.40` - Feb 8, 2019
* GOSQL-11 JWT authentication method
* GOSQL-16 tmode connection parameter
* GOSQL-17 commit and rollback functions

`16.20.0.39` - Oct 26, 2018
* GOSQL-33 CALL to stored procedure INOUT and OUT parameter output values

`16.20.0.38` - Oct 25, 2018
* PYDBAPI-56 Stored Procedure Dynamic Result Sets

`16.20.0.37` - Oct 22, 2018
* Documentation change

`16.20.0.36` - Oct 22, 2018
* GOSQL-5 Create/Replace Procedure MultiTSR protocol

`16.20.0.35` - Oct 22, 2018
* GOSQL-10 Stored Password Protection
* PYDBAPI-28 Secure Password at rest
* PYDBAPI-47 Port sample program TJEncryptPassword to Python

`16.20.0.34` - Oct 15, 2018
* Fix for sample program `TJEncryptPassword.py`

`16.20.0.33` - Oct 12, 2018
* Installation dependency pycryptodome

`16.20.0.32` - Sep 19, 2018
* Sample programs `LoadCSVFile.py` and `MetadataFromPrepare.py`
* Escape function teradata_fake_result_sets

`16.20.0.31` - Sep 19, 2018
* Added function tracing

`16.20.0.30` - Sep 14, 2018
* PYDBAPI-12 Connectivity
* PYDBAPI-33 Pandas library Interoperability
* Moved samples directory

`16.20.0.29` - Sep 14, 2018
* Sample program `ElicitFile.py`

`16.20.0.28` - Sep 13, 2018
* Documentation change

`16.20.0.27` - Sep 12, 2018
* Documentation change

`16.20.0.26` - Sep 11, 2018
* PYDBAPI-8 Documentation
* PYDBAPI-9 User Guide Content

`16.20.0.25` - Sep 10, 2018
* Documentation change

`16.20.0.24` - Sep 6, 2018
* PYDBAPI-54 Implement cursor rowcount attribute
* PYDBAPI-55 Improved support for Python data types

`16.20.0.23` - Aug 31, 2018
* KeepResponse only for LOB locators

`16.20.0.22` - Aug 30, 2018
* Fixed NUMBER values

`16.20.0.21` - Aug 29, 2018
* Close orphaned rows

`16.20.0.20` - Aug 28, 2018
* decimal and datetime values

`16.20.0.19` - Aug 22, 2018
* timedelta bind values

`16.20.0.18` - Aug 21, 2018
* datetime.datetime bind values

`16.20.0.17` - Aug 20, 2018
* Version number in errors

`16.20.0.16` - Aug 17, 2018
* SLES 11 SP1 compatibility

`16.20.0.15` - Aug 17, 2018
* Documentation change

`16.20.0.14` - Aug 10, 2018
* Documentation change

`16.20.0.13` - Aug 9, 2018
* Documentation change

`16.20.0.12` - Aug 9, 2018
* PYDBAPI-10 User Guide Delivery and Viewability
* PYDBAPI-11 Searchability

`16.20.0.11` - Aug 8, 2018
* Documentation change

`16.20.0.10` - Aug 8, 2018
* Documentation change

`16.20.0.9` - Aug 7, 2018
* Install documentation in teradatasql directory

`16.20.0.8` - Aug 7, 2018
* GOSQL-7 TDNEGO authentication method
* PYDBAPI-42 Teradata Logon mechanism - TDNEGO

`16.20.0.7` - Jul 30, 2018
* GOSQL-8 Support parameter marker batch insert
* PYDBAPI-45 Parameterized Batch Insertion using executeMany

`16.20.0.6` - Jul 25, 2018
* Thread safety for handle maps

`16.20.0.5` - Jul 25, 2018
* Removed atexit

`16.20.0.4` - Jul 23, 2018
* PYDBAPI-4 Provide Python Driver license file

`16.20.0.3` - Jul 19, 2018
* PYDBAPI-46 Accept subclasses of bytes, int, float, str as bind values

`16.20.0.2` - Jul 19, 2018
* Package attributes change

`16.20.0.1` - Jul 18, 2018
* Version number change

`16.20.0.0` - Jul 18, 2018
* GOSQL-1 Encrypted logon
* GOSQL-2 LDAP and Kerberos authentication
* GOSQL-3 Support for 1MB Rows
* GOSQL-6 Elicit File protocol
* PYDBAPI-1 Distribution
* PYDBAPI-5 cursor.execute method return cursor
* PYDBAPI-6 Install and Deployment
* PYDBAPI-7 pip install of python driver package
* PYDBAPI-13 Operating System Platforms
* PYDBAPI-14 Driver must be available for use by Windows OS Users
* PYDBAPI-15 Driver must be available for use by OSX (Mac) Users
* PYDBAPI-16 Driver must be available for use by Linux OS Users
* PYDBAPI-17 Python Language version
* PYDBAPI-18 Python language version 3.4
* PYDBAPI-19 Distribution
* PYDBAPI-23 Teradata Analytics Platform Interoperability/Support
* PYDBAPI-24 Works with Teradata Database 16.10, 16.20
* PYDBAPI-26 Teradata Logon mechanism - Kerberos
* PYDBAPI-32 Downloadable from pypi.org
* PYDBAPI-40 Teradata Logon mechanism - LDAP
* PYDBAPI-41 Teradata Logon mechanism - TD2
* PYDBAPI-43 parameterized single-row inserts
* PYDBAPI-44 parameterized queries
