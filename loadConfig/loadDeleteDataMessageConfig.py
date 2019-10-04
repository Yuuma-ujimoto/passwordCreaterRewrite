import json
import codecs


def load_delete_data_message() -> dict:
    file_path: str = "./config/deleteDataMessage.json"
    with codecs.open(filename=file_path, mode="r", encoding="utf-8") as config_file:
        config_data: dict = json.load(config_file)
    return config_data

