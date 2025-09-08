from openpyxl import load_workbook
from .models import WorksheetConfig
from typing import List, Any

def read_worksheet_data(excel_path: str, ws_config: WorksheetConfig) -> List[List[Any]]:
    wb = load_workbook(excel_path, data_only=True)
    ws = wb[ws_config.name]
    data = []
    for row in ws.iter_rows(
        min_row=ws_config.start_row,
        min_col=ws_config.start_col,
        values_only=True
    ):
        data.append(list(row))
    return data