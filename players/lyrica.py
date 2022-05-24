from players.player import Characters, Player


class Lyrica(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.LYRICA,
            move_speed = 4.2,
            focus_speed = 2.2
        )
