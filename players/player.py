import enum
import math
from typing import Tuple
import pygame
from window import screen
from assets import BGM, get_image

class Characters(enum.Enum):
    REIMU = 0
    MARISA = 1
    SAKUYA = 2
    YOUMU = 3
    REISEN = 4
    CIRNO = 5
    LYRICA = 6
    MERLIN = 7
    LUNASA = 8
    MYSTIA = 9
    TEWI = 10
    AYA = 11
    MEDICINE = 12
    YUUKA = 13
    KOMACHI = 14
    EIKI = 15

class Emotions(enum.Enum):
    ANNOYED = 0
    TRIUMPH = 1
    HAPPY = 2
    DISTRESS = 3
    EXCITED = 4
    SMILE = 5
    FROWN = 6
    SURPRISE = 7
    AWKWARD = 8

class MovingDirection(enum.Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


class Player:
    
    def __init__(self, character: Characters = Characters.REIMU,
                 move_speed: float = 4, focus_speed: float = 2,
                 theme: BGM = BGM.彼岸帰航) -> None:
        self.x = 0
        self.y = 0
        self.move_speed: float = move_speed
        self.focus_speed: float = focus_speed
        self.hp: int = 10
        self.p2 = False

        self.THEME = theme

        self.lesser_skill_level = 0
        self.dragon_skill_level = 0
        self.charge_level = 1 # Ranges from 0 to 4
        self.current_charge = 0

        self.character = character
        self.animation_frame = 0 # Ranges from 0 to 7 inclusive
        self.animation_timer = 0
        self.moving_direction = MovingDirection.NONE
    
    def is_player_two(self):
        self.p2 = True
        return self

    def update(self) -> None:
        
        keys = pygame.key.get_pressed()
        speed = self.focus_speed if keys[pygame.K_LSHIFT] else self.move_speed

        if keys[pygame.K_LEFT]:
            self.x -= speed
            self.moving_direction = MovingDirection.LEFT
        elif keys[pygame.K_RIGHT]:
            self.x += speed
            self.moving_direction = MovingDirection.RIGHT
        else:
            self.moving_direction = MovingDirection.NONE


        if keys[pygame.K_z]:
            self.current_charge += 0.05
            self.current_charge = min(self.current_charge, self.charge_level)
        else:
            if self.current_charge > 0:
                print(f"Released charged attack of strength {self.current_charge}")
                self.charge_level -= math.floor(self.current_charge)-1
            self.current_charge = 0
        
        if keys[pygame.K_x]:
            self.charge_level = min(self.charge_level + 0.05, 4)
        
        
        self.animation_timer += 1
        if self.animation_timer == 7:
            if self.moving_direction == MovingDirection.NONE:
                self.animation_frame = (self.animation_frame + 1) % 8
            else:
                if self.animation_frame == 7:
                    self.animation_frame -= 1
                else: 
                    self.animation_frame = (self.animation_frame + 1) % 8 
            self.animation_timer = 0
        
        if keys[pygame.K_UP]:
            self.y -= speed
        elif keys[pygame.K_DOWN]:
            self.y += speed

        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > 256: self.x = 256
        if self.y > 400: self.y = 400

    def show(self, surface: pygame.Surface) -> None:
        x = self.animation_frame * 32
        y = (self.character.value * 144) + (self.moving_direction.value * 48) + (2304 if self.p2 is True else 0)
        surface.blit(get_image("character_animations.png"), (self.x, self.y), (x, y, 32, 48))

    def shoot(self) -> None:
        pass

    def draw_portrait(self, emotion: Emotions, pos: Tuple[int, int]):
        # suffix = "_2p" if p2 is True else ""
        x, y = emotion.value * 256, self.character.value * 320 + (5120 if self.p2 is True else 0)
        # screen.blit(get_image(f"character_portraits{suffix}.png"), pos, (x, y, 256, 320))
        screen.blit(get_image(f"character_portraits.png"), pos, (x, y, 256, 320))