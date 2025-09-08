import yaml
from typing import List
from .models import WorksheetConfig, ConfigModel

def load_yaml_config(config_path: str) -> ConfigModel:
    with open(config_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    worksheets = []
    for ws in data.get("worksheets", []):
        worksheets.append(
            WorksheetConfig(
                name=ws["name"],
                start_row=ws.get("start_row", 1),
                start_col=ws.get("start_col", 1)
            )
        )
    return ConfigModel(worksheets=worksheets)