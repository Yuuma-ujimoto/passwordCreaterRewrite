import json
import codecs


def load_message_data(message_type: str = "main") -> dict:
    file_path: str = "./message_data/AllMessage.json"
    with codecs.open(filename=file_path, mode="r", encoding="utf-8") as message_file:
        all_message_data: dict = json.load(message_file)
    if message_type in all_message_data:
        message_data: dict = all_message_data[message_type]
        return message_data
    else:
        exit()
