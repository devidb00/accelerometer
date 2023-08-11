import os
import pyodbc

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    # Définissez les informations de connexion
    server = os.environ["server"]
    database = os.environ["database"]
    username = os.environ["user"]
    password = os.environ["password"]

    # Créez une connexion
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};Server=%s;Database=%s;Uid=%s;Pwd=%s" % (
            server, database, username, password)
    )

    # Fermez la connexion
    conn.close()
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )
