import loadConfig
import json
import codecs


def edit_config(key, value):
    message_data = loadConfig.load_message_data(message_type="edit")
    save_data = loadConfig.load_config()
    save_data[key] = value
    try:
        file_name: str = "./config/config.json"
        with codecs.open(filename=file_name, mode="w", encoding="utf-8") as config_file:
            json.dump(save_data, config_file)
        success_message = ">_{message}".format(
            message=message_data["Success"]
        )
        return success_message
    except Exception as save_config_error:
        error_message = ">_{error}{message}".format(
            error=save_config_error,
            message=message_data["Error"]
        )
        return error_message
