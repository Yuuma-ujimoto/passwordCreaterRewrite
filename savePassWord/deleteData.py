import os
import pathlib
import loadConfig


def delete_data():
    file_path: str = './pass/password.txt'
    message_data: dict = loadConfig.load_message_data(message_type="delete")
    try:
        os.remove(file_path)
        pathlib.Path(file_path)
        delete_data_success_message: str = ">_{0}".format(
            message_data["Success"]
        )
        return delete_data_success_message

    except Exception as delete_data_error:
        delete_data_error_message: str = ">_{0}:{1}".format(
            delete_data_error,
            message_data["Error"]
        )
        return delete_data_error_message
