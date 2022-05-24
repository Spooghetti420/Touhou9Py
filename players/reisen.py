from players.player import Characters, Player


class Reisen(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.REISEN,
            move_speed = 4.5,
            focus_speed = 2.5
        )
