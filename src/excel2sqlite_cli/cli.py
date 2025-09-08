import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate SQLite3 DB from Excel Workbook using YAML config."
    )
    parser.add_argument(
        "--excel", required=True, help="Path to Excel workbook (.xlsx)"
    )
    parser.add_argument(
        "--config", required=True, help="Path to YAML configuration file"
    )
    parser.add_argument(
        "--output", required=True, help="Path to output SQLite3 database file"
    )
    return parser.parse_args()