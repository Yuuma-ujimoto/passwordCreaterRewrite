import pyperclip
import savePassWord
import loadConfig
import createPassWord


class Main:
    def __init__(self):
        self.password: str = ""
        self.name: str = ""
        self.command: list = []
        self.password_length: int = 0
        self.config: dict = loadConfig.load_config()
        self.message: dict = loadConfig.load_message_data(message_type="main")
        self.y_or_n: str = ""
        self.save_password_message: str = ""
        self.input_name()

    def input_name(self):
        print(">_{message}".format(
            message=self.message["Input"]
        ))
        self.command: str = input().split()
        self.name = self.command[0]
        if len(self.command) == 2:
            if self.command[1].isdigit():
                self.set_len_pass()
            else:
                self.input_name()
        else:
            self.not_len_pass()

    def not_len_pass(self):
        self.password = createPassWord.not_len_pass()
        self.save_check()

    def set_len_pass(self):
        self.password_length = int(self.command[1])
        self.password = createPassWord.set_len_pass(
            length=self.password_length
        )
        self.save_check()

    def save_check(self):
        print(">_{password_message}:{password}\n>_{name_message}:{name}\n>_{message}".format(
            password_message=self.message["PassWord"],
            password=self.password,
            name_message=self.message["Name"],
            name=self.name,
            message=self.message["Registration"]
        ),
            end="")
        self.registration_check()

    def registration_check(self):
        print("{y}/{n}".format(
            y=self.config["yes"],
            n=self.config["no"]
        ))
        self.y_or_n: str = input()
        if self.y_or_n == "y" or self.y_or_n == "n":
            if self.y_or_n == "y":
                self.save()
            else:
                print(">_{message}".format(
                    message=self.message["Exit"]
                ))
                # exit()
        else:
            self.registration_check()

    def save(self):

        pyperclip.copy(self.password)
        self.save_password_message = savePassWord.save_pass_word(
            name=self.name,
            password=self.password
        )
        print(">_{message}".format(
            message=self.save_password_message
        ))


if __name__ == '__main__':
    Main()
