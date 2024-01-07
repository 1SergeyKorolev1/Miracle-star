from utils import functions

def app_operation(start_pack):
    pygame = start_pack.pygame
    run, star_count, clock, start_time, star_add_increment, stars, player = (
        start_pack.run, start_pack.star_count, start_pack.clock,
        start_pack.start_time, start_pack.star_add_increment, start_pack.stars, start_pack.player)
    while run:
        star_count += clock.tick(60)
        elapsed_time = start_pack.time.time() - start_time

        if star_count > star_add_increment:
            functions.get_stars(start_pack, pygame, stars)
            star_add_increment = max(100, star_add_increment - 25)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        functions.control(pygame, player, start_pack)
        functions.hit_and_remove_stars(stars, start_pack, player)

        if start_pack.hit:
            lost_text = start_pack.FONT.render('Вы проиграли', 1, 'red')
            start_pack.WIN.blit(lost_text, (
                start_pack.WIDTH / 2 - lost_text.get_width() / 2, start_pack.HEIGHT / 2 - lost_text.get_height() / 2))
            result_text = start_pack.FONT.render(f'Ваш рекорд: {round(elapsed_time)}c', 1, 'white')
            start_pack.WIN.blit(result_text, (10, 60))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        start_pack.draw(player, elapsed_time, stars, start_pack, pygame)

    pygame.quit()