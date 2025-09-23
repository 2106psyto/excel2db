import sys
import tempfile
import yaml
import openpyxl
import os
import pytest
from excel2sqlite_cli.main import main

def test_main_workflow(monkeypatch):
    # Prepare Excel file
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["名前", "値"])
    ws.append(["りんご", "100"])
    ws.append(["みかん", "200"])
    excel_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(excel_file.name)
    excel_file.close()

    # Prepare YAML config
    config_dict = {
        "worksheets": [
            {"name": "Sheet1", "start_cell": "A1", "header_rows": 1}
        ]
    }
    config_file = tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml", encoding="utf-8")
    yaml.dump(config_dict, config_file)
    config_file.close()

    # Prepare output DB
    output_db = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
    output_db.close()

    # Patch sys.argv
    monkeypatch.setattr(sys, "argv", [
        "main.py",
        "--excel", excel_file.name,
        "--config", config_file.name,
        "--output", output_db.name
    ])

    main()

    # Check DB contents
    import sqlite3
    conn = sqlite3.connect(output_db.name)
    cursor = conn.execute('SELECT * FROM "Sheet1";')
    rows = cursor.fetchall()
    assert rows == [("名前", "値"), ("りんご", "100"), ("みかん", "200")]
    conn.close()

    os.remove(excel_file.name)
    os.remove(config_file.name)
    os.remove(output_db.name)
