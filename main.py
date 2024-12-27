from sys import exit
import pygame
from random import randint


# TODO switch over to OOP for cleaner code, do when game mechanics are "finished" (still room for polishing)

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surface = stickman_font.render(
        f'Score: {int(current_time/1000)}', True, 'white')
    score_surface = pygame.transform.rotozoom(score_surface, 0, .7)
    score_rect = score_surface.get_rect(topleft=(10, 10))
    screen.blit(score_surface, score_rect)
    return int(current_time/1000)


def meat_movement(meat_list):
    if meat_list:
        for meat_rect in meat_list:
            meat_rect.y += 10
            if meat_rect.y < 515:
                screen.blit(meat, meat_rect)
            else:
                pass
        meat_list = [
            meat for meat in meat_list if meat_rect.y < 600]
        return meat_list
    else:
        return []

# TODO clean this up by adding param, that way there is one func for obstacle movement.


def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 6
            if obstacle_rect.bottom == 650:
                screen.blit(smiley_ball, obstacle_rect)
                screen.blit(pygame.transform.rotate(
                    smiley_face, -obstacle_rect.x/2), smiley_face.get_rect(center=obstacle_rect.center))
            elif obstacle_rect.bottom == 651:
                screen.blit(sad_ball, obstacle_rect)
                screen.blit(pygame.transform.rotate(
                    sad_face, -obstacle_rect.x/2), sad_face.get_rect(center=obstacle_rect.center))
            else:
                screen.blit(purple_ball, obstacle_rect)
                screen.blit(pygame.transform.rotate(
                    straight_face, -obstacle_rect.x/2), straight_face.get_rect(center=obstacle_rect.center))
        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    return []


def obstacle_movement2(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 4
            if obstacle_rect.top == 390:
                screen.blit(glacier, obstacle_rect)
            elif obstacle_rect.top == 375:
                screen.blit(boat, obstacle_rect)
            else:
                screen.blit(shark, obstacle_rect)
        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.x > -250]
        return obstacle_list
    return []


def obstacle_movement3(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.y += 4
            if obstacle_rect.x == 315:
                screen.blit(spike1, obstacle_rect)
            else:
                screen.blit(spike2, obstacle_rect)
        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.y < 750]

        return obstacle_list
    return []


