from players.player import Characters, Player


class Yuuka(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.YUUKA,
            move_speed = 3.0,
            focus_speed = 1.8
        )
