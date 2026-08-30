from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import (
    fetch_all,
    fetch_one,
    execute_query
)


app = FastAPI(
    title="Rural Care API",
    description="Healthcare platform for rural communities",
    version="1.0.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# ALLOWED TABLES
# --------------------------------------------------

ALLOWED_TABLES = {
    "health_information",
    "health_records",
    "healthcare_centres"
}


# --------------------------------------------------
# HOME
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "success": True,
        "message": "Rural Care API is running"
    }


# --------------------------------------------------
# DATABASE STATUS
# --------------------------------------------------

@app.get("/database-status")
def database_status():

    result = fetch_one(
        "SELECT 1 AS connected"
    )

    if result:
        return {
            "success": True,
            "connected": True,
            "message": "MySQL/MariaDB connected successfully"
        }

    return {
        "success": False,
        "connected": False,
        "message": "Database connection failed"
    }


# --------------------------------------------------
# GET TABLE COLUMNS
# --------------------------------------------------

@app.get("/table-columns/{table_name}")
def get_table_columns(table_name: str):

    if table_name not in ALLOWED_TABLES:
        raise HTTPException(
            status_code=400,
            detail="Invalid table name"
        )

    query = """
        SELECT
            COLUMN_NAME,
            DATA_TYPE,
            IS_NULLABLE,
            COLUMN_KEY,
            EXTRA
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'defaultdb'
        AND TABLE_NAME = %s
        ORDER BY ORDINAL_POSITION
    """

    columns = fetch_all(
        query,
        (table_name,)
    )

    return {
        "success": True,
        "table": table_name,
        "columns": columns
    }


# --------------------------------------------------
# HEALTH INFORMATION
# --------------------------------------------------

@app.get("/health-information")
def get_health_information():

    data = fetch_all(
        "SELECT * FROM health_information"
    )

    return {
        "success": True,
        "data": data
    }


# --------------------------------------------------
# HEALTH RECORDS
# --------------------------------------------------

@app.get("/health-records")
def get_health_records():

    data = fetch_all(
        """
        SELECT
            id,
            record_type,
            record_date,
            description,
            created_at
        FROM health_records
        ORDER BY record_date DESC, id DESC
        """
    )

    return {
        "success": True,
        "data": data
    }
# --------------------------------------------------
# HEALTHCARE CENTRES
# --------------------------------------------------

@app.get("/healthcare-centres")
def get_healthcare_centres():

    data = fetch_all(
        "SELECT * FROM healthcare_centres"
    )

    return {
        "success": True,
        "data": data
    }


# =========================================================
# ADD HEALTH RECORD
# =========================================================

@app.post("/health-records")
def add_health_record(record: dict):

    record_type = record.get("record_type")
    record_date = record.get("record_date")
    description = record.get("description")


    # -----------------------------
    # VALIDATION
    # -----------------------------

    if not record_type or not record_type.strip():
        raise HTTPException(
            status_code=400,
            detail="Record type is required"
        )

    if not record_date:
        raise HTTPException(
            status_code=400,
            detail="Record date is required"
        )

    if not description or not description.strip():
        raise HTTPException(
            status_code=400,
            detail="Description is required"
        )


    # -----------------------------
    # INSERT INTO DATABASE
    # -----------------------------

    query = """
        INSERT INTO health_records
        (
            record_type,
            record_date,
            description
        )
        VALUES
        (%s, %s, %s)
    """

    params = (
        record_type.strip(),
        record_date,
        description.strip()
    )


    success = execute_query(
        query,
        params
    )


    if not success:
        raise HTTPException(
            status_code=500,
            detail="Failed to save health record"
        )


    # -----------------------------
    # GET INSERTED RECORD
    # -----------------------------

    new_record = fetch_one(
        """
        SELECT
            id,
            record_type,
            record_date,
            description,
            created_at
        FROM health_records
        ORDER BY id DESC
        LIMIT 1
        """
    )


    return {
        "success": True,
        "message": "Health record added successfully",
        "data": new_record
    }