def obstacle_movement4(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 3
            if obstacle_rect.width > 200:
                screen.blit(airplane, obstacle_rect)
            else:
                screen.blit(bird, obstacle_rect)

        obstacle_list = [
            obstacle for obstacle in obstacle_list if obstacle.y < 750]

        return obstacle_list
    return []


def coin_movement(coin_list, distance, direction):
    if coin_list:
        for coin_rect in coin_list:
            if direction == "W":
                coin_rect.x -= distance
            elif direction == "S":
                coin_rect.y += distance
            screen.blit(coin, coin_rect)
        coin_list = [coin for coin in coin_list if (
            coin.x > -100 and direction == "W") or (coin.y < 900 and direction == "S")]
        return coin_list
    return []


def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def coins_collisions(player, coins):
    if coins:
        for coin_rect in coins:
            if player.colliderect(coin_rect):
                coin_list.remove(coin_rect)
                return False
    return True


def stickman_animation():
    global stickman_surf, stickman_index
    if not stickman_pickup:
        stickman_index += .015
        if stickman_index >= 2:
            stickman_index = 0
        if left:
            stickman_surf = stickman_left_idle[int(stickman_index)]
        else:
            stickman_surf = stickman_right_idle[int(stickman_index)]
    else:
        if left:
            stickman_surf = stickman_left
        else:
            stickman_surf = stickman_right


def swimming_animation():
    global stickman_index, stickman_swimming_surf
    stickman_index += .05
    if stickman_index >= 2:
        stickman_index = 0
    stickman_swimming_surf = stickman_swimming[int(stickman_index)]


def flying_animation():
    global stickman_index, stickman_flying_surf
    stickman_index += .05
    if stickman_index >= 2:
        stickman_index = 0
    stickman_flying_surf = stickman_flying[int(stickman_index)]


def climbing_left_animation():
    global stickman_index, stickman_climbing_surf
    stickman_index += .03
    if stickman_index >= 2:
        stickman_index = 0
    stickman_climbing_surf = stickman_climbing[int(stickman_index)]


def climbing_right_animation():
    global stickman_index, stickman_climbing_surf
    stickman_index += .03
    if stickman_index >= 4 or stickman_index < 2:
        stickman_index = 2
    stickman_climbing_surf = stickman_climbing[int(stickman_index)]


def running_animation():
    global stickman_index, stickman_running_surf, stickman_animation_speed
    stickman_index += stickman_animation_speed
    if stickman_index >= 2:
        stickman_index = 0
    stickman_running_surf = stickman_running[int(stickman_index)]


def opp_racing_animation():
    global opp1_index, opp2_index, opp3_index, opp1_surf, opp2_surf, opp3_surf
    opp1_index += .06
    opp2_index += .08
    opp3_index += .1
    if opp1_index >= 2:
        opp1_index = 0
    if opp2_index >= 2:
        opp2_index = 0
    if opp3_index >= 2:
        opp3_index = 0

    opp1_surf = opp1_list[int(opp1_index)]
    opp2_surf = opp2_list[int(opp2_index)]
    opp3_surf = opp3_list[int(opp3_index)]


# def running_animation2():
#     global stickman_index, stickman_running_surf
#     stickman_index += .05
#     if stickman_index >= 2:
#         stickman_index = 0
#     stickman_running_surf = stickman_running[int(stickman_index)]
# def running_animation3():
#     global stickman_index, stickman_running_surf
#     stickman_index += .05
#     if stickman_index >= 2:
#         stickman_index = 0
#     stickman_running_surf = stickman_running[int(stickman_index)]
pygame.init()
screen = pygame.display.set_mode((900, 700))
clock = pygame.time.Clock()
pygame.display.set_caption("Stickman Life")
stickman_font = pygame.font.Font('Stickman-Regular.ttf', 75)

# MOUSE CURSOR
mouse_cursor = pygame.image.load('./images/mouse_cursor.png').convert_alpha()
mouse_cursor_rect = mouse_cursor.get_rect(center=(0, 0))


# TITLE SCREEN
title = stickman_font.render("stickman life", True, 'black')
title_rect = title.get_rect(center=(450, 400))
play_text = stickman_font.render("play", True, 'black')
play_text = pygame.transform.rotozoom(play_text, 0, .5)
play_text_rect = play_text.get_rect(center=(450, 500))
titlehead = pygame.image.load('./images/intro/titlehead.png').convert_alpha()
titlehead_rect = titlehead.get_rect(center=(450, 200))
play_button = pygame.image.load(
    './images/intro/play_button.png').convert_alpha()
play_button_rect = play_button.get_rect(center=(450, 500))
play_buttondown = pygame.image.load(
    './images/intro/play_buttondown.png').convert_alpha()
play_buttondown_rect = play_buttondown.get_rect(center=(450, 500))


# INTRODUCTION
continue_text = stickman_font.render("press space to continue", True, 'black')
continue_text = pygame.transform.rotozoom(continue_text, 0, .3)
continue_text_rect = continue_text.get_rect(bottomright=(890, 690))

intro1_surface = stickman_font.render(
    "you were once a successful farmer..", True, 'black')
intro1_surface = pygame.transform.rotozoom(intro1_surface, 0, .5)
intro1_rect = intro1_surface.get_rect(center=(450, 550))
intro1_scene = pygame.image.load(
    './images/intro/intro1_scene.png').convert_alpha()
intro1_scene_rect = intro1_scene.get_rect(center=(450, 275))

intro2_surface = stickman_font.render(
    "but a tornado came and destroyed everything.", True, 'black')
intro2_surface = pygame.transform.rotozoom(intro2_surface, 0, .5)
intro2_rect = intro2_surface.get_rect(center=(450, 550))
intro2_scene = pygame.image.load(
    './images/intro/intro2_scene.png').convert_alpha()
intro2_scene_rect = intro2_scene.get_rect(center=(450, 275))

intro3_surface = stickman_font.render(
    "the only thing left was a mysterious egg", True, 'black')
intro3_surface = pygame.transform.rotozoom(intro3_surface, 0, .5)
intro3_rect = intro3_surface.get_rect(center=(450, 550))
intro3_scene = pygame.image.load(
    './images/intro/intro3_scene.png').convert_alpha()
intro3_scene_rect = intro3_scene.get_rect(center=(450, 275))

intro4_surface = stickman_font.render(
    "which hatched into a stickman!", True, 'black')
intro4_surface = pygame.transform.rotozoom(intro4_surface, 0, .5)
intro4_rect = intro4_surface.get_rect(center=(450, 550))
intro4_scene = pygame.image.load(
    './images/intro/intro4_scene.png').convert_alpha()
intro4_scene_rect = intro4_scene.get_rect(center=(450, 275))

intro5_surface = stickman_font.render(
    "now you must train this stickman and race others", True, 'black')
intro5_surface = pygame.transform.rotozoom(intro5_surface, 0, .5)
intro5_rect = intro5_surface.get_rect(center=(450, 550))
intro5_scene = pygame.image.load(
    './images/intro/intro5_scene.png').convert_alpha()
intro5_scene_rect = intro5_scene.get_rect(center=(450, 275))

intro6_surface = stickman_font.render(
    "so you can earn money and rebuild the farm!", True, 'black')
intro6_surface = pygame.transform.rotozoom(intro6_surface, 0, .5)
intro6_rect = intro6_surface.get_rect(center=(450, 550))
intro6_scene = pygame.image.load(
    './images/intro/intro6_scene.png').convert_alpha()
intro6_scene_rect = intro6_scene.get_rect(center=(450, 275))


# BACKGROUND
sky = pygame.image.load('./images/sky.png').convert_alpha()
sky_rect = sky.get_rect(topleft=(0, 0))
ground = pygame.image.load('./images/ground.png').convert_alpha()
ground_rect = ground.get_rect(topleft=(0, 0))
hills = pygame.image.load('./images/hills.png').convert_alpha()
hills_rect = hills.get_rect(topleft=(0, 0))
hills_running = pygame.image.load(
    './images/training/running/running_hills.png').convert_alpha()
hills_running_rect = hills_running.get_rect(topleft=(-20, 0))
hills_running2 = pygame.image.load(
    './images/training/running/running_hills2.png').convert_alpha()
hills_running2_rect = hills_running2.get_rect(topleft=(900, 0))


# PROPS
racing_banner = pygame.image.load(
    './images/home/racing_banner.png').convert_alpha()
racing_banner_rect = racing_banner.get_rect(center=(750, 460))
racing_banner_selected = pygame.image.load(
    './images/home/racing_banner_selected.png').convert_alpha()
racing_banner_selected_rect = racing_banner_selected.get_rect(
    center=(750, 460))
gym = pygame.image.load('./images/home/gym.png').convert_alpha()
gym_rect = gym.get_rect(center=(100, 490))
gym_selected = pygame.image.load(
    './images/home/gym_selected.png').convert_alpha()
gym_selected_rect = gym_selected.get_rect(center=(100, 490))

coin_logo = pygame.image.load('./images/home/coin.png').convert_alpha()
coin_logo_rect = coin_logo.get_rect(topleft=(10, 10))

coin = pygame.image.load('./images/training/coin2.png').convert_alpha()

meat_stand = pygame.image.load(
    './images/home/mysterymeat_stand.png').convert_alpha()
meat_stand_rect = meat_stand.get_rect(topleft=(200, 460))
meat_stand_selected = pygame.image.load(
    './images/home/mysterymeat_stand_selected.png').convert_alpha()
meat_stand_selected_rect = meat_stand_selected.get_rect(topleft=(200, 460))
meat_buy_text = stickman_font.render("buy meat? ($15)", True, 'black')
meat_buy_text = pygame.transform.rotozoom(meat_buy_text, 0, .3)
meat_buy_text_rect = meat_buy_text.get_rect(center=(290, 440))
meat = pygame.image.load('./images/home/mystery_meat.png').convert_alpha()
meat = pygame.transform.rotozoom(meat, 0, .5)


# PLAYER
stickman_left = pygame.image.load(
    './images/stickman/player copy.png').convert_alpha()
stickman_rect = stickman_left.get_rect(topleft=(450, 500))
stickman_left_open = pygame.image.load(
    './images/stickman/player_left_open.png').convert_alpha()
stickman_open_rect = stickman_left_open.get_rect(topleft=(450, 500))
stickman_left2 = pygame.image.load(
    './images/stickman/player_left_idle2.png').convert_alpha()
stickman_left_idle = [stickman_left, stickman_left2]
stickman_index = 0
stickman_surf = stickman_left_idle[stickman_index]

stickman_right = pygame.image.load(
    './images/stickman/player1 copy.png').convert_alpha()
stickman_right_rect = stickman_right.get_rect(topleft=(150, 500))
stickman_right_open = pygame.image.load(
    './images/stickman/player_right_open.png').convert_alpha()
stickman_right2 = pygame.image.load(
    './images/stickman/player_right_idle2.png').convert_alpha()
stickman_right_idle = [stickman_right, stickman_right2]

stickman_swimming1 = pygame.image.load(
    './images/stickman/player_swim1.png').convert_alpha()
stickman_swimming2 = pygame.image.load(
    './images/stickman/player_swim2.png').convert_alpha()
stickman_swimming = [stickman_swimming1, stickman_swimming2]
stickman_swimming_surf = stickman_swimming[stickman_index]
stickman_swimming_rect = stickman_swimming1.get_rect(topleft=(100, 550))

stickman_flying1 = pygame.image.load(
    './images/stickman/player_fly1.png').convert_alpha()
stickman_flying2 = pygame.image.load(
    './images/stickman/player_fly2.png').convert_alpha()
stickman_flying_rect = stickman_flying1.get_rect(topleft=(300, 400))
stickman_flying = [stickman_flying1, stickman_flying2]
stickman_flying_surf = stickman_flying[stickman_index]

stickman_climbing1 = pygame.image.load(
    './images/stickman/player_climb1.png').convert_alpha()
stickman_climbing2 = pygame.image.load(
    './images/stickman/player_climb2.png').convert_alpha()
stickman_climbing3 = pygame.image.load(
    './images/stickman/player_climb3.png').convert_alpha()
stickman_climbing4 = pygame.image.load(
    './images/stickman/player_climb4.png').convert_alpha()
stickman_climbing_rect = stickman_climbing1.get_rect(topleft=(300, 400))
stickman_climbing = [stickman_climbing1, stickman_climbing2,
                     stickman_climbing3, stickman_climbing4]
stickman_climbing_surf = stickman_climbing[stickman_index]


# TRAINING MENU
training_title = stickman_font.render("training", True, 'black')
training_title_rect = training_title.get_rect(center=(450, 75))
training_instructions = stickman_font.render(
    "hover over the buttons", True, 'black')
training_instructions = pygame.transform.rotozoom(training_instructions, 0, .5)
training_instructions_rect = training_instructions.get_rect(topleft=(75, 180))
training_instructions2 = stickman_font.render("to learn more", True, 'black')
training_instructions2 = pygame.transform.rotozoom(
    training_instructions2, 0, .5)
training_instructions2_rect = training_instructions2.get_rect(
    topleft=(75, 240))
back_button = stickman_font.render("back", True, 'black')
back_button = pygame.transform.rotozoom(back_button, 0, .7)
back_button_rect = back_button.get_rect(bottomleft=(50, 670))
back_button_selected = stickman_font.render("back", True, 'gray51')
back_button_selected = pygame.transform.rotozoom(back_button_selected, 0, .7)
back_button_selected_rect = back_button_selected.get_rect(bottomleft=(50, 670))

# running
running_button = pygame.image.load(
    './images/training/training_button.png').convert_alpha()
running_button_rect = running_button.get_rect(center=(650, 200))
running_button_selected = pygame.image.load(
    './images/training/training_button_selected.png').convert_alpha()
running_button_selected_rect = running_button_selected.get_rect(
    center=(650, 200))
running_text = stickman_font.render("running", True, 'black')
running_text = pygame.transform.rotozoom(running_text, 0, .7)
running_text_rect = running_text.get_rect(center=(650, 200))
# obstacles
smiley_ball = pygame.image.load(
    './images/training/running/smiley_ball.png').convert_alpha()
smiley_face = pygame.image.load(
    './images/training/running/smiley.png').convert_alpha()
sad_ball = pygame.image.load(
    './images/training/running/sad_ball.png').convert_alpha()
sad_face = pygame.image.load(
    './images/training/running/sad_face.png').convert_alpha()
purple_ball = pygame.image.load(
    './images/training/running/purple_ball.png').convert_alpha()
straight_face = pygame.image.load(
    './images/training/running/straight_face.png').convert_alpha()
# desc
running_desc1 = stickman_font.render(
    "increase your running", True, 'black')
running_desc1 = pygame.transform.rotozoom(running_desc1, 0, .5)
running_desc1_rect = running_desc1.get_rect(topleft=(75, 180))
running_desc2 = stickman_font.render(
    "level here!", True, 'black')
running_desc2 = pygame.transform.rotozoom(running_desc2, 0, .5)
running_desc2_rect = running_desc2.get_rect(topleft=(75, 240))
running_desc3 = stickman_font.render(
    "press space to jump", True, 'black')
running_desc3 = pygame.transform.rotozoom(running_desc3, 0, .5)
running_desc3_rect = running_desc3.get_rect(topleft=(75, 320))
running_desc4 = stickman_font.render(
    "over obstacles.", True, 'black')
running_desc4 = pygame.transform.rotozoom(running_desc4, 0, .5)
running_desc4_rect = running_desc4.get_rect(topleft=(75, 380))

# swimming
swimming_button = pygame.image.load(
    './images/training/training_button.png').convert_alpha()
swimming_button_rect = swimming_button.get_rect(center=(650, 325))
swimming_button_selected = pygame.image.load(
    './images/training/training_button_selected.png').convert_alpha()
swimming_button_selected_rect = swimming_button_selected.get_rect(
    center=(650, 325))
swimming_text = stickman_font.render("swimming", True, 'black')
swimming_text = pygame.transform.rotozoom(swimming_text, 0, .7)
swimming_text_rect = swimming_text.get_rect(center=(650, 325))
# desc
swimming_desc1 = stickman_font.render(
    "increase your swimming", True, 'black')
swimming_desc1 = pygame.transform.rotozoom(swimming_desc1, 0, .5)
swimming_desc1_rect = swimming_desc1.get_rect(topleft=(75, 180))
swimming_desc2 = stickman_font.render(
    "level here!", True, 'black')
swimming_desc2 = pygame.transform.rotozoom(swimming_desc2, 0, .5)
swimming_desc2_rect = swimming_desc2.get_rect(topleft=(75, 240))
# background
ocean = pygame.image.load(
    './images/training/swimming/ocean.png').convert_alpha()
ocean_floor = pygame.image.load(
    './images/training/swimming/ocean_floor.png').convert_alpha()
ocean_background = pygame.image.load(
    './images/training/swimming/ocean_background.png').convert_alpha()
ocean_rect = ocean.get_rect(topleft=(0, 441))
ocean_floor_rect1 = ocean_floor.get_rect(topleft=(0, 441))
ocean_floor_rect2 = ocean_floor.get_rect(topleft=(902, 441))
ocean_background_rect = ocean_background.get_rect(topleft=(0, 441))
# obstacles
glacier = pygame.image.load(
    './images/training/swimming/glacier.png').convert_alpha()
glacier_rect = glacier.get_rect(topleft=(450, 390))
boat = pygame.image.load('./images/training/swimming/boat.png').convert_alpha()
boat_rect = boat.get_rect(topleft=(450, 375))
shark = pygame.image.load(
    './images/training/swimming/shark.png').convert_alpha()
shark_rect = shark.get_rect(topleft=(300, 450))

# flying
flying_button = pygame.image.load(
    './images/training/training_button.png').convert_alpha()
flying_button_rect = flying_button.get_rect(center=(650, 450))
flying_button_selected = pygame.image.load(
    './images/training/training_button_selected.png').convert_alpha()
flying_button_selected_rect = flying_button_selected.get_rect(
    center=(650, 450))
flying_text = stickman_font.render("flying", True, 'black')
flying_text = pygame.transform.rotozoom(flying_text, 0, .7)
flying_text_rect = flying_text.get_rect(center=(650, 450))
# desc
flying_desc1 = stickman_font.render(
    "increase your flying", True, 'black')
flying_desc1 = pygame.transform.rotozoom(flying_desc1, 0, .5)
flying_desc1_rect = flying_desc1.get_rect(topleft=(75, 180))
flying_desc2 = stickman_font.render(
    "level here!", True, 'black')
flying_desc2 = pygame.transform.rotozoom(flying_desc2, 0, .5)
flying_desc2_rect = flying_desc2.get_rect(topleft=(75, 240))
# background
flying_background = pygame.image.load(
    './images/training/flying/flying_background.png').convert_alpha()
flying_background_rect = flying_background.get_rect(topleft=(0, 0))
clouds = pygame.image.load(
    './images/training/flying/clouds.png').convert_alpha()
clouds_rect1 = clouds.get_rect(topleft=(0, 0))
clouds_rect2 = clouds.get_rect(topleft=(900, 0))
# obstacles
airplane = pygame.image.load(
    './images/training/flying/airplane.png').convert_alpha()
airplane_rect = airplane.get_rect()
bird = pygame.image.load('./images/training/flying/bird.png').convert_alpha()
bird_rect = bird.get_rect()

# climbing
climbing_button = pygame.image.load(
    './images/training/training_button.png').convert_alpha()
climbing_button_rect = climbing_button.get_rect(center=(650, 575))
climbing_button_selected = pygame.image.load(
    './images/training/training_button_selected.png').convert_alpha()
climbing_button_selected_rect = climbing_button_selected.get_rect(
    center=(650, 575))
climbing_text = stickman_font.render("climbing", True, 'black')
climbing_text = pygame.transform.rotozoom(climbing_text, 0, .7)
climbing_text_rect = climbing_text.get_rect(center=(650, 575))
# desc
climbing_desc1 = stickman_font.render(
    "increase your climbing", True, 'black')
climbing_desc1 = pygame.transform.rotozoom(climbing_desc1, 0, .5)
climbing_desc1_rect = climbing_desc1.get_rect(topleft=(75, 180))
climbing_desc2 = stickman_font.render(
    "level here!", True, 'black')
climbing_desc2 = pygame.transform.rotozoom(climbing_desc2, 0, .5)
climbing_desc2_rect = climbing_desc2.get_rect(topleft=(75, 240))
# background
climbing_background1 = pygame.image.load(
    './images/training/climbing/climbing_background1.png').convert_alpha()
climbing_background2 = pygame.image.load(
    './images/training/climbing/climbing_background2.png').convert_alpha()
climbing_background3 = pygame.image.load(
    './images/training/climbing/climbing_background3.png').convert_alpha()
climbing_walls = pygame.image.load(
    './images/training/climbing/climbing_walls.png').convert_alpha()
blue_background = pygame.image.load(
    './images/blue_background.png').convert_alpha()
climbing_background1_rect = climbing_background1.get_rect(topleft=(0, 0))
climbing_background2_rect = climbing_background2.get_rect(topleft=(0, -700))
climbing_background3_rect = climbing_background3.get_rect(topleft=(0, -1400))
climbing_walls_rect = climbing_walls.get_rect(topleft=(0, 0))
blue_background_rect = blue_background.get_rect(topleft=(0, 0))
# obstacles
spike1 = pygame.image.load(
    './images/training/climbing/spike.png').convert_alpha()
spike2 = pygame.image.load(
    './images/training/climbing/spike2.png').convert_alpha()

# TRAINING RESULTS
training_results_title = stickman_font.render(
    'training results', True, 'black')
training_results_title_rect = training_results_title.get_rect(center=(450, 75))
training_results_coins = stickman_font.render(
    'coins:', True, 'black')
training_results_coins = pygame.transform.rotozoom(
    training_results_coins, 0, .7)
training_results_coins_rect = training_results_coins.get_rect(
    topleft=(100, 400))
training_results_score = stickman_font.render(
    'score:', True, 'black')
training_results_score = pygame.transform.rotozoom(
    training_results_score, 0, .7)
training_results_score_rect = training_results_score.get_rect(
    topleft=(100, 200))
retry_button = stickman_font.render('retry', True, 'black')
retry_button = pygame.transform.rotozoom(retry_button, 0, .7)
retry_button_rect = retry_button.get_rect(bottomright=(850, 670))
retry_button_selected = stickman_font.render('retry', True, 'gray51')
retry_button_selected = pygame.transform.rotozoom(retry_button_selected, 0, .7)
retry_button_selected_rect = retry_button_selected.get_rect(
    bottomright=(850, 670))

# STATS MENU
stats_button = pygame.image.load('./images/home/trophy.png').convert_alpha()
stats_button_rect = stats_button.get_rect(topleft=(840, 10))
stats_button_selected = pygame.image.load(
    './images/home/trophy_selected.png').convert_alpha()
stats_button_selected_rect = stats_button_selected.get_rect(topleft=(840, 10))
stats_title = stickman_font.render('stats', True, 'black')
stats_text = pygame.transform.rotozoom(stats_title, 0, .3)
stats_text_rect = stats_text.get_rect(topleft=(840, 65))
stats_title_rect = stats_title.get_rect(center=(450, 75))
running_bar_rect = pygame.Rect(100, 225, 300, 50)
flying_bar_rect = pygame.Rect(100, 450, 300, 50)
swimming_bar_rect = pygame.Rect(475, 225, 300, 50)
climbing_bar_rect = pygame.Rect(475, 450, 300, 50)

# RACING MENU

races_text = stickman_font.render('races', True, 'black')
races_text_rect = races_text.get_rect(center=(450, 75))
races_map = pygame.image.load('./images/racing/races_map.png').convert_alpha()
races_map_rect = races_map.get_rect(topleft=(0, 0))
races_circle = pygame.image.load(
    './images/racing/races_circle.png').convert_alpha()
races_circle_rect1 = races_circle.get_rect(center=(129, 426))
races_circle_rect2 = races_circle.get_rect(center=(252, 375))
races_circle_rect3 = races_circle.get_rect(center=(381, 413))
races_circle_rect4 = races_circle.get_rect(center=(494, 327))
races_circle_rect5 = races_circle.get_rect(center=(616, 377))
races_circle_selected = pygame.image.load(
    './images/racing/races_circle_selected.png').convert_alpha()
races_trophy = pygame.image.load(
    './images/racing/races_trophy.png').convert_alpha()
races_trophy_rect = races_trophy.get_rect(center=(714, 321))
races_stickman = pygame.transform.rotozoom(stickman_right, 0, .7)
races_stickman_rect = races_stickman.get_rect(bottomleft=(115, 426))
races_click = stickman_font.render('click to start', True, 'black')
races_click = pygame.transform.rotozoom(races_click, 0, .3)
races_click_rect = races_click.get_rect(topleft=(105, 460))

races_podium = pygame.image.load(
    './images/racing/racing_podium.png').convert_alpha()
races_podium_rect = races_podium.get_rect(topleft=(220, 300))

skip_text = stickman_font.render('skip', True, 'black')
skip_text = pygame.transform.rotozoom(skip_text, 0, .35)
skip_text_selected = stickman_font.render('skip', True, 'gray51')
skip_text_selected = pygame.transform.rotozoom(skip_text_selected, 0, .35)

skip_text_selected_rect = skip_text_selected.get_rect(topleft=(50, 650))

skip_text_rect = skip_text.get_rect(topleft=(50, 650))

# racing opps

opp1_index = 0
opp2_index = 0
opp3_index = 0

opp1_idle = pygame.image.load(
    './images/stickman/opp1_idle.png').convert_alpha()
opp1_run1 = pygame.image.load(
    './images/stickman/opp1_run1.png').convert_alpha()
opp1_run2 = pygame.image.load(
    './images/stickman/opp1_run2.png').convert_alpha()
opp2_idle = pygame.image.load(
    './images/stickman/opp2_idle.png').convert_alpha()
opp2_run1 = pygame.image.load(
    './images/stickman/opp2_run1.png').convert_alpha()
opp2_run2 = pygame.image.load(
    './images/stickman/opp2_run2.png').convert_alpha()
opp3_idle = pygame.image.load(
    './images/stickman/opp3_idle.png').convert_alpha()
opp3_run1 = pygame.image.load(
    './images/stickman/opp3_run1.png').convert_alpha()
opp3_run2 = pygame.image.load(
    './images/stickman/opp3_run2.png').convert_alpha()

opp1_idle_rect = opp1_idle.get_rect(topleft=(100, 480))
opp2_idle_rect = opp2_idle.get_rect(topleft=(100, 460))
opp3_idle_rect = opp3_idle.get_rect(topleft=(100, 440))
opp1_pos = opp1_idle_rect.x
opp2_pos = opp2_idle_rect.x
opp3_pos = opp3_idle_rect.x

stickman_racing_pos = 0

opp1_surf = opp1_idle
opp2_surf = opp2_idle
opp3_surf = opp3_idle

opp1_list = [opp1_run1, opp1_run2]
opp2_list = [opp2_run1, opp2_run2]
opp3_list = [opp3_run1, opp3_run2]

stickman_animation_speed = 0.05
stickman_speed = 0
racing_end_banner = pygame.transform.rotozoom(
    racing_banner, 0, 1.5)
racing_end_banner_rect = racing_end_banner.get_rect(center=(450, 350))
# race 1
stickman_right_run1 = pygame.image.load(
    './images/stickman/player_right_run1.png').convert_alpha()
stickman_right_run2 = pygame.image.load(
    './images/stickman/player_right_run2.png').convert_alpha()
stickman_running = [stickman_right_run1, stickman_right_run2]
stickman_running_surf = stickman_right
# desc
race1_desc1 = stickman_font.render(
    'race for noobs.', True, 'black')
race1_desc1 = pygame.transform.rotozoom(race1_desc1, 0, .4)
race1_desc_rect1 = race1_desc1.get_rect(topleft=(350, 550))

race1_desc2 = stickman_font.render(
    'if you lose racing might not be for you...', True, 'black')
race1_desc2 = pygame.transform.rotozoom(race1_desc2, 0, .4)
race1_desc_rect2 = race1_desc1.get_rect(topleft=(350, 600))

race_result = []
opp1_finish = False
opp2_finish = False
opp3_finish = False
stickman_finish = False

# end
races_lose = stickman_font.render('you lost', True, 'black')
races_lose_rect = races_lose.get_rect(center=(450, 100))
races_win = stickman_font.render('you won', True, 'black')
races_win_rect = races_win.get_rect(center=(450, 100))
title_screen = False
introduction = False
game_active = True
stickman_pickup = False
running_training = False
training_over = False
swimming_training = False
flying_training = False
climbing_training = False
last_training = 0
home_screen = False
training = False
racing = True
stats_screen = False
space_pressed = 0
player_gravity = 0
player_acceleration = 0
money = 50
meat_list = []
obstacle_list = []
coin_list = []
# max en start 10
max_energy = 50
energy = max_energy
left, right = True, False
start_time = 0
score = 0
coins = 0
running_lvl, climbing_lvl, flying_lvl, swimming_lvl = 0, 0, 0, 0
climb_right = False
race1, race2, race3, race4, race5 = False, False, False, False, False
pause = True
current_race = 1
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1200)

