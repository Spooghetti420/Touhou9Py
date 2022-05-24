from players.player import Characters, Player


class Merlin(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.MERLIN,
            move_speed = 3.8,
            focus_speed = 2.0
        )
