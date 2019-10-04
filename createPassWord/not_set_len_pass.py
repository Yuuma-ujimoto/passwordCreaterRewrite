import string
import random


def not_len_pass() -> str:
    """
    8~14桁のランダムなパスワードを生成する。

    Returns
    -------
    password : str
        ランダムに生成されたパスワード

    See Also
    --------
    set_len_pass : パスワードの桁数を指定したい時に使うための関数。
                   指定された引数の値に応じてパスワードの桁数が変わる。
    """
    password: str = ""
    set_data: str = string.digits + string.ascii_letters
    loop_num: int = random.randint(8, 14)
    for loop in range(0, loop_num):
        choice_character: str = random.choice(set_data)
        password += choice_character
    return password
