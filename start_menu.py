from pygame import *
from btncreator import creator
import json

init()

size = (1400, 788)

screen = display.set_mode(size)

skin_changing = False

ship_upgrade1 = False

charinfo = {}

skins = ['skin1.png', 'skin2.png', 'skin3.png']

counter = 0

fontcreds = font.SysFont('Copperplate Gothic', 30)
font = font.SysFont('Copperplate Gothic', 50)

bg = image.load("media/frames_start_menu/f1 (1).gif").convert_alpha()

menu = creator()


def ship_upgrade():
    menu.clearing()

    global ship_upgrade1

    ship_upgrade1 = True

    with open('spaceship.json', 'r', encoding='utf-8') as j:
        global charinfo

        charinfo = json.load(j)

    menu.add_option(
        f'Upgrade ship > Current level : {charinfo["curlevel"]}', lambda: charupgrade(), font)
    menu.add_option('Change Ship', lambda: skin_change(), font)
    menu.add_option(
        f'Level 1 record : {charinfo["currecordlvl1"]}', False, font)
    menu.add_option(
        f'Level 2 record : {charinfo["currecordlvl2"]}', False, font)
    menu.add_option(
        f'Level 3 record : {charinfo["currecordlvl3"]}', False, font)
    menu.add_option(f'Back >', lambda: main_menu(), font)


def charupgrade():
    with open('spaceship.json', 'w', encoding='utf-8') as j:
        global charinfo
        charinfo['curlevel'] += 1
        json.dump(charinfo, j)

    ship_upgrade()


def main_menu():
    menu.clearing()
    global ship_upgrade1

    ship_upgrade1 = False

    menu.add_option('Level list >', exit, font)
    menu.add_option('Upgrade spaceship >', lambda: ship_upgrade(), font)
    menu.add_option('Quit >', exit, font)


main_menu()


def skin_change():

    global skin_changing

    skin_changing = 1

    ship_upgrade()


creds = [fontcreds.render('Credits:', True, (255, 255, 255)), fontcreds.render(
    'Nikita Kananadze', True, (255, 255, 255)), fontcreds.render('Anna Lobanova', True, (255, 255, 255))]

background_index = 1
background_time = 0
background_delay = 85

clock = time.Clock()
running = True
while running:
    for event_ in event.get():
        if event_.type == QUIT:
            running = False
        if event_.type == KEYDOWN:
            if not skin_changing:
                if event_.key == K_UP:
                    menu.switch_point(-1)
                elif event_.key == K_DOWN:
                    menu.switch_point(1)
                elif event_.key == K_RIGHT:
                    menu.select()
            if skin_changing:
                if event_.key == K_RIGHT:
                    counter += 1
                if event_.key == K_LEFT:
                    counter -= 1
                if event_.key == K_UP:
                    with open('spaceship.json', 'w', encoding='utf-8') as j:
                        charinfo['curskin'] = f'media/playable_{skins[counter % 3]}'
                        json.dump(charinfo, j)
                    skin_changing = False

    time_now = time.get_ticks()

    if not ship_upgrade1:
        if time_now > background_time + background_delay:
            background_time = time_now
            background_index += 1
            if background_index > 45:
                background_index = 1

            screen.blit(image.load(
                f"media/frames_start_menu/f1 ({int(background_index)}).gif").convert_alpha(), (0, 0))

        for i, option in enumerate(creds):
            option_rect = option.get_rect()
            option_rect.topleft = (1100, 660 + i * 40)
            screen.blit(option, option_rect)

    else:
        screen.blit(image.load(
            f"media/background_upgrading.png").convert_alpha(), (0, 0))
        screen.blit(image.load(
            f'media/{skins[(counter) % 3]}').convert_alpha(), (900, 450))

    if not skin_changing:
        menu.draw(screen, 100, 100, 75)

    else:
        menu.draw(screen, 100, 100, 75)
        screen.blit(image.load('media/left_icon.png'), (840, 600))
        screen.blit(image.load('media/right_icon.png'), (1200, 600))

    display.flip()

quit()