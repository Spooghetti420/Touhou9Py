from players.player import Characters, Player


class Marisa(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.MARISA,
            move_speed = 5.0,
            focus_speed = 3.0
        )
