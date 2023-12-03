from pygame import *


class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 1000:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700:
            self.rect.y += self.speed

    direction = 'right'
    def move2(self):
        if self.rect.x > 1000:
            self.direction = 'left'
        if self.rect.x < 20:
            self.direction = 'right'
        
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
    
    direction2 = 'up'
    def move3(self):
        if self.rect.y > 600:
            self.direction = 'down'
        if self.rect.y < 100:
            self.direction = 'up'
        
        if self.direction == 'up':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
        # кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




window = display.set_mode((1100,700), RESIZABLE)
picture = transform.scale(image.load("bg1.png"),(1100,700))

anti_mage = Object("anti-mage.png",80,300,100,100,10)
pudge = Object("pudge.png",800,50,100,100,4)
Krip = Object("Krip1.webp",800,150,100,100,4)

wall = Wall(0, 0, 0, 200, 200, 1000, 10)
wall2 = Wall(0, 0, 0, 200, 200, 10, 1000)

clock = time.Clock()
#створення головного циклу
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    window.blit(picture,(0,0))
    anti_mage.reset()
    pudge.reset()
    Krip.reset()
    anti_mage.move()
    pudge.move2()
    Krip.move3()
    wall.draw_wall()
    wall2.draw_wall()

    if sprite.collide_rect(anti_mage, pudge) or sprite.collide_rect(anti_mage, Krip):
        game = False


 
    
    display.update()
    clock.tick(60)