obstacle_timer2 = pygame.USEREVENT + 3
pygame.time.set_timer(obstacle_timer2, 2000)

obstacle_timer3 = pygame.USEREVENT + 4
pygame.time.set_timer(obstacle_timer3, 1500)

obstacle_timer4 = pygame.USEREVENT + 5
pygame.time.set_timer(obstacle_timer4, 2000)

coin_timer = pygame.USEREVENT + 2
pygame.time.set_timer(coin_timer, 2000)


while True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if title_screen and play_buttondown_rect.collidepoint(mouse_pos):
                title_screen, introduction = False, True
            if home_screen:
                if stickman_rect.collidepoint(mouse_pos) and not meat_list:
                    stickman_pickup = True
                elif gym_selected_rect.collidepoint(mouse_pos) and not meat_list:
                    training, home_screen = True, False
                elif meat_stand_selected_rect.collidepoint(mouse_pos) and money >= 15:
                    meat_list.append(meat.get_rect(
                        topleft=(stickman_rect.x, -50)))
                    money -= 15
                    max_energy += 2
                    energy = max_energy
                elif stats_button_selected_rect.collidepoint(mouse_pos) and not meat_list:
                    stats_screen = True
                elif stats_screen and back_button_selected_rect.collidepoint(mouse_pos):
                    stats_screen = False
                elif racing_banner_selected_rect.collidepoint(mouse_pos):
                    racing, home_screen = True, False
            elif training:
                if running_button_selected_rect.collidepoint(mouse_pos):
                    start_time = pygame.time.get_ticks()
                    running_training, training = True, False
                    stickman_right_rect.y = 500
                    stickman_right_rect.x = 150
                    obstacle_list = []
                    coin_list = []
                elif swimming_button_selected_rect.collidepoint(mouse_pos):
                    start_time = pygame.time.get_ticks()
                    swimming_training, training = True, False
                    stickman_right_rect.y = 500
                    stickman_right_rect.x = 150
                    obstacle_list = []
                    coin_list = []
                elif flying_button_selected_rect.collidepoint(mouse_pos):
                    start_time = pygame.time.get_ticks()
                    stickman_right_rect.y = 500
                    stickman_right_rect.x = 150
                    obstacle_list = []
                    coin_list = []
                    flying_training, training = True, False
                elif climbing_button_selected_rect.collidepoint(mouse_pos):
                    start_time = pygame.time.get_ticks()
                    stickman_right_rect.x = 315
                    stickman_right_rect.y = 150
                    obstacle_list = []
                    coin_list = []
                    climbing_training, training = True, False
                elif back_button_selected_rect.collidepoint(mouse_pos):
                    training, home_screen = False, True
            elif training_over:
                if back_button_selected_rect.collidepoint(mouse_pos):
                    money += coins * 5
                    coins = 0
                    training_over, training = False, True
                    if last_training == 1:
                        running_training = False
                    elif last_training == 2:
                        flying_training = False
                    elif last_training == 3:
                        swimming_training = False
                    else:
                        climbing_training = False
                        climb_right = False
                elif retry_button_selected_rect.collidepoint(mouse_pos):
                    training_over = False
                    money += coins * 5
                    coins = 0
                    if last_training == 1:
                        start_time = pygame.time.get_ticks()
                        stickman_right_rect.y = 500
                        stickman_right_rect.x = 150
                        obstacle_list = []
                        coin_list = []
                        running_training = True
                    elif last_training == 2:
                        start_time = pygame.time.get_ticks()
                        stickman_right_rect.y = 500
                        stickman_right_rect.x = 150
                        obstacle_list = []
                        coin_list = []
                        flying_training = True
                    elif last_training == 3:
                        start_time = pygame.time.get_ticks()
                        stickman_right_rect.y = 750
                        stickman_right_rect.x = 500
                        obstacle_list = []
                        coin_list = []
                        swimming_training = True
                    else:
                        start_time = pygame.time.get_ticks()
                        obstacle_list = []
                        coin_list = []
                        stickman_right_rect.x = 315
                        stickman_right_rect.y = 150
                        climb_right = False
                        climbing_training = True
                    last_training = 0

            elif racing:
                if back_button_selected_rect.collidepoint(mouse_pos):
                    racing, home_screen = False, True
                    race1, race2, race3, race4, race5 = False, False, False, False, False
                elif races_circle_rect1.collidepoint(mouse_pos) and current_race == 1:
                    stickman_right_rect.x = 100
                    stickman_right_rect.y = 500
                    stickman_running_surf = stickman_right

                    opp1_idle_rect.topleft = (100, 480)
                    opp2_idle_rect.topleft = (100, 460)
                    opp3_idle_rect.topleft = (100, 440)
                    opp1_pos = opp1_idle_rect.x
                    opp2_pos = opp2_idle_rect.x
                    opp3_pos = opp3_idle_rect.x
                    opp1_surf = opp1_idle
                    opp2_surf = opp2_idle
                    opp3_surf = opp3_idle
                    stickman_racing_pos = stickman_right_rect.x
                    stickman_finish = False
                    opp1_finish = False
                    race1 = True
                    race_result = []
                    stickman_animation_speed = int(running_lvl) * 0.007 + 0.05
                    stickman_speed = int(running_lvl) * 0.1
                    start_time = pygame.time.get_ticks()
                elif races_circle_rect2.collidepoint(mouse_pos) and current_race == 2:
                    race2 = True
                elif races_circle_rect3.collidepoint(mouse_pos) and current_race == 3:
                    race3 = True
                elif races_circle_rect4.collidepoint(mouse_pos) and current_race == 4:
                    race4 = True
                elif races_circle_rect5.collidepoint(mouse_pos) and current_race == 5:
                    race5 = True
                elif skip_text_selected_rect.collidepoint(mouse_pos):
                    countdown = 23

        if event.type == pygame.MOUSEBUTTONUP:
            if stickman_pickup:
                stickman_pickup = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if introduction:
                    space_pressed += 1
                if running_training and stickman_right_rect.y == 500:
                    player_gravity = -22
                    player_acceleration = 11
            if event.key == pygame.K_a:
                if climbing_training and stickman_climbing_rect.x >= 550:
                    climb_right = False
            if event.key == pygame.K_d:
                if climbing_training and stickman_climbing_rect.x <= 300:
                    climb_right = True
        if event.type == obstacle_timer:
            if running_training:
                obstacle_list.append(smiley_ball.get_rect(
                    midbottom=(randint(1100, 1300), randint(650, 652))))
        if event.type == obstacle_timer2:
            if swimming_training:
                if randint(0, 1):
                    obstacle_list.append(shark.get_rect(
                        topleft=(randint(920, 1000), randint(450, 600))))
                elif randint(0, 1):
                    obstacle_list.append(glacier.get_rect(
                        topleft=(randint(920, 1000), 390)))
                else:
                    obstacle_list.append(boat.get_rect(
                        topleft=(randint(920, 1000), 375)))
        if event.type == obstacle_timer3:
            if climbing_training:
                if randint(0, 1):
                    obstacle_list.append(spike1.get_rect(
                        topleft=(315, randint(-100, -50))))
                else:
                    obstacle_list.append(spike2.get_rect(
                        topleft=(538, randint(-100, -50))))
        if event.type == obstacle_timer4:
            if flying_training:
                if randint(0, 1):
                    obstacle_list.append(bird.get_rect(
                        topleft=(randint(900, 1000), randint(100, 600))))
                else:
                    obstacle_list.append(airplane.get_rect(
                        topleft=(randint(900, 1000), randint(100, 600))))

        if event.type == coin_timer:
            if running_training:
                coin_list.append(coin.get_rect(
                    center=(randint(1100, 1300), randint(300, 600))))
            elif swimming_training:
                coin_list.append(coin.get_rect(
                    center=(randint(1100, 1300), randint(550, 700))))
            elif flying_training:
                coin_list.append(coin.get_rect(
                    center=(randint(900, 1000), randint(100, 600))))
            elif climbing_training:
                coin_list.append(coin.get_rect(
                    center=(randint(300, 600), randint(-150, -50))))

    if title_screen:
        screen.fill('white')
        screen.blit(title, title_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(play_text, play_text_rect)
        if play_button_rect.collidepoint(mouse_pos):
            screen.blit(play_buttondown, play_buttondown_rect)
            screen.blit(play_text, play_text_rect)
        screen.blit(titlehead, titlehead_rect)
    if introduction:
        if not space_pressed:
            screen.fill('white')
            screen.blit(intro1_surface, intro1_rect)
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro1_scene, intro1_scene_rect)
        elif space_pressed == 1:
            screen.fill('white')
            screen.blit(intro2_surface, intro2_rect)
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro2_scene, intro2_scene_rect)
        elif space_pressed == 2:
            screen.fill('white')
            screen.blit(intro3_surface, intro3_rect)
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro3_scene, intro3_scene_rect)
        elif space_pressed == 3:
            screen.fill('white')
            screen.blit(intro4_surface, intro4_rect)
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro4_scene, intro4_scene_rect)
        elif space_pressed == 4:
            screen.fill('white')
            screen.blit(intro5_surface, intro5_rect)
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro5_scene, intro5_scene_rect)
        elif space_pressed == 5:
            screen.fill('white')
            screen.blit(continue_text, continue_text_rect)
            screen.blit(intro6_surface, intro6_rect)
            screen.blit(intro6_scene, intro6_scene_rect)
        else:
            game_active, home_screen, introduction = True, True, False
    if game_active:
        if home_screen:
            # BACKGROUND
            screen.blit(sky, sky_rect)
            screen.blit(hills, hills_rect)
            screen.blit(ground, ground_rect)

            # PROPS
            screen.blit(stats_button, stats_button_rect)
            if stats_button_rect.collidepoint(mouse_pos) and not stickman_pickup and not meat_list:
                screen.blit(stats_button_selected, stats_button_selected_rect)
                screen.blit(stats_text, stats_text_rect)
            screen.blit(racing_banner, racing_banner_rect)
            if racing_banner_rect.collidepoint(mouse_pos) and not stickman_pickup and not meat_list:
                screen.blit(racing_banner_selected,
                            racing_banner_selected_rect)
            screen.blit(gym, gym_rect)
            if gym_rect.collidepoint(mouse_pos) and not stickman_pickup and not meat_list:
                screen.blit(gym_selected, gym_selected_rect)
            screen.blit(coin_logo, coin_logo_rect)
            money_surface = stickman_font.render(str(money), True, 'white')
            money_surface = pygame.transform.rotozoom(money_surface, 0, .6)
            money_surface_rect = money_surface.get_rect(topleft=(70, 13))
            screen.blit(money_surface, money_surface_rect)
            screen.blit(meat_stand, meat_stand_rect)
            if meat_stand_rect.collidepoint(mouse_pos) and not stickman_pickup:
                screen.blit(meat_stand_selected, meat_stand_selected_rect)
                screen.blit(meat_buy_text, meat_buy_text_rect)
            meat_list = meat_movement(meat_list)
            energy_text = stickman_font.render(
                f"max energy: {max_energy}", True, 'black')
            energy_text = pygame.transform.rotozoom(energy_text, 0, .35)

            energy_text_rect = energy_text.get_rect(topleft=(710, 650))
            screen.blit(energy_text, energy_text_rect)
            # PLAYER
            stickman_animation()
            if meat_list:
                stickman_open_rect.x = stickman_rect.x
                stickman_open_rect.y = stickman_rect.y
                if mouse_pos[0] < stickman_rect.midtop[0]:
                    screen.blit(stickman_left_open, stickman_open_rect)
                else:
                    screen.blit(stickman_right_open, stickman_open_rect)
            else:
                if mouse_pos[0] < stickman_rect.midtop[0]-1:
                    left, right = True, False
                elif mouse_pos[0] > stickman_rect.midtop[0]+1:
                    right, left = True, False
                screen.blit(stickman_surf, stickman_rect)

            if stickman_pickup:
                stickman_rect.x, stickman_rect.y = mouse_pos
                stickman_rect.x -= 25
                stickman_rect.y -= 75
            else:
                player_gravity += 1
                stickman_rect.y += player_gravity

            if stickman_rect.y > 500:
                player_gravity = 0
                stickman_rect.y = 500
            if stats_screen:
                running_stat = stickman_font.render(
                    f"running: {int(running_lvl)}", True, 'black')
                running_stat = pygame.transform.rotozoom(running_stat, 0, .7)
                running_stat_rect = running_stat.get_rect(topleft=(100, 150))
                swimming_stat = stickman_font.render(
                    f"swimming: {int(swimming_lvl)}", True, 'black')
                swimming_stat = pygame.transform.rotozoom(swimming_stat, 0, .7)
                swimming_stat_rect = swimming_stat.get_rect(topleft=(475, 150))
                climbing_stat = stickman_font.render(
                    f"climbing: {int(climbing_lvl)}", True, 'black')
                climbing_stat = pygame.transform.rotozoom(climbing_stat, 0, .7)
                climbing_stat_rect = climbing_stat.get_rect(topleft=(475, 375))
                flying_stat = stickman_font.render(
                    f"flying: {int(flying_lvl)}", True, 'black')
                flying_stat = pygame.transform.rotozoom(flying_stat, 0, .7)
                flying_stat_rect = flying_stat.get_rect(topleft=(100, 375))

                screen.fill('white')
                screen.blit(back_button, back_button_rect)
                screen.blit(stats_title, stats_title_rect)
                screen.blit(running_stat, running_stat_rect)
                screen.blit(climbing_stat, climbing_stat_rect)
                screen.blit(flying_stat, flying_stat_rect)
                screen.blit(swimming_stat, swimming_stat_rect)

                pygame.draw.rect(
                    screen, 'lightgoldenrod', pygame.Rect(100, 225, (running_lvl-int(running_lvl)) * 300, 50), 0, border_bottom_left_radius=15, border_top_left_radius=15)
                pygame.draw.rect(
                    screen, 'lightgoldenrod', pygame.Rect(100, 450, (flying_lvl-int(flying_lvl)) * 300, 50), 0, border_bottom_left_radius=15, border_top_left_radius=15)
                pygame.draw.rect(
                    screen, 'lightgoldenrod', pygame.Rect(475, 225, (swimming_lvl-int(swimming_lvl)) * 300, 50), 0, border_bottom_left_radius=15, border_top_left_radius=15)
                pygame.draw.rect(
                    screen, 'lightgoldenrod', pygame.Rect(475, 450, (climbing_lvl-int(climbing_lvl)) * 300, 50), 0, border_bottom_left_radius=15, border_top_left_radius=15)
                pygame.draw.rect(
                    screen, 'black', running_bar_rect, 5, 15)
                pygame.draw.rect(
                    screen, 'black', flying_bar_rect, 5, 15)
                pygame.draw.rect(
                    screen, 'black', swimming_bar_rect, 5, 15)
                pygame.draw.rect(
                    screen, 'black', climbing_bar_rect, 5, 15)

                if running_bar_rect.collidepoint(mouse_pos):
                    running_percent = stickman_font.render(
                        f"{int((running_lvl-int(running_lvl))*100)}%", True, 'black')
                    running_percent = pygame.transform.rotozoom(
                        running_percent, 0, .5)
                    running_percent_rect = running_percent.get_rect(
                        center=(250, 250))
                    screen.blit(running_percent, running_percent_rect)

                if flying_bar_rect.collidepoint(mouse_pos):
                    flying_percent = stickman_font.render(
                        f"{int((flying_lvl-int(flying_lvl))*100)}%", True, 'black')
                    flying_percent = pygame.transform.rotozoom(
                        flying_percent, 0, .5)
                    flying_percent_rect = flying_percent.get_rect(
                        center=(250, 475))
                    screen.blit(flying_percent, flying_percent_rect)

                if swimming_bar_rect.collidepoint(mouse_pos):
                    swimming_percent = stickman_font.render(
                        f"{int((swimming_lvl-int(swimming_lvl))*100)}%", True, 'black')
                    swimming_percent = pygame.transform.rotozoom(
                        swimming_percent, 0, .5)
                    swimming_percent_rect = swimming_percent.get_rect(
                        center=(625, 250))
                    screen.blit(swimming_percent, swimming_percent_rect)

                if climbing_bar_rect.collidepoint(mouse_pos):
                    climbing_percent = stickman_font.render(
                        f"{int((climbing_lvl-int(climbing_lvl))*100)}%", True, 'black')
                    climbing_percent = pygame.transform.rotozoom(
                        climbing_percent, 0, .5)
                    climbing_percent_rect = climbing_percent.get_rect(
                        center=(625, 475))
                    screen.blit(climbing_percent, climbing_percent_rect)

                if back_button_rect.collidepoint(mouse_pos):
                    screen.blit(back_button_selected,
                                back_button_selected_rect)

        # TRAINING
        if training:
            screen.fill('white')
            screen.blit(training_title, training_title_rect)
            screen.blit(training_instructions, training_instructions_rect)
            screen.blit(training_instructions2, training_instructions2_rect)
            screen.blit(back_button, back_button_rect)
            screen.blit(running_button, running_button_rect)
            screen.blit(running_text, running_text_rect)
            screen.blit(swimming_button, swimming_button_rect)
            screen.blit(swimming_text, swimming_text_rect)
            screen.blit(flying_button, flying_button_rect)
            screen.blit(flying_text, flying_text_rect)
            screen.blit(climbing_button, climbing_button_rect)
            screen.blit(climbing_text, climbing_text_rect)

            if back_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'white', back_button_rect)
                screen.blit(back_button_selected, back_button_selected_rect)

            if running_button_rect.collidepoint((mouse_pos)):
                pygame.draw.rect(screen, 'white', training_instructions_rect)
                pygame.draw.rect(screen, 'white', training_instructions2_rect)
                screen.blit(running_button_selected,
                            running_button_selected_rect)
                screen.blit(running_text, running_text_rect)
                screen.blit(running_desc1, running_desc1_rect)
                screen.blit(running_desc2, running_desc2_rect)
                screen.blit(running_desc3, running_desc3_rect)
                screen.blit(running_desc4, running_desc4_rect)

            if swimming_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'white', training_instructions_rect)
                pygame.draw.rect(screen, 'white', training_instructions2_rect)
                screen.blit(swimming_button_selected,
                            swimming_button_selected_rect)
                screen.blit(swimming_text, swimming_text_rect)
                screen.blit(swimming_desc1, swimming_desc1_rect)
                screen.blit(swimming_desc2, swimming_desc2_rect)

            if flying_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'white', training_instructions_rect)
                pygame.draw.rect(screen, 'white', training_instructions2_rect)
                screen.blit(flying_button_selected,
                            flying_button_selected_rect)
                screen.blit(flying_text, flying_text_rect)
                screen.blit(flying_desc1, flying_desc1_rect)
                screen.blit(flying_desc2, flying_desc2_rect)

            if climbing_button_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, 'white', training_instructions_rect)
                pygame.draw.rect(screen, 'white', training_instructions2_rect)
                screen.blit(climbing_button_selected,
                            climbing_button_selected_rect)
                screen.blit(climbing_text, climbing_text_rect)
                screen.blit(climbing_desc1, climbing_desc1_rect)
                screen.blit(climbing_desc2, climbing_desc2_rect)

        if running_training:

            # BACKGROUND
            screen.blit(sky, sky_rect)
            screen.blit(hills_running, hills_running_rect)
            screen.blit(hills_running2, hills_running2_rect)
            screen.blit(ground, ground_rect)
            score = display_score()

            hills_running_rect.x -= 3
            hills_running2_rect.x -= 3
            if hills_running_rect.x < -920:
                hills_running_rect.x = 880
            if hills_running2_rect.x < -900:
                hills_running2_rect.x = 900

            coin_list = coin_movement(coin_list, 4, "W")
            if not coins_collisions(stickman_right_rect, coin_list):
                coins += 1

            # PLAYER

            screen.blit(stickman_right, stickman_right_rect)

            player_gravity += 1
            stickman_right_rect.y += player_gravity

            player_acceleration -= .2
            stickman_right_rect.x += player_acceleration
            stickman_right_rect.x -= 3

            if stickman_right_rect.y > 500:
                stickman_right_rect.y = 500
                player_acceleration = 0

            if stickman_right_rect.x < -50:
                running_lvl += score/(5*(running_lvl+1))
                training_over = True
                running_training = False
                last_training = 1

            if stickman_right_rect.x > 800:
                stickman_right_rect.x = 800

            obstacle_list = obstacle_movement(obstacle_list)

            if not collisions(stickman_right_rect, obstacle_list):
                running_lvl += score/(5*(running_lvl+1))
                training_over = True
                running_training = False
                last_training = 1

        if swimming_training:
            keys = pygame.key.get_pressed()
            screen.fill('white')
            screen.blit(sky, sky_rect)
            screen.blit(ocean_background, ocean_background_rect)
            score = display_score()

            ocean_floor_rect1.x -= 3
            if ocean_floor_rect1.x < -900:
                ocean_floor_rect1.x = 900
            ocean_floor_rect2.x -= 3
            if ocean_floor_rect2.x < -900:
                ocean_floor_rect2.x = 902
            screen.blit(ocean_floor, ocean_floor_rect1)
            screen.blit(ocean_floor, ocean_floor_rect2)
            coin_list = coin_movement(coin_list, 4, "W")
            if not coins_collisions(stickman_swimming_rect, coin_list):
                coins += 1
            swimming_animation()
            screen.blit(stickman_swimming_surf, stickman_swimming_rect)
            if keys[pygame.K_w] and stickman_swimming_rect.y > 420:
                stickman_swimming_rect.y -= 3
            if keys[pygame.K_s] and stickman_swimming_rect.y < 650:
                stickman_swimming_rect.y += 3
            obstacle_list = obstacle_movement2(obstacle_list)
            screen.blit(ocean, ocean_rect)

            if not collisions(stickman_swimming_rect, obstacle_list):
                swimming_lvl += score/(5*(swimming_lvl+1))
                training_over = True
                swimming_training = False
                last_training = 3

        if flying_training:
            keys = pygame.key.get_pressed()
            screen.fill('white')
            screen.blit(flying_background, flying_background_rect)
            score = display_score()
            screen.blit(clouds, clouds_rect1)
            screen.blit(clouds, clouds_rect2)
            clouds_rect1.x -= 3
            clouds_rect2.x -= 3
            if clouds_rect1.x < -1850:
                clouds_rect1.x = randint(900, 1000)
            if clouds_rect2.x < -1850:
                clouds_rect2.x = randint(900, 1000)
            flying_animation()
            coin_list = coin_movement(coin_list, 3, "W")
            if not coins_collisions(stickman_flying_rect, coin_list):
                coins += 1
            screen.blit(stickman_flying_surf, stickman_flying_rect)
            if keys[pygame.K_w] and stickman_flying_rect.y > 20:
                stickman_flying_rect.y -= 3
            if keys[pygame.K_s] and stickman_flying_rect.y < 600:
                stickman_flying_rect.y += 3
            if keys[pygame.K_a] and stickman_flying_rect.x > 20:
                stickman_flying_rect.x -= 3
            if keys[pygame.K_d] and stickman_flying_rect.x < 700:
                stickman_flying_rect.x += 3
            obstacle_list = obstacle_movement4(obstacle_list)
            if not collisions(stickman_flying_rect, obstacle_list):
                flying_lvl += score/(5*(flying_lvl+1))
                training_over = True
                flying_training = False
                last_training = 2

        if climbing_training:
            keys = pygame.key.get_pressed()
            screen.blit(blue_background, blue_background_rect)
            if climbing_background1_rect.y < 700:
                screen.blit(climbing_background1, climbing_background1_rect)
            screen.blit(climbing_background2, climbing_background2_rect)
            screen.blit(climbing_background3, climbing_background3_rect)
            climbing_background1_rect.y += 3
            climbing_background2_rect.y += 3
            climbing_background3_rect.y += 3
            if climbing_background2_rect.y > 700:
                climbing_background2_rect.y = -700
            if climbing_background3_rect.y > 700:
                climbing_background3_rect.y = -700
            screen.blit(climbing_walls, climbing_walls_rect)
            obstacle_list = obstacle_movement3(obstacle_list)
            score = display_score()
            screen.blit(stickman_climbing_surf, stickman_climbing_rect)
            if climb_right:
                climbing_right_animation()
                if stickman_climbing_rect.x < 550:
                    stickman_climbing_rect.x += 10
                    stickman_climbing_rect.y -= 2
            else:
                climbing_left_animation()
                if stickman_climbing_rect.x > 300:
                    stickman_climbing_rect.x -= 10
                    stickman_climbing_rect.y -= 2

            coin_list = coin_movement(coin_list, 4, "S")
            if not coins_collisions(stickman_climbing_rect, coin_list):
                coins += 1

            if stickman_climbing_rect.x <= 300 or stickman_climbing_rect.x >= 550:
                if keys[pygame.K_w] and stickman_climbing_rect.y > 20:
                    stickman_climbing_rect.y -= 3
                if keys[pygame.K_s] and stickman_climbing_rect.y < 550:
                    stickman_climbing_rect.y += 3
            if not collisions(stickman_climbing_rect, obstacle_list):
                climbing_lvl += score/(5*(climbing_lvl+1))
                training_over = True
                climbing_training = False
                last_training = 4

        if training_over:
            score_results = stickman_font.render(str(score), True, 'black')
            score_results = pygame.transform.rotozoom(score_results, 0, .7)
            score_results_rect = score_results.get_rect(topleft=(450, 200))

            coin_results = stickman_font.render(str(coins), True, 'black')
            coin_results = pygame.transform.rotozoom(coin_results, 0, .7)
            coin_results_rect = coin_results.get_rect(topleft=(450, 400))

            screen.fill('white')
            screen.blit(training_results_title,
                        training_results_title_rect)
            screen.blit(training_results_score,
                        training_results_score_rect)
            screen.blit(score_results, score_results_rect)
            screen.blit(training_results_coins,
                        training_results_coins_rect)
            screen.blit(coin_results, coin_results_rect)
            screen.blit(back_button, back_button_rect)
            screen.blit(retry_button, retry_button_rect)

            if back_button_rect.collidepoint(mouse_pos):
                screen.blit(back_button_selected,
                            back_button_selected_rect)

            if retry_button_rect.collidepoint(mouse_pos):
                screen.blit(retry_button_selected,
                            retry_button_selected_rect)

        if racing:
            screen.fill('white')
            screen.blit(races_text, races_text_rect)
            screen.blit(back_button, back_button_rect)

            if back_button_rect.collidepoint(mouse_pos):
                screen.blit(back_button_selected, back_button_selected_rect)

            screen.blit(races_map, races_map_rect)
            screen.blit(races_circle, races_circle_rect1)
            screen.blit(races_circle, races_circle_rect2)
            screen.blit(races_circle, races_circle_rect3)
            screen.blit(races_circle, races_circle_rect4)
            screen.blit(races_circle, races_circle_rect5)

            if races_circle_rect1.collidepoint(mouse_pos) and current_race == 1:
                screen.blit(races_circle_selected, races_circle_rect1)
                screen.blit(race1_desc1, race1_desc_rect1)
                screen.blit(race1_desc2, race1_desc_rect2)
                screen.blit(races_click, races_click_rect)

            if races_circle_rect2.collidepoint(mouse_pos) and current_race == 2:
                screen.blit(races_circle_selected, races_circle_rect2)
            if races_circle_rect3.collidepoint(mouse_pos) and current_race == 3:
                screen.blit(races_circle_selected, races_circle_rect3)
            if races_circle_rect4.collidepoint(mouse_pos) and current_race == 4:
                screen.blit(races_circle_selected, races_circle_rect4)
            if races_circle_rect5.collidepoint(mouse_pos) and current_race == 5:
                screen.blit(races_circle_selected, races_circle_rect5)

            screen.blit(races_trophy, races_trophy_rect)

            if current_race == 1:
                races_stickman_rect.x = 115
            elif current_race == 2:
                races_stickman_rect.x = 238
                races_stickman_rect.y = 268
            elif current_race == 3:
                races_stickman_rect.x = 367
                races_stickman_rect.y = 307
            elif current_race == 4:
                races_stickman_rect.x = 480
                races_stickman_rect.y = 220
            elif current_race == 5:
                races_stickman_rect.x = 602
                races_stickman_rect.y = 270

            screen.blit(races_stickman, races_stickman_rect)

            if race1:
                screen.fill('white')
                countdown = display_score()
                # countdown = 23

                # BACKGROUND
                screen.blit(sky, sky_rect)
                screen.blit(hills_running, hills_running_rect)
                screen.blit(hills_running2, hills_running2_rect)
                screen.blit(ground, ground_rect)

                racing_energy_text = stickman_font.render(
                    f"energy: {int(energy)}", True, 'black')
                racing_energy_text = pygame.transform.rotozoom(
                    racing_energy_text, 0, .35)

                racing_energy_text_rect = racing_energy_text.get_rect(
                    topleft=(750, 650))
                screen.blit(racing_energy_text, racing_energy_text_rect)

                if energy <= 0:
                    screen.blit(skip_text, skip_text_rect)
                    if skip_text_rect.collidepoint(mouse_pos):
                        screen.blit(skip_text_selected,
                                    skip_text_selected_rect)

                if countdown > 3:
                    opp_racing_animation()
                    if energy > 0:
                        energy -= .05

                    if countdown <= 15:
                        if countdown <= 13:
                            opp1_pos += .1
                            opp2_pos += .5
                            opp3_pos += .8
                            opp1_idle_rect.x = opp1_pos
                            opp2_idle_rect.x = opp2_pos
                            opp3_idle_rect.x = opp3_pos

                            if energy > 0:
                                running_animation()
                                stickman_racing_pos += stickman_speed
                                stickman_right_rect.x = stickman_racing_pos
                            else:
                                stickman_running_surf = pygame.transform.rotate(
                                    stickman_right, 270)
                                stickman_right_rect.y = 600
                                stickman_right_rect.x -= 2

                        racing_end_banner_rect.x = 1000
                        racing_end_banner_rect.y = 450

                    if racing_end_banner_rect.x > 700:

                        if countdown > 13:
                            opp1_pos += .1
                            opp2_pos += .5
                            opp3_pos += .8
                            opp1_idle_rect.x = opp1_pos
                            opp2_idle_rect.x = opp2_pos
                            opp3_idle_rect.x = opp3_pos
                            if energy > 0:
                                stickman_racing_pos += stickman_speed
                                stickman_right_rect.x = stickman_racing_pos
                                running_animation()
                            else:
                                stickman_running_surf = pygame.transform.rotate(
                                    stickman_right, 270)
                                stickman_right_rect.y = 600
                                stickman_right_rect.x -= 2
                        if countdown > 15:

                            racing_end_banner_rect.x -= 3
                            screen.blit(racing_end_banner,
                                        racing_end_banner_rect)

                        hills_running_rect.x -= 3
                        hills_running2_rect.x -= 3
                        if hills_running_rect.x < -920:
                            hills_running_rect.x = 880
                        if hills_running2_rect.x < -900:
                            hills_running2_rect.x = 900
                    else:
                        screen.blit(racing_end_banner, racing_end_banner_rect)
                        opp1_pos += 2.3
                        opp2_pos += 2.8
                        opp3_pos += 3.2
                        if energy > 0:
                            running_animation()
                            stickman_racing_pos += stickman_speed + 2
                            stickman_right_rect.x = stickman_racing_pos
                        else:
                            stickman_running_surf = pygame.transform.rotate(
                                stickman_right, 270)
                            stickman_right_rect.y = 600

                        opp1_idle_rect.x = opp1_pos
                        opp2_idle_rect.x = opp2_pos
                        opp3_idle_rect.x = opp3_pos
                        if countdown > 23:

                            energy = max_energy
                            screen.fill('white')
                            screen.blit(races_podium, races_podium_rect)

                            for i in range(len(race_result)):
                                if i == 0:
                                    screen.blit(race_result[i],
                                                (432, 215))
                                    if race_result[i] == stickman_right:
                                        screen.blit(races_win, races_win_rect)
                                    else:
                                        screen.blit(
                                            races_lose, races_lose_rect)
                                elif i == 1:
                                    screen.blit(race_result[i],
                                                (285, 280))
                                elif i == 2:
                                    screen.blit(race_result[i],
                                                (555, 322))

                            # if stickman_right_rect.x > 700:
                            #     # screen.blit(races_win, races_win_rect)
                            #     screen.fill('white')
                            #     screen.blit(races_podium, races_podium_rect)
                            #     for i in range(3):
                            #         screen.blit(race_result[i],
                            #                     (races_podium_rect.x + (100 * i),
                            #                      races_podium_rect.y + 100))
                            #     current_race = 2
                            # else:
                            #     # screen.blit(races_lose, races_lose_rect)
                            #     screen.fill('white')
                            #     screen.blit(races_podium, races_podium_rect)
                            #     for i in range(len(race_result)):
                            #         if i == 0:
                            #             screen.blit(race_result[i],
                            #                         (432, 215))
                            #         elif i == 1:
                            #             screen.blit(race_result[i],
                            #                         (285, 280))
                            #         elif i == 2:
                            #             screen.blit(race_result[i],
                            #                         (555, 322))

                            screen.blit(back_button, back_button_rect)
                            if back_button_rect.collidepoint(mouse_pos):
                                pygame.draw.rect(
                                    screen, 'white', back_button_rect)
                                screen.blit(back_button_selected,
                                            back_button_selected_rect)
                        # else:
                        #     if energy > 0:
                        #         stickman_right_rect.x += 2 + stickman_speed
                else:
                    if countdown == 3:
                        countdown_text = stickman_font.render(
                            'Go!', True, 'black')
                    else:
                        countdown_text = stickman_font.render(
                            str(3-countdown), True, 'black')

                    countdown_text_rect = countdown_text.get_rect(
                        center=(450, 350))
                    screen.blit(countdown_text, countdown_text_rect)
                if opp3_idle_rect.x < 910:
                    screen.blit(opp3_surf, opp3_idle_rect)
                else:
                    if not opp3_finish:
                        opp3_finish = True
                        race_result.append(opp3_idle)

                if opp2_idle_rect.x < 910:
                    screen.blit(opp2_surf, opp2_idle_rect)
                else:
                    if not opp2_finish:
                        opp2_finish = True
                        race_result.append(opp2_idle)

                if opp1_idle_rect.x < 910:
                    screen.blit(opp1_surf, opp1_idle_rect)
                else:
                    if not opp1_finish:
                        opp1_finish = True
                        race_result.append(opp1_idle)
                if stickman_right_rect.x < 910 and countdown <= 23:
                    screen.blit(stickman_running_surf, stickman_right_rect)
                else:
                    if not stickman_finish:
                        stickman_finish = True
                        race_result.append(stickman_right)

    pygame.mouse.set_visible(False)
    mouse_cursor_rect.center = mouse_pos
    screen.blit(mouse_cursor, mouse_cursor_rect)

    pygame.display.update()
    clock.tick(60)
