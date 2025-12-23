#!/usr/bin/env python3
import pygame

FRAME_RATE = 60
WINDOW_SIZE = [100, 100]


def handle_event(e):
    if e.type == pygame.JOYBUTTONDOWN:
        print('button pressed', e.button)
    if e.type == pygame.JOYAXISMOTION:
        print('axis motion', e.axis, e.value)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    joystick = pygame.joystick.Joystick(0)
    print('joystick name:', joystick.get_name())
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            handle_event(e)
        clock.tick(FRAME_RATE)


main()
