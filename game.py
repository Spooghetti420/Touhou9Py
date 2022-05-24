import pygame
import os
import time
from assets import get_image, get_sound
from campaign_scene import CampaignScene
from menu_scene import MenuScene
from players.cirno import Cirno
from window import window, screen

def preload() -> None:
    """
    Load all the game's assets.
    """
    loading_screen = pygame.transform.scale(get_image("loading.png"), (960, 720))
    flower_sprite = get_image("loading_textbox_temporary.png")

    window.blit(loading_screen, (0, 0))
    window.blit(flower_sprite, (640, 640))
    pygame.display.flip()

    for image in os.listdir("images"):
        get_image(image)
    
    for sound in os.listdir("sounds"):
        get_sound(sound)

class Game:
    frame_counter: int = 0

    @staticmethod
    def main():

        running: bool = True
        current_scene = CampaignScene(Cirno())

        # Load the game's assets
        preload()

        # Game loop begins here
        dt = 0
        while running:
            start_time = time.perf_counter()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    current_scene.on_key_pressed(event.key)
                elif event.type == pygame.KEYUP:
                    current_scene.on_key_released(event.key)

            screen.fill((0, 0, 0))
            current_scene.update(dt)

            pygame.transform.scale(screen, (window.get_width(), window.get_height()), window)

            pygame.display.flip()

            dt = time.perf_counter() - start_time
            
            # Regular 60 fps time interval is maintained
            if dt <= 1/60:
                time.sleep(1/60 - dt)

            Game.frame_counter += 1

        pygame.quit()

if __name__ == "__main__":
    Game.main()