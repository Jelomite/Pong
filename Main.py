import sys
import Object
import Menu
import Colors
import pygame
import GUIText
import socket
import math
import Server
import thread
from pygame.locals import *

# default ip and port
port = 4050
bug_iteration = 0

# static variables
pygame.init()
my_font = pygame.font.Font(None, 30)
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
menu = True

pygame.display.set_caption("Pong")
all_data = ''


def print_text(color, x, y, message):
    screen.blit(my_font.render(message, 1, color),
                [x, y])
    pygame.display.update()


try:
    icon = pygame.image.load(__file__.replace('Main.py', '') + '/Pong Logo.png')
    pygame.display.set_icon(icon)
except:
    print 'unable to load icon'

try:
    host = (
        [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
                     [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in
                       [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
except:
    host = '127.0.0.1'
    sys.stderr.write('no internet connection, game will join localhost')
    print ''
    print_text(Colors.pomegranate, width / 3, 50, 'Searching for Players...')
host1 = host


# gui text method, gets message as a prompt, and returns the value that is written in it.
def text(message):
    txtbx = GUIText.Input(maxlength=16, color=Colors.pure_white, prompt=message)
    # create the pygame clock
    clock = pygame.time.Clock()
    # main loop!

    while True:
        # make sure the program is running at 30 fps
        clock.tick(60)

        # events for txtbx
        events = pygame.event.get()
        # process other events

        screen.fill(Colors.pure_black)
        # update txtbx
        txtbx.update(events)
        txtbx.draw(screen)
        pygame.display.flip()

        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    return txtbx.value


# data transfer manager
def connection(message):
    s.send(message)
    date = s.recv(1024)
    return date


# returns distance between two cords
def distance((x1, y1), (x2, y2)):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


while True:
    carry = True
    screen.fill(Colors.pure_black)
    pygame.display.update()
    pygame.key.set_repeat(500, 30)

    choose = Menu.menu(screen, 'Pong', [
        'Play',
        'Host',
        'Options',
        'Quit Game'], width / 3, height / 3, None, 50, 1.4, Colors.pure_white, Colors.pure_white)

    # game itself is initialized and runs here.
    if choose == 0:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        print 'timeout is now 5 seconds'

        try:
            s.connect((host, port))
            print "connection established with %s:%s" % (host, port)


        except:
            print "unable to connect %s:%s" % (host, port)

            continue

        sys.stdout.flush()

        screen_width = 680
        screen_height = 480
        fps = 60

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pong")
        score_font = my_font

        clock = pygame.time.Clock()
        carry = True
        speed = 4
        movement = [1, 0.5]

        inverted = 1
        angle = math.pi / 6

        socket_list = [sys.stdin, s]

        ready_to_read = socket_list
        first = int(str(s.recv(4096)).split(':', 3)[0])
        if first == -1:
            inverted = first
        elif first == 1:
            pass
        print_text(Colors.pomegranate, width / 3, 50, 'Searching for Players...')
        player_right = Object.Racket(Colors.pure_white, screen_width * 0.9 - 5, screen_height / 2, (10, 50))
        player_left = Object.Racket(Colors.pure_white, screen_width * 0.1 + 5, screen_height / 2, (10, 50))
        ball = Object.Racket(Colors.pure_white, screen_width / 2, screen_height / 2, (10, 10))
        sprites = [player_right, player_left, ball]
        players = pygame.sprite.Group(player_left, player_right)
        game_sprites = pygame.sprite.Group(sprites)

        collision_list = pygame.sprite.spritecollide(ball, players, False)
        one_time = True
        cooldown = 0
        data = ''
        score = 0

        while carry:
            try:
                all_data = connection("0:0:0:0")
                carry = False
            except:
                all_data = "0:0:0:0"
                pygame.display.update()
                break

        carry = True
        s.settimeout(0.1)

        while carry:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carry = False
            keys = pygame.key.get_pressed()

            # right controls
            if keys[pygame.K_DOWN] and player_right.rect.y < screen_height - 54:
                player_right.move_down(speed)
            if keys[pygame.K_UP] and 0 < player_right.rect.y:
                player_right.move_up(speed)

            exit_mode = True
            try:
                all_data = connection(
                    str(player_right.rect.y) + ':' + str(ball.rect.x) + ':' + str(ball.rect.y) + ':' + str(score))
                temp = int(all_data.split(':', 3)[3])
                exit_mode = False
            except:
                all_data = "0:0:0:0"

                print "unable to retrieve data from server 1"
                break
            if exit_mode:
                carry = False
                break
            if distance((ball.rect.x, ball.rect.y),
                        (screen_width - int(all_data.split(':', 3)[1]),
                         int(all_data.split(':', 3)[2]))) > 10 and inverted == 1:
                ball.set_position(screen_width - int(all_data.split(':', 3)[1]), int(all_data.split(':', 3)[2]))

            player_left.rect.y = int(all_data.split(':', 3)[0])
            ball_pos = (screen_width - int(all_data.split(':', 3)[1]), int(all_data.split(':', 3)[2]))
            ball.move_angle(speed, movement, inverted)
            # if distance((ball.rect.x, ball.rect.y), ball_pos) > 180 and inverted:
            #   ball.set_position(ball_pos[0], ball_pos[1])

            if not 0 < ball.rect.y < screen_height:
                movement[1] = -movement[1]
            if not 0 < ball.rect.x < screen_width:
                if ball.rect.x <= 0:
                    score += 1
                ball.set_position(screen_width / 2, 30)

            collision_list = pygame.sprite.spritecollide(ball, players, False)

            if len(collision_list) and cooldown > 6:
                movement[0] = -movement[0]
                cooldown = 0

            cooldown += 1

            bug_iteration += 1

            # print bug_iteration, ball.rect.x, ball.rect.y
            try:
                their_score = all_data.split(':', 3)[3]
            except IndexError:
                their_score = '0'

            score_text = score_font.render(their_score + ':' + str(score), 1, Colors.pure_white)
            pygame.draw.rect(screen, Colors.pure_black, [0, 0, screen_width, screen_height])
            screen.blit(score_text, [screen_width / 2, 100])
            game_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(fps)

    # host server
    elif choose == 1:
        menu = True
        while menu:
            # reset screen
            screen.fill(Colors.pure_black)

            server_choose = Menu.menu(screen, 'IP: ' + host1 + ':' + str(port), [
                'Start Server',
                'Change Port',
                'Back'
            ], width / 3, height / 3, None, 50, 1.4, Colors.pure_white, Colors.pure_white)

            if server_choose == 0:
                thread.start_new_thread(Server.server, (4050, ''))
            elif server_choose == 1:
                port = text('Port: ')
                if not port:
                    port = 4050
            elif server_choose == 2:
                menu = False

    elif choose == 2:
        # options menu
        menu = True
        while menu:
            # reset screen
            screen.fill(Colors.pure_black)
            pygame.display.update()
            choose = Menu.menu(screen, 'Options', [
                'Back',
                'IP',
                'Port'], width / 3, height / 3, None, 50, 1.4, Colors.pure_white, Colors.pure_white)
            if choose == 0:
                menu = False
            elif choose == 1:
                host = text('ip: ')
                if not host:
                    host = host1
            elif choose == 2:
                port = text('port: ')
                if not port:
                    port = 4050
    elif choose == 3:
        break
    s.close()
pygame.quit()
exit()
