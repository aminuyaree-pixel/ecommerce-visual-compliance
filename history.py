
import sqlite3
import json
from pathlib import Path
from datetime import datetime

# Database location
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATA_DIR / "history.db"


def initialize_db():

    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            description TEXT,
            image_name TEXT,
            detections TEXT,
            matches TEXT,
            findings TEXT,
            status TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_analysis(description, image_name,
                  detections, matches, findings):

    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        INSERT INTO analyses (
            created_at,
            description,
            image_name,
            detections,
            matches,
            findings,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        description,
        image_name,
        json.dumps(detections, default=str),
        json.dumps(matches, default=str),
        json.dumps(findings, default=str),
        "Review Required" if findings else "No Demo Rule Matched"
    ))

    connection.commit()
    connection.close()


def get_history():

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    records = connection.execute("""
        SELECT * FROM analyses
        ORDER BY id DESC
    """).fetchall()

    connection.close()

    return [dict(record) for record in records]


def get_statistics():

    connection = sqlite3.connect(DB_PATH)

    total = connection.execute(
        "SELECT COUNT(*) FROM analyses"
    ).fetchone()[0]

    flagged = connection.execute("""
        SELECT COUNT(*) FROM analyses
        WHERE status = 'Review Required'
    """).fetchone()[0]

    connection.close()

    return {
        "total": total,
        "flagged": flagged,
        "not_flagged": total - flagged
    }


def get_analysis_by_id(analysis_id):

    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row

    record = connection.execute("""
        SELECT * FROM analyses
        WHERE id = ?
    """, (analysis_id,)).fetchone()

    connection.close()

    if record is None:
        return None

    analysis = dict(record)

    analysis["detections"] = json.loads(
        analysis["detections"] or "[]"
    )

    analysis["matches"] = json.loads(
        analysis["matches"] or "[]"
    )

    analysis["findings"] = json.loads(
        analysis["findings"] or "[]"
    )

    return analysis
