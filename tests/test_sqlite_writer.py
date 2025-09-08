import sqlite3
import tempfile
import os
from excel2sqlite_cli.sqlite_writer import create_table_and_insert

def test_create_table_and_insert():
    db_fd, db_path = tempfile.mkstemp(suffix=".db")
    conn = sqlite3.connect(db_path)
    columns = ["col1", "col2"]
    rows = [["あ", "い"], ["う", "え"]]
    create_table_and_insert(conn, "TestTable", columns, rows)

    cursor = conn.execute('SELECT * FROM "TestTable";')
    results = cursor.fetchall()
    assert results == [("あ", "い"), ("う", "え")]

    conn.close()
    os.close(db_fd)
    os.remove(db_path)