def get_stars(start_pack, pygame, stars):
    for _ in range(3):
        star_x = start_pack.random.randint(0, start_pack.WIDTH - start_pack.STAR_WIDTH)
        star = pygame.Rect(star_x, -start_pack.STAR_HEIGHT, start_pack.STAR_WIDTH, start_pack.STAR_HEIGHT)
        stars.append(star)

def control(pygame, player, start_pack):
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - start_pack.PLAYER_TURN >= 0:
        player.x -= start_pack.PLAYER_TURN
    if (keys[pygame.K_d] or keys[
        pygame.K_RIGHT]) and player.x + start_pack.PLAYER_TURN + player.width <= start_pack.WIDTH:
        player.x += start_pack.PLAYER_TURN

def hit_and_remove_stars(stars, start_pack, player):
    for star in stars[:]:
        star.y += start_pack.STAR_TURN
        if star.y > start_pack.HEIGHT:
            stars.remove(star)
        elif star.y >= player.y - 14 and star.colliderect(player):
            stars.remove(star)
            start_pack.hit = True
            break