import yaml
from typing import List
from .models import WorksheetConfig, ConfigModel
import jsonschema

CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "worksheets": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "start_row": {"type": "integer", "minimum": 1},
                    "start_col": {"type": "integer", "minimum": 1}
                },
                "required": ["name"]
            }
        }
    },
    "required": ["worksheets"]
}

class ConfigValidationError(Exception):
    pass

def load_yaml_config(config_path: str) -> ConfigModel:
    with open(config_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    try:
        jsonschema.validate(instance=data, schema=CONFIG_SCHEMA)
    except jsonschema.ValidationError as e:
        raise ConfigValidationError(f"YAML config validation failed: {e.message}")
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