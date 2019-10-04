import savePassWord
import loadConfig
import editConfig

MESSAGE_DATA: dict = loadConfig.load_message_data(message_type="setting")
config: dict = loadConfig.load_config()
edit_config_flag: bool = False
while True:
    if edit_config_flag:
        config = loadConfig.load_config()
        edit_config_flag = False
    print(">_{message}".format(
        message=MESSAGE_DATA["InputCommand"]
    ))
    command: str = input()
    if command == config["exit"]:
        print(">_{message}".format(
            message=MESSAGE_DATA["Exit"]
        ))
        break
    elif command == config["help"]:
        print(">_{message}".format(
            message=MESSAGE_DATA["Help"]
        ))
        continue
    elif command == config["delete"]:
        savePassWord.delete_data()
        continue
    elif command == config["config"]:
        config = loadConfig.load_config()
        for key, value in config.items():
            print(f"key:{key}\tValue:{value}")
        continue
    elif command == config["edit"]:
        config = loadConfig.load_config()
        while True:
            print(">_{message}".format(
                message=MESSAGE_DATA["Edit"]
            ))
            edit_key = input()
            print(edit_key)
            if edit_key in config:
                print(">_{message}".format(
                    message=MESSAGE_DATA["FoundKey"]
                ))
                break
            elif edit_key == config["exit"]:
                break
            else:
                print(">_{message}".format(
                    message=MESSAGE_DATA["NotFoundKey"]
                ))
        if edit_key == config["exit"]:
            continue
        edit_value = input()
        editConfig.edit_config(edit_key, edit_value)
        edit_config_flag = True
    else:
        print(">_{message}".format(
            message=MESSAGE_DATA["EmptyCommand"]
        ))
