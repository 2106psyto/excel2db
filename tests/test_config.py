import os
import tempfile
import yaml
from excel2sqlite_cli.config import load_yaml_config

def test_load_yaml_config():
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