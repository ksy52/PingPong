from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
ракетка3 = transform.scale(image.load('ракетка3.png'), (600, 100)) 
ракетка4 = transform.scale(image.load("ракетка4.png"), (100, 100))
clock = time.Clock()
FPS = 60
game = True 
x1 = y1 = 300
x2 = y2 = 70

class GameSprit(sprite.Sprite):
    def __init__ (self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprit):
    def update_l(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += self.speed
            
pl1 = Player('ракетка3.png', 30, 10, 10)
pl2 = Player('ракетка4.png', 600, 10, 10)


while game:

    clock.tick(FPS)
    window.fill((127, 199, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    pl1.reset()
    pl1.update_l()
    pl2.reset()
    pl2.update_r()
    display.update()