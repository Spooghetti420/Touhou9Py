from players.player import Characters, Player


class Youmu(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.YOUMU,
            move_speed = 5.0,
            focus_speed = 2.1
        )
