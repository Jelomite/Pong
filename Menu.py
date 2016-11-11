import pygame, sys


def menu(screen, headline, menu, x_pos=100, y_pos=100, font=None,
         size=70, distance=1.4, fgcolor=(255, 255, 255),
         cursor_color=(255, 0, 0), exit_allowed=True):
    # Draw the Menupoints
    pygame.font.init()
    if font is None:
        my_font = pygame.font.Font(None, size)
    else:
        my_font = pygame.font.SysFont(font, size)
    cursor_pos = 0
    render_w_chars = False
    head_text = my_font.render(headline, True, fgcolor)

    screen.blit(head_text, head_text.get_rect())
    pygame.display.update()
    for i in menu:
        if not render_w_chars:
            text = my_font.render(i, True, fgcolor)
        else:
            text = my_font.render(i, True, fgcolor)
            char += 1
        text_rect = text.get_rect()
        text_rect = text_rect.move(x_pos,
                                   (size // distance * cursor_pos) + y_pos)
        screen.blit(text, text_rect)
        pygame.display.update(text_rect)
        cursor_pos += 1
        if cursor_pos == 9:
            render_w_chars = True
            char = 65

    # Draw the ">", the Cursor
    cursor_pos = 0
    cursor = my_font.render('>', True, cursor_color)
    cursorrect = cursor.get_rect()
    cursorrect = cursorrect.move(x_pos - (size // distance),
                                 (size // distance * cursor_pos) + y_pos)

    # The whole While-loop takes care to show the Cursor, move the
    # Cursor and getting the Keys (1-9 and A-Z) to work...
    arrow_pressed = True
    exit_menu = False
    clock = pygame.time.Clock()
    filler = pygame.Surface.copy(screen)
    filler_rect = filler.get_rect()
    while True:
        clock.tick(30)
        if arrow_pressed:
            screen.blit(filler, filler_rect)
            pygame.display.update(cursorrect)
            cursorrect = cursor.get_rect()
            cursorrect = cursorrect.move(x_pos - (size // distance),
                                         (size // distance * cursor_pos) + y_pos)
            screen.blit(cursor, cursorrect)
            pygame.display.update(cursorrect)
            arrow_pressed = False
        if exit_menu:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and exit_allowed == True:
                    if cursor_pos == len(menu) - 1:
                        exit_menu = True
                    else:
                        cursor_pos = len(menu) - 1
                        arrow_pressed = True

                # This Section is huge and ugly, I know... But I don't
                # know a better method for this^^
                if event.key == pygame.K_1:
                    cursor_pos = 0
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_2 and len(menu) >= 2:
                    cursor_pos = 1
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_3 and len(menu) >= 3:
                    cursor_pos = 2
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_4 and len(menu) >= 4:
                    cursor_pos = 3
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_5 and len(menu) >= 5:
                    cursor_pos = 4
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_6 and len(menu) >= 6:
                    cursor_pos = 5
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_7 and len(menu) >= 7:
                    cursor_pos = 6
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_8 and len(menu) >= 8:
                    cursor_pos = 7
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_9 and len(menu) >= 9:
                    cursor_pos = 8
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_a and len(menu) >= 10:
                    cursor_pos = 9
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_b and len(menu) >= 11:
                    cursor_pos = 10
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_c and len(menu) >= 12:
                    cursor_pos = 11
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_d and len(menu) >= 13:
                    cursor_pos = 12
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_e and len(menu) >= 14:
                    cursor_pos = 13
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_f and len(menu) >= 15:
                    cursor_pos = 14
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_g and len(menu) >= 16:
                    cursor_pos = 15
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_h and len(menu) >= 17:
                    cursor_pos = 16
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_i and len(menu) >= 18:
                    cursor_pos = 17
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_j and len(menu) >= 19:
                    cursor_pos = 18
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_k and len(menu) >= 20:
                    cursor_pos = 19
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_l and len(menu) >= 21:
                    cursor_pos = 20
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_m and len(menu) >= 22:
                    cursor_pos = 21
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_n and len(menu) >= 23:
                    cursor_pos = 22
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_o and len(menu) >= 24:
                    cursor_pos = 23
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_p and len(menu) >= 25:
                    cursor_pos = 24
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_q and len(menu) >= 26:
                    cursor_pos = 25
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_r and len(menu) >= 27:
                    cursor_pos = 26
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_s and len(menu) >= 28:
                    cursor_pos = 27
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_t and len(menu) >= 29:
                    cursor_pos = 28
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_u and len(menu) >= 30:
                    cursor_pos = 29
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_v and len(menu) >= 31:
                    cursor_pos = 30
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_w and len(menu) >= 32:
                    cursor_pos = 31
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_x and len(menu) >= 33:
                    cursor_pos = 32
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_y and len(menu) >= 34:
                    cursor_pos = 33
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_z and len(menu) >= 35:
                    cursor_pos = 34
                    arrow_pressed = True
                    exit_menu = True
                elif event.key == pygame.K_UP:
                    arrow_pressed = True
                    if cursor_pos == 0:
                        cursor_pos = len(menu) - 1
                    else:
                        cursor_pos -= 1
                elif event.key == pygame.K_DOWN:
                    arrow_pressed = True
                    if cursor_pos == len(menu) - 1:
                        cursor_pos = 0
                    else:
                        cursor_pos += 1
                elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    exit_menu = True

    return cursor_pos


if __name__ == '__main__':
    sys.stderr.write("That's not how this shit works.")
    sys.exit()
