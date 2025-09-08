import openpyxl
import tempfile
import os
from excel2sqlite_cli.models import WorksheetConfig
from excel2sqlite_cli.excel_reader import read_worksheet_data

def test_read_worksheet_data():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "TestSheet"
    ws.append(["A", "B", "C"])
    ws.append([1, 2, 3])
    ws.append([4, 5, 6])

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    wb.save(tmp_file.name)
    tmp_file.close()

    ws_cfg = WorksheetConfig(name="TestSheet", start_row=1, start_col=1)
    data = read_worksheet_data(tmp_file.name, ws_cfg)
    assert data[0] == ["A", "B", "C"]
    assert data[1] == [1, 2, 3]
    assert data[2] == [4, 5, 6]

    os.remove(tmp_file.name)