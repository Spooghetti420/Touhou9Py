import math
import random
from pygame import Surface
import pygame
from assets import get_image
from campaign import get_campaign
from config import campaign_get_starting_lives
from constants import GAMEPLAY_SCREEN_SIZE
from players.aya import Aya
from players.cirno import Cirno
from players.eiki import Eiki
from players.komachi import Komachi
from players.lunasa import Lunasa
from players.lyrica import Lyrica
from players.marisa import Marisa
from players.medicine import Medicine
from players.merlin import Merlin
from players.mystia import Mystia
from players.player import Emotions, Player
from players.reimu import Reimu
from players.reisen import Reisen
from players.sakuya import Sakuya
from players.tewi import Tewi
from players.youmu import Youmu
from players.yuuka import Yuuka
from scene import Scene
from window import screen


class CampaignScene(Scene):
    def __init__(self, player: Player) -> None:
        players = [Aya, Cirno, Eiki, Komachi, Lunasa, Lyrica, Marisa, Medicine, Merlin, Mystia, Reimu, Reisen, Sakuya, Tewi, Youmu, Yuuka]
        self.player1: Player = Reimu()
        self.player2: Player = None
        # self.player1: Player = random.choice(players)()

        self.campaign = get_campaign(self.player1.character)
        self.current_stage = 4
        self.next_level()  # Will set player 2 automatically depending on the first stage

        # self.player2: Player = random.choice(players)().is_player_two()

        self.extra_lives = campaign_get_starting_lives()

        self.left_side = Surface(GAMEPLAY_SCREEN_SIZE)
        self.right_side = Surface(GAMEPLAY_SCREEN_SIZE)

        self.border = get_image("border.png")
        self.charge_bar = get_image("charge_bar.png")
        self.spell_point_box = get_image("spell_point_box.png")
        self.hp_full = get_image("hp_full.png")
        self.hp_half = get_image("hp_half.png")
        self.hp_empty = get_image("hp_empty.png")
        self.extra_life = get_image("extra_life.png")

    def next_level(self):
        self.current_stage += 1
        self.player2 = self.campaign[self.current_stage]().is_player_two()
        


    def update(self, dt: float):

        screen.blit(self.border, (0, 0))
        self.left_side.fill((0, 0, 0))
        self.right_side.fill((0, 0, 0))
        self.player1.update()
        self.player2.update()

        self.player1.show(self.left_side)
        self.player2.show(self.right_side)

        self.draw_ui()

        screen.blit(self.left_side, (16, 16))
        screen.blit(self.right_side, (336, 16))

        # self.player1.draw_portrait(Emotions.EXCITED, pos=(0, 160))
        # self.player2.draw_portrait(Emotions.EXCITED, pos=(384, 160))

    def draw_ui(self):
        for (player, side) in zip((self.player1, self.player2), (self.left_side, self.right_side)):

            charge_color = [
                (160, 160, 160),
                (200, 200, 107),
                (202, 200, 0),
                (216, 216, 170),
                (210, 75, 114)
            ][math.floor(player.current_charge)]
            
            pygame.draw.rect(side, (108, 108, 108), (17, 444, 256*player.charge_level/4, 3))
            pygame.draw.rect(side, charge_color, (17, 444, 256*player.current_charge/4, 3))



            side.blit(self.charge_bar, (16, 442))
            side.blit(self.spell_point_box, (1, 1))

            hp = player.hp
            orbs = 0
            pos = 109
            while orbs < 5:
                if hp >= 2:
                    img_to_draw = self.hp_full
                    hp -= 2
                elif hp == 1:
                    img_to_draw = self.hp_half
                    hp -= 1
                else:
                    img_to_draw = self.hp_empty

                side.blit(img_to_draw, (pos, 1))
                pos += 15
                orbs += 1

        for i in range(self.extra_lives):
            self.left_side.blit(self.extra_life, (1 + i * 13, 33))