import os
import tempfile
import yaml
import pytest
from excel2sqlite_cli.config import load_yaml_config, ConfigValidationError

def test_load_yaml_config_valid():
    config_dict = {
        "worksheets": [
            {"name": "Sheet1", "start_row": 2, "start_col": 1},
            {"name": "Sheet2", "start_row": 1, "start_col": 3}
        ]
    }
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml", encoding="utf-8") as tmp:
        yaml.dump(config_dict, tmp)
        tmp_path = tmp.name

    config = load_yaml_config(tmp_path)
    assert len(config.worksheets) == 2
    assert config.worksheets[0].name == "Sheet1"
    assert config.worksheets[0].start_row == 2
    assert config.worksheets[1].start_col == 3

    os.remove(tmp_path)

def test_load_yaml_config_invalid():
    # Missing 'worksheets' key
    invalid_dict = {
        "foo": "bar"
    }
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml", encoding="utf-8") as tmp:
        yaml.dump(invalid_dict, tmp)
        tmp_path = tmp.name

    with pytest.raises(ConfigValidationError):
        load_yaml_config(tmp_path)

    os.remove(tmp_path)

def test_load_yaml_config_missing_name():
    # Worksheet missing 'name'
    invalid_dict = {
        "worksheets": [
            {"start_row": 1, "start_col": 1}
        ]
    }
    with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".yaml", encoding="utf-8") as tmp:
        yaml.dump(invalid_dict, tmp)
        tmp_path = tmp.name

    with pytest.raises(ConfigValidationError):
        load_yaml_config(tmp_path)

    os.remove(tmp_path)