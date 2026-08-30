import sqlite3
import os


DATABASE_PATH = "database/progress.db"


def create_database():

    os.makedirs("database", exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            language TEXT,

            sentence TEXT,

            corrected_sentence TEXT,

            grammar_score INTEGER,

            vocabulary_score INTEGER,

            overall_score INTEGER,

            difficulty TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_session(
    language,
    sentence,
    corrected_sentence,
    grammar_score,
    vocabulary_score,
    overall_score,
    difficulty
):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions (
            language,
            sentence,
            corrected_sentence,
            grammar_score,
            vocabulary_score,
            overall_score,
            difficulty
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        language,
        sentence,
        corrected_sentence,
        grammar_score,
        vocabulary_score,
        overall_score,
        difficulty
    ))

    connection.commit()

    connection.close()


def get_sessions():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            language,
            sentence,
            corrected_sentence,
            grammar_score,
            vocabulary_score,
            overall_score,
            difficulty,
            created_at
        FROM sessions
        ORDER BY created_at DESC
    """)

    data = cursor.fetchall()

    connection.close()

    return data


def get_average_scores():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            AVG(grammar_score),
            AVG(vocabulary_score),
            AVG(overall_score)
        FROM sessions
    """)

    result = cursor.fetchone()

    connection.close()

    return result