from players.player import Characters, Player


class Eiki(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.CIRNO,
            move_speed = 5.0,
            focus_speed = 2.4
        )
