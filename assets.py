"""
This module defines the `assets` dict which will contain
a series of filepath-asset key-value pairs, which
map from a filepath to a Surface or Sound.
"""
import enum
import os.path
from pygame import Surface
import pygame
from pygame.image import load as load_image
from pygame.mixer import Sound

images: dict = {}
sounds: dict = {}
pygame.mixer.init()

def get_image(filename: str) -> Surface:
    if filename not in images:
        images[filename] = load_image(os.path.join("images", filename))
    
    return images[filename]

def get_sound(filename: str) -> Sound:
    if filename not in sounds:
        sounds[filename] = Sound(os.path.join("sounds", filename))
    
    return sounds[filename]

class BGM(enum.Enum):
    花映塚 = "01. 花映塚　～ Higan Retour.wav"
    春色小径 = "02. 春色小径　～ Colorful Path.wav"
    オリエンタルダークフライト = "03. オリエンタルダークフライト.wav"
    フラワリングナイト = "04. フラワリングナイト.wav"
    東方妖々夢 = "05. 東方妖々夢　～ Ancient Temple.wav"
    狂気の瞳 = "06. 狂気の瞳　～ Invisible Full Moon.wav"
    おてんば恋娘の冒険 = "07. おてんば恋娘の冒険.wav"
    幽霊楽団 = "08. 幽霊楽団　～ Phantom Ensemble.wav"
    もう歌しか聞こえない = "09. もう歌しか聞こえない　～ Flower Mix.wav"
    お宇佐さまの素い幡 = "10. お宇佐さまの素い幡.wav"
    風神少女 = "11. 風神少女　 (Short Version).wav"
    ポイズンボディ = "12. ポイズンボディ　～ Forsaken Doll.wav"
    今昔幻想郷 = "13. 今昔幻想郷　～ Flower Land.wav"
    彼岸帰航 = "14. 彼岸帰航　～ Riverside View.wav"
    六十年目の東方裁判 = "15. 六十年目の東方裁判　～ Fate of Sixty Years.wav"
    花の映る塚 = "16. 花の映る塚.wav"
    此岸の塚 = "17. 此岸の塚.wav"
    花は幻想のままに = "18. 花は幻想のままに.wav"
    魂の花 = "19. 魂の花　～ Another Dream.wav"

def set_bgm(track: BGM):
    global current_bgm
    current_bgm = pygame.mixer.music.load(os.path.join("bgm", track.value))

set_bgm(BGM.花映塚)

current_bgm.play()
