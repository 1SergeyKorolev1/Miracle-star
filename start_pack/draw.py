def draw(player, elapsed_time, stars, start_pack, pygame):
    start_pack.WIN.blit(start_pack.BG, (0, 0))

    time_text = start_pack.FONT.render(f'Время: {round(elapsed_time)}c', 1, 'white')
    start_pack.WIN.blit(time_text, (10, 10))

    # pygame.draw.rect(start_pack.WIN, 'blue', player)
    pygame.draw.ellipse(start_pack.WIN, 'blue', player)
    for star in stars:
        pygame.draw.rect(start_pack.WIN, 'white', star)
    pygame.display.update()