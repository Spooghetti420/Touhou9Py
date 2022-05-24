from players.player import Characters, Player


class Komachi(Player):
    def __init__(self) -> None:
        super().__init__(
            character = Characters.KOMACHI,
            move_speed = 4.1,
            focus_speed = 2.2
        )
