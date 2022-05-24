from players.player import Characters, Player


class Medicine(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.MEDICINE,
            move_speed = 5.0,
            focus_speed = 2.4
        )
