import codecs
import loadConfig


def save_pass_word(name: str, password: str) -> str:
    message_data: dict = loadConfig.load_message_data(message_type="save")
    save_string: str = "{name} : {password}\n".format(
        name=name,
        password=password
    )
    try:
        with codecs.open("./pass/password.txt", "a", encoding="utf-8") as save_file:
            save_file.write(save_string)
        save_password_success_message: str = ">_{message}".format(
            message=message_data["Success"]
        )
        return save_password_success_message
    except Exception as save_file_error:
        save_password_error_message: str = ">_Error:{error}{message}".format(
            error=save_file_error,
            message=message_data["Error"]
        )
        return save_password_error_message
