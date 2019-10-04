import json
import codecs


def load_edit_config_message() -> dict:
    with codecs.open(filename="./config/MainMessage.json", mode="r", encoding="utf-8") as config_file:
        config_data: dict = json.load(config_file)

    return config_data
