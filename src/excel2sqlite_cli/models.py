from dataclasses import dataclass
from typing import List

@dataclass
class WorksheetConfig:
    name: str
    start_cell: str  # e.g., "C21", "AN7"
    header_rows: int = 1  # Number of rows to treat as header, default is 1

@dataclass
class TableSchema:
    name: str
    columns: List[str]
    types: List[str]

@dataclass
class ConfigModel:
    worksheets: List[WorksheetConfig]