from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class WorksheetConfig:
    name: str
    start_row: int
    start_col: int

@dataclass
class TableSchema:
    name: str
    columns: List[str]
    types: List[str]

@dataclass
class ConfigModel:
    worksheets: List[WorksheetConfig]