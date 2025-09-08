import sqlite3
from typing import List, Any

def create_table_and_insert(conn: sqlite3.Connection, table_name: str, columns: List[str], rows: List[List[Any]]):
    # Infer column types as TEXT for simplicity, can be improved
    col_defs = ', '.join([f'"{col}" TEXT' for col in columns])
    col_names = ', '.join([f'"{col}"' for col in columns])
    conn.execute(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({col_defs});')
    placeholders = ', '.join(["?"] * len(columns))
    for row in rows:
        conn.execute(f'INSERT INTO "{table_name}" ({col_names}) VALUES ({placeholders});', row)
    conn.commit()