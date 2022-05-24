from abc import ABC, abstractmethod

from players.player import Characters


class Stage(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def update(self):
        pass

class BambooForestOfTheLost(Stage):
    pass

class PhantomMeadow(Stage):
    pass

class KyakugyokurousStairway(Stage):
    pass

class Eientei(Stage):
    pass

class MistyLake(Stage):
    pass

class BarrierOfLifeAndDeath(Stage):
    pass

class YoukaiTrail(Stage):
    pass

class GiantToadsPond(Stage):
    pass

class RoadOfReconsideration(Stage):
    pass

class Muenzuka(Stage):
    pass

HomeStages = {
    Characters.AYA: GiantToadsPond,
    Characters.CIRNO: MistyLake,
    Characters.EIKI: Muenzuka,
    Characters.KOMACHI: RoadOfReconsideration,
    Characters.LUNASA: BarrierOfLifeAndDeath,
    Characters.LYRICA: BarrierOfLifeAndDeath,
    Characters.MARISA: BambooForestOfTheLost,
    Characters.MEDICINE: BambooForestOfTheLost,
    Characters.MERLIN: BarrierOfLifeAndDeath,
    Characters.MYSTIA: YoukaiTrail,
    Characters.REIMU: BambooForestOfTheLost,
    Characters.REISEN: Eientei,
    Characters.YOUMU: KyakugyokurousStairway,
    Characters.SAKUYA: PhantomMeadow,
    Characters.TEWI: BambooForestOfTheLost,
    Characters.YUUKA: BambooForestOfTheLost
}