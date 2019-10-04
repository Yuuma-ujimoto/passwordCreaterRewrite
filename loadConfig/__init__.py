from .loadConfig import load_config
from .loadMessageConfig import load_main_message
from .loadSavePassWordMessageConfig import load_save_pass_message
from .loadDeleteDataMessageConfig import load_delete_data_message
from .loadSetttingConfig import load_setting_message
from .loadEditConfigMessage import load_edit_config_message
# これだけ
from .loadMessageData import load_message_data
"""
命名規則
[目的/load::save]_[取得先]_[取得データの種類/message::config::data]
"""


__ALL__: list = ["load_config",
                 "load_main_message",
                 "load_save_pass_message",
                 "load_delete_data_message",
                 "load_setting_message",
                 "load_edit_config_message"
                 ]
