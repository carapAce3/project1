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


window = display.set_mode((1100,700), RESIZABLE)
picture = transform.scale(image.load("bg1.png"),(1100,700))

anti_mage = Object("anti-mage.png",200,150,150,150,10)
pudge = Object("pudge.png",100,150,150,150,10)
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
    anti_mage.move()

 
    
    display.update()
    clock.tick(60)