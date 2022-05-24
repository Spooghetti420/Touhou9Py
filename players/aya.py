from players.player import Characters, Player


class Aya(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.AYA,
            move_speed = 5.5,
            focus_speed = 3.5
        )
