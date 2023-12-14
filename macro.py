import keyboard
import random

tab = ['Right', 'Left', 'Up', 'Down']


def keyboard_key_event(e):
    if e.event_type == keyboard.KEY_DOWN:
        rdm = random.randint(0, 3)
        keyboard.press_and_release(tab[rdm])


keyboard.hook(keyboard_key_event)
keyboard.wait('esc')
