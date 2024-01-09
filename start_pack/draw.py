def draw(player, elapsed_time, stars, start_pack, pygame):
    start_pack.WIN.blit(start_pack.BG, (0, 0))

    time_text = start_pack.FONT.render(f'Время: {round(elapsed_time)}c', 1, 'white')
    start_pack.WIN.blit(time_text, (10, 10))

    # pygame.draw.rect(start_pack.WIN, 'blue', player)
    # pygame.draw.ellipse(start_pack.WIN, 'blue', player)
    start_pack.WIN.blit(start_pack.player_image_transform, player)
    # start_pack.WIN.blit(player, (start_pack.WIDTH / 2, start_pack.HEIGHT - start_pack.PLAYER_HEIGHT))

    star_image = pygame.image.load('image/star/star.png')
    star_image_transform = pygame.transform.scale(star_image, (start_pack.STAR_WIDTH, start_pack.STAR_HEIGHT))
    for star in stars:
        start_pack.WIN.blit(star_image_transform, star)
    pygame.display.update()