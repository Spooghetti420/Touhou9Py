from players.player import Characters, Player


class Mystia(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.MYSTIA,
            move_speed = 5.0,
            focus_speed = 3.4
        )
