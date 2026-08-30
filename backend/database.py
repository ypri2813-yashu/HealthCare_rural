
import os
import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", "26389")),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "defaultdb"),
    "ssl_ca": os.getenv("DB_SSL_CA")
}


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():

    try:

        connection = mysql.connector.connect(
            **DB_CONFIG
        )

        if connection.is_connected():

            print("✅ Aiven Cloud MySQL connected")

            return connection

    except Error as e:

        print("❌ Database connection error:", e)

    return None


# =========================================================
# FETCH ALL
# =========================================================

def fetch_all(query, params=None):

    connection = get_connection()

    if connection is None:
        return []

    cursor = None

    try:

        cursor = connection.cursor(
            dictionary=True
        )

        if params:

            cursor.execute(
                query,
                params
            )

        else:

            cursor.execute(query)

        return cursor.fetchall()

    except Error as e:

        print("❌ Database query error:", e)

        return []

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# FETCH ONE
# =========================================================

def fetch_one(query, params=None):

    connection = get_connection()

    if connection is None:
        return None

    cursor = None

    try:

        cursor = connection.cursor(
            dictionary=True
        )

        if params:

            cursor.execute(
                query,
                params
            )

        else:

            cursor.execute(query)

        return cursor.fetchone()

    except Error as e:

        print("❌ Database query error:", e)

        return None

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# EXECUTE INSERT / UPDATE / DELETE
# =========================================================

def execute_query(query, params=None):

    connection = get_connection()

    if connection is None:
        return False

    cursor = None

    try:

        cursor = connection.cursor()

        if params:

            cursor.execute(
                query,
                params
            )

        else:

            cursor.execute(query)

        connection.commit()

        return True

    except Error as e:

        print("❌ Database update error:", e)

        connection.rollback()

        return False

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# TEST CONNECTION
# =========================================================

if __name__ == "__main__":

    connection = get_connection()

    if connection:

        print("====================================")
        print("✅ CLOUD MYSQL CONNECTION SUCCESS")
        print("Database: defaultdb")
        print("Host: Aiven")
        print("====================================")

        connection.close()

    else:

        print("====================================")
        print("❌ CLOUD MYSQL CONNECTION FAILED")
        print("====================================")
