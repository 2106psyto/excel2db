import sys
from .cli import parse_args
from .config import load_yaml_config
from .excel_reader import read_worksheet_data
from .sqlite_writer import create_table_and_insert

import sqlite3

def main():
    args = parse_args()
    config = load_yaml_config(args.config)
    conn = sqlite3.connect(args.output)
    for ws_cfg in config.worksheets:
        data = read_worksheet_data(args.excel, ws_cfg)
        if not data:
            print(f"Warning: No data found in worksheet '{ws_cfg.name}'")
            continue
        columns = [str(c) if c is not None else f"col{i+1}" for i, c in enumerate(data[0])]
        rows = data
        create_table_and_insert(conn, ws_cfg.name, columns, rows)
        print(f"Imported worksheet '{ws_cfg.name}' to table '{ws_cfg.name}'")
    conn.close()

if __name__ == "__main__":
    main()