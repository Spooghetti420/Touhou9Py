from players.player import Characters, Player


class Sakuya(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.SAKUYA,
            move_speed = 4.0,
            focus_speed = 3.2
        )
