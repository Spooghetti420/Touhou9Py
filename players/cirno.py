from players.player import Characters, Player


class Cirno(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.CIRNO,
            move_speed = 4.7,
            focus_speed = 3.3
        )
