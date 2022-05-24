from players.player import Characters, Player


class Lunasa(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.LUNASA,
            move_speed = 4.5,
            focus_speed = 2.5
        )
