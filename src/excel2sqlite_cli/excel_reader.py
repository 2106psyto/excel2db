from openpyxl import load_workbook, utils
from .models import WorksheetConfig
from typing import List, Any

def read_worksheet_data(excel_path: str, ws_config: WorksheetConfig) -> List[List[Any]]:
    wb = load_workbook(excel_path, data_only=True)
    ws = wb[ws_config.name]
    data = []
    start_row, start_col = utils.coordinate_to_tuple(ws_config.start_cell)
    for row in ws.iter_rows(
        min_row=start_row,
        min_col=start_col,
        values_only=True
    ):
        data.append(list(row))
    return data