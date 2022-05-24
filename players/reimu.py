from players.player import Characters, Player


class Reimu(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.REIMU,
            move_speed = 4.0,
            focus_speed = 2.0
        )
