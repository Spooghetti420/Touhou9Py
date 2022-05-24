from typing import Union

DEFAULT_CONFIG = {
    # General
    "extra_lives": 3,
    "bgm": True,
    "bgm_volume": 100,
    "se_volume": 80,
    "fullscreen": True,
    # Controls
    ## General controls
    "escape": 41,
    "ctrl": 224,
    "home": 74,
    "q": 20,
    # Singleplayer
    "sg_up": 82,
    "sg_down": 81,
    "sg_left": 80,
    "sg_right": 79,
    "sg_z": 29,
    "sg_x": 27,
    "sg_slow": 225,
    # Player-1-specific
    "p1_up": 23,
    "p1_down": 10,
    "p1_left": 9,
    "p1_right": 11,
    "p1_z": 29,
    "p1_x": 27,
    "p1_slow": 225, 
}

# class Config:
#     def __init__(self):
#         try:
#             with open("settings.cfg", mode="rb") as config:
#                 self.extra_lives = int.from_bytes(config.read(1), "big")
                
#                 bgm_int = int.from_bytes(config.read(1), "big")
#                 settings["bgm"] = True if bgm_int == 1 else False
                
#                 settings["bgm_volume"] = int.from_bytes(config.read(1), "big")
#                 settings["se_volume"] = int.from_bytes(config.read(1), "big")

#                 fullscreen_int = int.from_bytes(config.read(1), "big")
#                 settings["fullscreen"] = True if fullscreen_int == 1 else False

#         except FileNotFoundError:
#             write_config(DEFAULT_CONFIG)

#     @staticmethod
#     def bytes_generic(data: Union[bool, int], length=1) -> bytes:
#         try:
#             return data.to_bytes(length, "big")
#         except OverflowError:
#             return Config.bytes_generic(data, length+1)

#     @staticmethod
#     def restore_bytes(binary: bytes, type):

#     def write_config(self, settings: dict) -> None:
#         with open("settings.cfg", mode="wb") as config:
#             config.write(settings["extra_lives"].to_bytes(1, "big"))
#             config.write(settings["bgm"].to_bytes(1, "big"))
#             config.write(settings["bgm_volume"].to_bytes(1, "big"))
#             config.write(settings["se_volume"].to_bytes(1, "big"))
#             config.write(settings["fullscreen"].to_bytes(1, "big"))


def campaign_get_starting_lives() -> int:
    return 2

# configuration = read_config()