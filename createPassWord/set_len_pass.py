import string
import random


def set_len_pass(length: int)->str:
    """
    指定された桁のランダムなパスワードを生成する。

    Args
    ----
    length : int
      生成したいパスワードの長さ

    Returns
    -------
    password : str
      ランダムに生成されたパスワード

    See Also
    --------
    not_len_pass :
      パスワードの桁数を指定していない時に使うための関数。8~14桁のランダムなパスワードが生成される.
    """
    password: str = ""

    set_data: str = string.digits + string.ascii_letters

    loop_num: int = length
    for loop in range(0, loop_num):
        choice_character: str = random.choice(set_data)
        password += choice_character
    return password
