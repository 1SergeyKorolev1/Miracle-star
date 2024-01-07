import start_pack

pygame = start_pack.pygame

def draw(player, elapsed_time, stars):
    start_pack.WIN.blit(start_pack.BG, (0, 0))

    time_text = start_pack.FONT.render(f'Время: {round(elapsed_time)}c', 1, 'white')
    start_pack.WIN.blit(time_text, (10, 10))

    # pygame.draw.rect(start_pack.WIN, 'blue', player)
    pygame.draw.ellipse(start_pack.WIN, 'blue', player)
    for star in stars:
        pygame.draw.rect(start_pack.WIN, 'white', star)
    pygame.display.update()


def app():
    run = True
    # player = pygame.Rect(200, start_pack.HEIGHT - start_pack.PLAYER_HEIGHT, start_pack.PLAYER_WIDTH,
    #                      start_pack.PLAYER_HEIGHT)
    player = pygame.draw.circle(start_pack.WIN, 'blue', (start_pack.WIDTH / 2, start_pack.HEIGHT - start_pack.PLAYER_RADIUS),
                                start_pack.PLAYER_RADIUS, width=0)

    clock = pygame.time.Clock()
    start_time = start_pack.time.time()

    star_add_increment = 1000
    star_count = 0

    stars = []
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = start_pack.time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = start_pack.random.randint(0, start_pack.WIDTH - start_pack.STAR_WIDTH)
                star = pygame.Rect(star_x, -start_pack.STAR_HEIGHT, start_pack.STAR_WIDTH, start_pack.STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(100, star_add_increment - 25)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - start_pack.PLAYER_TURN >= 0:
            player.x -= start_pack.PLAYER_TURN
        if (keys[pygame.K_d] or keys[
            pygame.K_RIGHT]) and player.x + start_pack.PLAYER_TURN + player.width <= start_pack.WIDTH:
            player.x += start_pack.PLAYER_TURN

        for star in stars[:]:
            star.y += start_pack.STAR_TURN
            if star.y > start_pack.HEIGHT:
                stars.remove(star)
            elif star.y >= player.y - 14 and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = start_pack.FONT.render('Вы проиграли', 1, 'red')
            start_pack.WIN.blit(lost_text, (
                start_pack.WIDTH / 2 - lost_text.get_width() / 2, start_pack.HEIGHT / 2 - lost_text.get_height() / 2))
            result_text = start_pack.FONT.render(f'Ваш рекорд: {round(elapsed_time)}c', 1, 'white')
            start_pack.WIN.blit(result_text, (10, 60))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


if __name__ == '__main__':
    app()
