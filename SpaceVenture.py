import pygame
import random
import os
from pygame.locals import *


pygame.init()

pygame.mixer.init()
pygame.mixer.set_num_channels(10000)
FPS = 60

score = ()
shoot = 0
WIDTH = 1080
HEIGHT = 540
shoot_time = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# 遊戲初始化 and 創建視窗
pygame.init()
pygame.mixer.init()
screen_shake = 0
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT), pygame.SCALED + pygame.RESIZABLE)
pygame.display.toggle_fullscreen()
pygame.display.set_caption("Space-Venture")
clock = pygame.time.Clock()

# 載入圖片

health_img = pygame.image.load(os.path.join("data", "img", "health.png")).convert()
start_img = pygame.image.load(os.path.join("data", "img",  "start.png"))
health_img.set_colorkey(BLACK)
player_img = pygame.image.load(os.path.join("data", "img",  "player.png"))
player_img.get_rect()
player_mini_img = pygame.transform.scale(player_img, (30, 29))
startgame_img = pygame.image.load(os.path.join("data", "img",  "startgame.jpg"))
button1_img = pygame.image.load(os.path.join("data", "img",  "button1.png"))
bullet2_img = [pygame.image.load(os.path.join("data", "img",  "bullet2.png")),
               pygame.image.load(os.path.join("data", "img",  "bullet3.png"))]
background_img = pygame.image.load(os.path.join("data", "img",  "background.png"))
pygame.transform.scale(startgame_img, (720, 540))
writtenby_img = pygame.image.load(os.path.join("data", "img",  "writtenby.jpg"))
player_mini_img.set_colorkey(BLACK)
pygame.display.set_icon(player_mini_img)
bullet_img = pygame.image.load(os.path.join("data", "img", "bullet.png"))
rock_imgs = []

for i in range(7):
    rock_imgs.append(pygame.image.load(
        os.path.join("data", "img",  f"rock{i}.png")).convert())

for i in range(9):
    redexpl_img = pygame.image.load(os.path.join("data", "img", f"redexpl{i}.png"))

redexpl_anim = {'lg': [], 'sm': [], 'player': []}
for i in range(9):
    redexpl_img = pygame.image.load(os.path.join("data", "img",  f"redexpl{i}.png"))
    redexpl_anim['lg'].append(pygame.transform.scale(redexpl_img, (400, 400)))
    redexpl_anim['sm'].append(pygame.transform.scale(redexpl_img, (50, 50)))
    player_expl_img = pygame.image.load(
        os.path.join("data", "img",  f"player_expl{i}.png"))
    player_expl_img.set_colorkey(BLACK)
    redexpl_anim['player'].append(player_expl_img)
power_imgs = {'shield': pygame.image.load(os.path.join("data", "img",  "shield.png")),
              'gun': pygame.image.load(os.path.join("data", "img",  "gun.png"))}

expl_anim = {'lg': [], 'sm': [], 'player': []}
for i in range(9):
    expl_img = pygame.image.load(os.path.join("data", "img",  f"expl{i}.png"))
    expl_anim['lg'].append(pygame.transform.scale(expl_img, (400, 400)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img, (50, 50)))
    player_expl_img = pygame.image.load(
        os.path.join("data", "img",  f"player_expl{i}.png"))
    player_expl_img.set_colorkey(BLACK)
    expl_anim['player'].append(player_expl_img)
power_imgs = {'shield': pygame.image.load(os.path.join("data", "img",  "shield.png")),
              'gun': pygame.image.load(os.path.join("data", "img",  "gun.png"))}

# 載入音樂、音效
shoot_sound = pygame.mixer.Sound(os.path.join("data", "sfx", "shoot.wav"))
wasted_sound = pygame.mixer.Sound(os.path.join("data", "sfx", "wasted.mp3"))
teleport_sound = pygame.mixer.Sound(os.path.join("data", "sfx", "teleport.mp3"))
level_up = pygame.mixer.Sound(os.path.join("data", "sfx", "levelup.mp3"))
gameover_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "gameover.mp3"))
start_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "start.mp3"))
start = pygame.mixer.Sound(os.path.join("data", "sfx",  "startgame.mp3"))
start_sound2 = pygame.mixer.Sound(os.path.join("data", "sfx",  "start2.mp3"))
intro_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "intro.mp3"))
gun_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "pow1.wav"))
shield_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "pow0.wav"))
die_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "rumble.ogg"))
expl_sounds = [
    pygame.mixer.Sound(os.path.join("data", "sfx",  "expl0.wav")),
    pygame.mixer.Sound(os.path.join("data", "sfx",  "expl1.wav"))

]
background_sound = pygame.mixer.Sound(os.path.join("data", "sfx",  "background.mp3"))

