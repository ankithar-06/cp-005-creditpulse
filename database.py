
import sqlite3
from pathlib import Path
from datetime import datetime

# Store the database inside the project's data folder
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "creditpulse.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS score_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                recorded_at TEXT NOT NULL,
                payment REAL NOT NULL,
                utilisation REAL NOT NULL,
                account_age REAL NOT NULL,
                enquiries INTEGER NOT NULL,
                credit_types INTEGER NOT NULL,
                estimated_score INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)


def save_score(
    payment,
    utilisation,
    account_age,
    enquiries,
    credit_types,
    estimated_score,
    category
):
    recorded_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with get_connection() as connection:
        connection.execute("""
            INSERT INTO score_history (
                recorded_at,
                payment,
                utilisation,
                account_age,
                enquiries,
                credit_types,
                estimated_score,
                category
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            recorded_at,
            payment,
            utilisation,
            account_age,
            enquiries,
            credit_types,
            estimated_score,
            category
        ))


def get_score_history():
    with get_connection() as connection:
        rows = connection.execute("""
            SELECT *
            FROM score_history
            ORDER BY recorded_at ASC
        """).fetchall()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    create_table()
    print("CreditPulse database created successfully!")

    history = get_score_history()
    print("Existing history records:", len(history))
