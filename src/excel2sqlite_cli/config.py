import yaml
import jsonschema
from .models import WorksheetConfig, ConfigModel

CONFIG_SCHEMA = {
    "type": "object",
    "properties": {
        "worksheets": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "start_cell": {
                        "type": "string",
                        "pattern": "^[A-Z]+[1-9][0-9]*$"
                    }
                },
                "required": ["name", "start_cell"]
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
                start_cell=ws["start_cell"]
            )
        )
    return ConfigModel(worksheets=worksheets)