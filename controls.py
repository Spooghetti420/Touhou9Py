from typing import Sequence
import pygame
"""
Set of utilities for managing keyboard input.
The functions will allow callers to determine whether given keys
are pressed, held, or released on the frame of calling.
In order to do so, the `update_keys` method must be called at the
beginning of each frame to actualise the current state of the
keyboard.
"""

Keylist = pygame.key.ScancodeWrapper

previous_keys: Keylist = None
current_keys: Keylist = None

def update_keys():
    global previous_keys, current_keys
    previous_keys = current_keys
    current_keys = pygame.key.get_pressed()

def is_held(keycode: int) -> bool:
    return current_keys[keycode]

def is_pressed(keycode: int) -> bool:
    return current_keys[keycode] and not previous_keys[keycode]

def is_released(keycode: int) -> bool:
    previous_keys[keycode] and not current_keys[keycode]