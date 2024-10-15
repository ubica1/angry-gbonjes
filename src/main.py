import pygame

# инициализируем пайгейм
pygame.init()

# задаем размеры окна
X = 800
Y = 450

# инициализируем окно
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Angry Gbonjs')

# подгружаем картинки
button_start = pygame.image.load("resources/images/start_button.jpg").convert()
button_exit = pygame.image.load("resources/images/exit_button.jpg").convert()
background_image = pygame.image.load("resources/images/background.jpg").convert()
game_background = pygame.image.load("resources/images/game_background.jpg").convert()

# задаем позиции для кнопок
start_rect = button_start.get_rect(center=(X // 2, Y // 3))
exit_rect = button_exit.get_rect(center=(X // 2, Y // 1.5))

# делаем флаг для меню
menu_active = True

while True:
    for event in pygame.event.get():
        # проверяем нажатие кнопки выхода
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if menu_active:
            # считываем клик, если координата нажатия лежит в кнопке старта то снимаем флаг, если в кнопке екзита, то выходим
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    menu_active = False
                elif exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()
    # отрисовываем кнопки и фон
    if menu_active:
        screen.blit(background_image, (0, 0))
        screen.blit(button_start, start_rect.topleft)
        screen.blit(button_exit, exit_rect.topleft)
    # попадая сюда после нажатия старта отрисовываем картинку
    else:
        screen.blit(game_background, (0, 0))
    # обновляем кадр
    pygame.display.flip()