font_name = os.path.join("data", "font",  "font.ttf")
font_name2 = os.path.join("data", "font",  "pixelart.ttf")
font_name3 = os.path.join("data", "font",  "pixelart2.ttf")

pygame.mouse.set_visible(bool(0))


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)
    screenshake = 10
    if screenshake > 0:
        screenshake -= 1
    render_offset = [0, 0]
    if screenshake:
        render_offset[0] = random.randint(0, 2) - 1
        render_offset[1] = random.randint(0, 2) - 1
        screen.blit(screen, render_offset)
    if player.gun >= 2:
        render_offset[0] = random.randint(0, 4) - 2
        render_offset[1] = random.randint(0, 4) - 2
        screen.blit(screen, render_offset)


def blit_center(target_surf, surf, loc):
    target_surf.blit(
        surf, (loc[0] - surf.get_width() // 2, loc[1] - surf.get_height() // 2))


def blit_center_add(target_surf, surf, loc):
    target_surf.blit(surf, (loc[0] - surf.get_width() // 2, loc[1] - surf.get_height() // 2),
                     special_flags=pygame.BLEND_RGBA_ADD)


def draw_text4(surf, text, size, x, y):
    font = pygame.font.Font(font_name2, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def draw_text5(surf, text, size, x, y):
    font = pygame.font.Font(font_name3, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


class Background(pygame.sprite.Sprite):
    def __init__(self):

        self.bgimage = pygame.image.load(
            os.path.join("data", "img",  "background.png")).convert()

        self.bgimage2 = pygame.image.load(
            os.path.join("data", "img",  "background2.png")).convert()
        self.rectBGimg = self.bgimage.get_rect()
        self.rectBGimg2 = self.bgimage.get_rect()

        self.bgX1 = 0
        self.bgY1 = 0

        self.bgX2 = 0
        self.bgY2 = -self.rectBGimg.height
        self.movingUpspeed = -1

    def update(self):
        self.bgY1 -= self.movingUpspeed
        self.bgY2 -= self.movingUpspeed
        if self.bgY1 >= self.rectBGimg.height:
            self.bgY1 = -self.rectBGimg.height
        if self.bgY2 >= self.rectBGimg2.height:
            self.bgY2 = -self.rectBGimg2.height

    def render(self):

        screen.blit(self.bgimage, (self.bgX2, self.bgY2))
        screen.blit(self.bgimage2, (self.bgX1, self.bgY1))


back_ground = Background()


def draw_text2(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)
    screen_shake = 20
    if screen_shake > 0:
        screen_shake -= 1
    render_offset = [0, 0]
    if screen_shake:
        render_offset[0] = random.randint(0, 2) - 1
        render_offset[1] = random.randint(0, 2) - 1
        screen.blit(screen, render_offset)
    if player.gun >= 2:
        render_offset[0] = random.randint(0, 4) - 1
        render_offset[1] = random.randint(0, 4) - 1
        screen.blit(screen, render_offset)


def draw_text3(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


def new_rock():
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)


def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 200
    BAR_HEIGHT = 20
    fill = (hp / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, BLACK, outline_rect, 4)

    screen.blit(health_img, (-11, -74))


def draw_lives(surf, lives, img, x, y):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 32 * i
        img_rect.y = y
        surf.blit(img, img_rect)


def fade(WIDTH, HEIGHT):
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))
    for alpha in range(0, 45):
        fade.set_alpha(alpha)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(18)


def fade2(WIDTH, HEIGHT):
    fade2 = pygame.Surface((WIDTH, HEIGHT))
    fade2.fill((0, 0, 0))
    for alpha in range(0, 25):
        fade2.set_alpha(alpha)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(fade2, (0, 0))
        pygame.display.update()
        pygame.time.delay(7)


def startgame() -> object:
    background_sound.stop()

    screen.blit(startgame_img, (0, 0))
    pygame.display.update()
    start.play()
    pygame.time.delay(660)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            return False
            pygame.quit()
            quit()

    fade(1080, 540)

    pygame.display.update()


def draw_init() -> object:
    global event
    background_sound.stop()
    intro_sound.play()
    pygame.display.update()

    # gets mouse position

    # checks if mouse position is over the button

    background_sound.play()

    back_ground.movingUpspeed = -4.6
    waiting = True

    particles = []
    while waiting:

        if back_ground.movingUpspeed < -0.3:
            back_ground.movingUpspeed += 0.1

        back_ground.update()
        back_ground.render()

        draw_text3(screen, 'SPACEVENTURE ', 130, WIDTH / 2, HEIGHT / 4)
        draw_text5(screen, 'click to start ', 15, WIDTH / 2, 480)
        draw_text4(screen, 'esc = exit ', 20, 80, 10)
        draw_text3(screen, 'you scored', 30, WIDTH / 2.6, 280)
        draw_text3(screen, str(score), 40, WIDTH / 1.6, 280)

        pygame.display.update()

        # Buttons ------------------------------------------------ #

        # Update ------------------------------------------------- #

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    background_sound.stop()
                    fade2(1080, 540)
                    start_sound.play()
                    start_sound2.play()
                    pygame.mixer.music.set_volume(100)
                    back_ground.movingUpspeed = -1
                    back_ground.update()
                    back_ground.render()
                    return False

                    waiting = False

        clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (66, 80))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT
        self.speedx = 4
        self.speedy = 9
        self.pos = self.rect.midbottom
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_e]:
            if self.speedx > 9:
                self.speedx += 30

        self.health = 100
        self.lives = 3
        self.hidden = False
        self.gun = 1
        self.gun_time = 0
        pygame.display.update()

    def dash(self):
        self.rect.x -= 30
        if self.rect.x < 0:
            self.rect.x += 2

    def update(self):

        key_pressed = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if score >= 1:

            if self.gun > 1 and now - self.gun_time > 1000:
                draw_text3(screen, str(self.gun_time), 40, WIDTH / 2, 10)

                self.gun -= 1
                self.gun_time = now

            if self.hidden and now - self.hide_time > 1000:
                self.hidden = False
                self.rect.centerx = WIDTH / 2
                self.rect.bottom = HEIGHT

        if key_pressed[pygame.K_d]:
            if score >= 1:

                if player.rect.x < 1000:
                    self.rect.x += self.speedx
                    if key_pressed[pygame.K_q]:
                        if player.rect.x < 1000:
                            self.rect.x += self.speedx + 21
                            if player.health < 100:
                                if player.rect.x < 1000:
                                    player.health += 1

        if key_pressed[pygame.K_a]:
            if score >= 1:
                if player.rect.x > 20:
                    self.rect.x -= self.speedx
                    if key_pressed[pygame.K_e]:

                        if player.rect.x > 20:
                            self.rect.x -= self.speedx + 21
                            if player.health < 100:
                                if player.rect.x > 20:
                                    player.health += 1
                for event in pygame.event.get():

                    if event.type == QUIT:
                        pygame.quit()

                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0

        if key_pressed[pygame.K_ESCAPE]:
            self.lives = -1

    def rotate(self):
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def shoot(self):

        if not (self.hidden):
            if self.rect.y > 400:
                self.rect.y -= random.randint(-4, 5)

            self.rect.x -= random.randint(-2, 2)

            if self.gun == 1:
                self.image.set_alpha(1000)

                bullet = Bullet(self.rect.centerx, self.rect.y)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
                if player.health > 1:
                    player.health -= 1

            elif self.gun >= 2:
                self.image.set_alpha(90)

                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)

                bullets.add(bullet2)
                if player.health < 98:
                    player.health += 2
                pygame.mixer.music.set_volume(1)
                shoot_sound.play()
                pygame.display.update()

    def hide(self):
        self.hidden = True
        self.hide_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 500)

    def gunup(self):
        self.gun += 1
        self.gun_time = pygame.time.get_ticks()


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)
        self.image_ori.set_colorkey(BLACK)
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-200, -180)
        self.speedy = random.randrange(15, 20)
        self.speedx = random.randrange(-5, 5)
        self.total_degree = 0
        self.rot_degree = random.randrange(-3, 8)

        pygame.display.update()

    def rotate(self):
        self.total_degree += self.rot_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center

    def update(self):
        if score >= 1:

            self.rotate()
            self.rect.y += self.speedy
            self.rect.x += self.speedx
            if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
                self.rect.x = random.randrange(0, WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(10, 15)
                self.speedx = random.randrange(-13, 13)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        if player.gun <= 2:
            shoot_sound.set_volume(1)
            self.image = bullet_img
        if player.gun >= 2:
            self.image = random.choice(bullet2_img)

        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(x - 10, x + 10)
        self.rect.bottom = y + 37
        self.speedy = -20
        if player.gun >= 2:
            shoot_sound.set_volume(0.4)
            self.speedy = -27

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        if player.gun <= 1:
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = expl_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 20
        if player.gun >= 2:
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = redexpl_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 25

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            if self.frame == len(redexpl_anim[self.size]):
                self.kill()
            else:
                if player.gun <= 1:
                    self.image = expl_anim[self.size][self.frame]
                    center = self.rect.center
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                if player.gun >= 2:
                    self.image = redexpl_anim[self.size][self.frame]
                    center = self.rect.center
                    self.rect = self.image.get_rect()
                    self.rect.center = center


class Power(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = power_imgs[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 5.8

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

# 遊戲迴圈


startgame()

show_init = True
running = True
while running:




    if show_init:
        close = draw_init()
        if close:
            break
        show_init = False

        all_sprites = pygame.sprite.Group()
        rocks = pygame.sprite.Group()
        rocks2 = pygame.sprite.Group()
        back_ground = Background()
        boss = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powers = pygame.sprite.Group()
        player: Player = Player()

        all_sprites.add(player)

        for i in range(8):
            new_rock()
        score = 0

    clock.tick(60)

    # Buttons ------------------------------------------------ #

    # Update ------------------------------------------------- #
    # 取得輸入

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_e:
                back_ground.movingUpspeed -= -0.3

        if event.type == KEYUP:
            if event.key == K_e:
                back_ground.movingUpspeed = -1
        if event.type == KEYDOWN:
            if event.key == K_q:
                back_ground.movingUpspeed -= -0.3

        if event.type == KEYUP:
            if event.key == K_q:
                back_ground.movingUpspeed = -1
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if score < 1:
                        score += 1
                        fade2(1080, 540)

            if score > 0.1:
                if event.button == 4:
                        player.shoot()


            if score > 0.1:
                if event.button == 5:
                    player.shoot()
            if score < 1:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        score -= 1

    # 更新遊戲
    all_sprites.update()
    # 判斷石頭 子彈相撞
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits:
        random.choice(expl_sounds).play()
        score += hit.radius
        expl = Explosion(hit.rect.center, 'lg')

        all_sprites.add(expl)

        if random.random() > 0.9:
            pow = Power(hit.rect.center)
            all_sprites.add(pow)
            powers.add(pow)

        new_rock()

    # 判斷石頭 飛船相撞
    hits = pygame.sprite.spritecollide(
        player, rocks, True, pygame.sprite.collide_circle)
    for hit in hits:

        new_rock()

        player.health -= hit.radius * 2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.health <= 0:
            player.gun = 1
            death_expl = Explosion(player.rect.center, 'player')
            all_sprites.add(death_expl)
            die_sound.play()
            player.lives -= 1

            player.health = 100
            player.hide()
            if player.lives <= 2:
                player.image.set_alpha(1000)

    # 判斷寶物 飛船相撞

    hits = pygame.sprite.spritecollide(player, powers, True)
    for hit in hits:
        if hit.type == 'shield':
            player.health += 20
            if player.health > 100:
                player.health = 100
            shield_sound.play()
        elif hit.type == 'gun':
            player.gunup()
            gun_sound.play()

    if player.lives == 0 and not (death_expl.alive()):

        for i in range(6):
            rock_imgs.append(pygame.image.load(
                os.path.join("data", "img", f"rock{i}.png")).convert())

        draw_text3(screen, 'press F to continue', 60, WIDTH / 2, 400)
        draw_text3(screen, 'nice try', 56, WIDTH / 2.6, 320)

        waiting = True
        while waiting:

            back_ground = Background()

            background_sound.stop()

            pygame.mixer.set_num_channels(1)
            gameover_sound.play()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            show_init = True

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_f]:
                fade2(1080, 540)

                waiting = False
                pygame.mixer.set_num_channels(10000)
                gameover_sound.stop()
                intro_sound.play()

    back_ground.update()
    back_ground.render()

    if player.lives == -1:

        show_init = True

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_f]:
            waiting = False
            pygame.mixer.set_num_channels(10000)
            gameover_sound.stop()
            intro_sound.play()

    back_ground.update()
    back_ground.render()

    all_sprites.draw(screen)
    if score > 1:
        if score < 10000:
            draw_text(screen, str(score), 40, WIDTH / 2, 10)

    if score > 10000:
        screen_shake = 30

        draw_text2(screen, str(score), 80, WIDTH / 2, 12)
    draw_text(screen, "", 10, 10, 10)
    if score < 1:
        draw_text5(screen, "click to start", 20, WIDTH / 2, 360)
        draw_text5(screen, "one score is guaranteed", 20, WIDTH / 2, 340)
        draw_text4(screen, "ESC = main menu", 20, 300, 100)
        draw_text4(screen, "A = move left", 20, 300, 130)
        draw_text4(screen, "D = move right", 20, 300, 160)
        draw_text4(screen, "SCROLL = fire", 20, 780, 100)
        draw_text4(screen, "A + E = Dash - L", 20, 780, 130)
        draw_text4(screen, "D + Q = Dash - R", 20, 780, 160)
        draw_text5(screen, "HOW TO PLAY", 60, WIDTH / 2, 20)
    else:
        draw_health(screen, player.health, 20, 15)
        draw_lives(screen, player.lives, player_mini_img, WIDTH - 100, 15)

    pygame.display.update()

pygame.quit()
