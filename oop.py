
from sys import exit
from typing import Any
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Stickman Life")
stickman_font = pygame.font.Font('Stickman-Regular.ttf', 75)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.stickman = [
            pygame.image.load('player copy.png').convert_alpha(),
            pygame.image.load('player1 copy.png').convert_alpha()
        ]

        self.stickman_idle = [
            pygame.image.load('player_left_idle2.png').convert_alpha(),
            pygame.image.load('player_right_idle2.png').convert_alpha()
        ]

        self.stickman_running = [

        ]

        self.index = 0
        self.image = self.stickman[self.index]

        self.rect = self.image.get_rect(topleft=(0, 0))
        self.stickman_pickup = False
        self.index2 = 0
        self.screen = 'Lobby'
        self.pickup = False

    def update(self):
        keys = pygame.key.get_pressed()

        if self.screen == 'Lobby':
            self.index2 += .015
            if self.index2 >= 2:
                self.index2 = 0
            if self.pickup:
                self.image = self.stickman[self.index]
            else:
                self.image = [self.stickman[self.index],
                              self.stickman_idle[self.index]][int(self.index2)]
            self.rect = self.image.get_rect(topleft=self.rect.topleft)


class GameState:
    def __init__(self):
        self.current_state = "Title Screen"
        self.screens = []

    def update_state(self, new_state):
        self.current_state = new_state


player = Player()
game_state = GameState()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# MOUSE CURSOR
mouse_cursor = pygame.image.load('mouse_cursor.png').convert_alpha()
mouse_cursor_rect = mouse_cursor.get_rect(center=(0, 0))

# TITLE SCREEN
title = stickman_font.render("stickman life", True, 'black')
title_rect = title.get_rect(center=(450, 400))
play_text = stickman_font.render("play", True, 'black')
play_text = pygame.transform.rotozoom(play_text, 0, .5)
play_text_rect = play_text.get_rect(center=(450, 500))
titlehead = pygame.image.load('titlehead.png').convert_alpha()
titlehead_rect = titlehead.get_rect(center=(450, 200))
play_button = pygame.image.load('play_button.png').convert_alpha()
play_button_rect = play_button.get_rect(center=(450, 500))
play_buttondown = pygame.image.load('play_buttondown.png').convert_alpha()
play_buttondown_rect = play_buttondown.get_rect(center=(450, 500))

title_screen = True
introduction = False
game_active = False
stickman_pickup = False
running_training = False
training_over = False
swimming_training = False
flying_training = False
climbing_training = False
last_training = 0
home_screen = True
training = False
racing = False
stats_screen = False
space_pressed = 0
player_gravity = 0
player_acceleration = 0
money = 50
meat_list = []
obstacle_list = []
coin_list = []
max_energy = 10
energy = max_energy
left, right = True, False
start_time = 0
score = 0
coins = 0
running_lvl, climbing_lvl, flying_lvl, swimming_lvl = 0, 0, 0, 0
climb_right = False


while True:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.rect.topleft = (500, 500)

    if title_screen:
        screen.fill('white')
        screen.blit(title, title_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(play_text, play_text_rect)
        if play_button_rect.collidepoint(mouse_pos):
            screen.blit(play_buttondown, play_buttondown_rect)
            screen.blit(play_text, play_text_rect)
        screen.blit(titlehead, titlehead_rect)

    all_sprites.update()

    all_sprites.draw(screen)

    if mouse_pos[0] < player.rect.midtop[0]-1:
        player.index = 0
    elif mouse_pos[0] > player.rect.midtop[0]+1:
        player.index = 1

    pygame.mouse.set_visible(False)
    mouse_cursor_rect.center = mouse_pos
    screen.blit(mouse_cursor, mouse_cursor_rect)
    pygame.display.update()
    clock.tick(60)
