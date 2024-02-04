from pygame import *
from random import randint
'''Необхідні класи'''


#музика
mixer.init()
#фонова музика
mixer.music.load('odetari.mp3')
mixer.music.play()

#звук
sound1 = mixer.Sound('sound.mp3')
sound1.play()


 
# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #разом 55,55 - параметри
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# клас-спадкоємець для спрайту-гравця (керується стрілками)    
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        
    
 
#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
picture = transform.scale(image.load("p1.png"),(600,500))
picture2 = transform.scale(image.load("p2.png"),(600,500))


#текст
font.init()
font1 = font.Font(None, 30) #шрифт і розмір тексту

score1 = 0
score2 = 0
t = "Рахунок: " + str(score1) + ' - ' + str(score2)
text = font1.render(t, True, (0,0,0))





player1 = Player('racket.png', 0, 180, 10, 50, 100)
player2 = Player('racket.png', 545, 180, 10, 50, 100)
ball = GameSprite("ball1.png",300,200,10,60,60)

x = 3
y = 3


window.fill(back)




#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update_l()
        player2.update_r()

        t = "Рахунок: " + str(score1) + ' - ' + str(score2)
        text = font1.render(t, True, (0,0,0))
        window.blit(text,(100,100))

        ball.rect.x -= x
        ball.rect.y += y

        if ball.rect.y > 450 or ball.rect.y < 0:
            y *= -1
        
        if ball.rect.x < -40:
            ball.rect.x = 200
            ball.rect.y = 200
            score2 += 1
        if ball.rect.x > 600:
            ball.rect.x = 200
            ball.rect.y = 200
            score1 += 1
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            x *= -1
        if score1 >= 3:
            window.blit(picture,(0,0))
        if score2 >= 3:
            window.blit(picture2,(0,0))


        

        




    display.update()
    clock.tick(60)
    
