from players.player import Characters, Player


class Tewi(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.TEWI,
            move_speed = 4.5,
            focus_speed = 1.9
        )
