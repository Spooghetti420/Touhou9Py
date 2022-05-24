"""
This module defines all the possible Scenarios for the different characters.
Each character may experience a multitude of slightly different campaigns.
"""
import random
from players.aya import Aya
from players.cirno import Cirno
from players.eiki import Eiki
from players.komachi import Komachi
from players.lyrica import Lyrica
from players.marisa import Marisa
from players.mystia import Mystia
from players.player import Characters, Player
from players.reisen import Reisen
from players.sakuya import Sakuya
from players.tewi import Tewi
from players.youmu import Youmu
from stage import BambooForestOfTheLost, BarrierOfLifeAndDeath, Eientei, KyakugyokurousStairway, YoukaiTrail, MistyLake

def GenerateScenario(*stage_choices):
    """
    `stage_choices` is a list of 9 elements which specifies the options for each level.
    Options tuple looks like (A, B, C...) where each term is a tuple of (Player, Stage).
    """
    out = []
    seen = set()
    for option in stage_choices:
        proceed = False
        while not proceed:
            char = random.choice(option)
            if char not in seen:
                proceed = True
        out.append(char)
        seen.add(char)
    return out

def ScenarioReimu():
    return GenerateScenario(
        (Mystia, Cirno),
        (Mystia, Cirno, Lyrica),
        (Lyrica, Tewi, Reisen),
        (Lyrica, Tewi, Reisen),
        (Youmu, Marisa, Sakuya),
        (Marisa, Sakuya),
        (Aya,),
        (Komachi,),
        (Eiki,)
    )

def ScenarioMarisa():
    pass


def ScenarioSakuya():
    pass


def ScenarioYoumu():
    pass


def ScenarioReisen():
    pass


def ScenarioCirno():
    pass


def ScenarioLyrica():
    pass


def ScenarioMerlin():
    pass


def ScenarioLunasa():
    pass


def ScenarioMystia():
    pass


def ScenarioTewi():
    pass


def ScenarioAya():
    pass


def ScenarioMedicine():
    pass


def ScenarioYuuka():
    pass


def ScenarioKomachi():
    pass


def ScenarioEiki():
    pass


CAMPAIGNS = {
    Characters.REIMU: ScenarioReimu,
    Characters.MARISA: ScenarioMarisa,
    Characters.SAKUYA: ScenarioSakuya,
    Characters.YOUMU: ScenarioYoumu,
    Characters.REISEN: ScenarioReisen,
    Characters.CIRNO: ScenarioCirno,
    Characters.LYRICA: ScenarioLyrica,
    Characters.MERLIN: ScenarioMerlin,
    Characters.LUNASA: ScenarioLunasa,
    Characters.MYSTIA: ScenarioMystia,
    Characters.TEWI: ScenarioTewi,
    Characters.AYA: ScenarioAya,
    Characters.MEDICINE: ScenarioMedicine,
    Characters.YUUKA: ScenarioYuuka,
    Characters.KOMACHI: ScenarioKomachi,
    Characters.EIKI: ScenarioEiki
}

def get_campaign(char: Characters) -> list[Player]:
    return CAMPAIGNS[char]()