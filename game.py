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
            self.image = transform.scale(image.load('anti-mage2.png'),(100,100))
            for w in walls:
                if sprite.collide_rect(anti_mage,w):
                    self.rect.x += self.speed
        if keys[K_d] and self.rect.x < 1000:
            self.rect.x += self.speed
            self.image = transform.scale(image.load('anti-mage.png'),(100,100))
            for w in walls:
                if sprite.collide_rect(anti_mage,w):
                    self.rect.x -= self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
            for w in walls:
                if sprite.collide_rect(anti_mage,w):
                    self.rect.y += self.speed
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed
            for w in walls:
                if sprite.collide_rect(anti_mage,w):
                    self.rect.y -= self.speed

    direction = 'right'
    def move2(self):
        if self.rect.x > 1000:
            self.direction = 'right'
        if self.rect.x < -150:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
    
    direction2 = 'up'
    def move3(self):
        if self.rect.y > 600:
            self.direction = 'down'
        if self.rect.y < 220:
            self.direction = 'up'
        
        if self.direction == 'up':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

    def fire(self):
        bullet = Bullet("hook.webp", self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)

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

class Bullet(Object):
    def update(self):
        self.rect.x += 10
        if self.rect.x > 1100:
            self.kill()

bullets = sprite.Group()



menu = display.set_mode((400,400), RESIZABLE)
display.set_caption('Лабіринт')


start_button = Rect(150, 100, 100, 50)
exit_button = Rect(150, 200, 100, 50)

font.init()
menu_font = font.Font(None, 24)

mg = True
while mg:
    for e in event.get():
        if e.type == QUIT:
            mg = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            if exit_button.collidepoint(mouse.get_pos()):
                game = False
                mg = False
                
            elif start_button.collidepoint(mouse.get_pos()):
                mg = False
                game = True
                
    menu.fill((0,0,0))
    draw.rect(menu, (125,45,80), start_button)
    draw.rect(menu, (125,45,80), exit_button)

    start_text = menu_font.render('Почати гру', True,(0,0,0))
    exit_text = menu_font.render('Вийти', True,(0,0,0))
    menu.blit(start_text,(start_button.x+10, start_button.y+10))
    menu.blit(exit_text,(exit_button.x+10, exit_button.y+10))

    display.update()




window = display.set_mode((1980,1080), RESIZABLE)
picture = transform.scale(image.load("bg2.webp"),(1980,1080))

anti_mage = Object("anti-mage.png",80,300,100,100,5)
pudge = Object("pudge.png",800,50,100,100,4)
Krip = Object("Krip1.webp",500,150,100,100,4)
Rune1 = Object("rune.png",1030,20,70,70,4)
Rune2 = Object("rune.png",300,450,70,70,4)
next_level = Object("next_level.png",230,575,200,200,4)

wall = Wall(0, 0, 0, 200, 200, 750, 40)
###wall2 = Wall(0, 0, 0, 200, 200, 40, 1000)
wall3 = Wall(0, 0, 0, 200, 350, 250, 40)
wall4 = Wall(0, 0, 0, 450, 350, 40, 250)
wall5 = Wall(0, 0, 0, 230,560, 250, 40)
wall6 = Wall(0, 0, 0, 450,550, 40, 250)
walls = []
walls.append(wall)
###walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)
walls.append(wall6)

clock = time.Clock()
#створення головного циклу

level1 = True
level2 = False
while game:
    if level1:
        display.update()
        clock.tick(60)
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    anti_mage.fire()


        window.blit(picture,(0,0))
        bullets.update()
        bullets.draw(window)

        anti_mage.reset()
        pudge.reset()
        Krip.reset()
        Rune1.reset()
        Rune2.reset()
        next_level.reset()
        anti_mage.move()
        pudge.move2()
        Krip.move3()
        wall.draw_wall()
        ###wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()

        if sprite.collide_rect(anti_mage, pudge) or sprite.collide_rect(anti_mage, Krip):
            game = False
        if sprite.collide_rect(anti_mage, Rune1):
            Rune1.rect.x = -500
            wall3.rect.x = -1243
        if sprite.collide_rect(anti_mage, Rune2):
            Rune2.rect.x = -500
            wall6.rect.x = -2347
        if sprite.collide_rect(anti_mage, next_level):
            next_level.rect.x = -4325
            level1 = False
            level2 = True

            #####
            window = display.set_mode((1980,1080), RESIZABLE)
            picture = transform.scale(image.load("bg2.webp"),(1980,1080))

            anti_mage = Object("anti-mage.png",50,300,100,100,5)
            pudge = Object("pudge.png",800,50,100,100,4)
            Krip = Object("Krip1.webp",500,150,100,100,4)
            Rune1 = Object("rune.png",1030,20,70,70,4)
            Rune2 = Object("rune.png",300,450,70,70,4)
            next_level = Object("next_level.png",230,550,200,200,4)

            wall = Wall(0, 0, 0, 200, 3, 40, 250)
            wall2 = Wall(0, 0, 0, 200, 400, 40, 300)
            wall3 = Wall(0, 0, 0, 200, 250, 250, 40)
            #wall4 = Wall(0, 0, 0, 450, 350, 40, 250)
            #wall5 = Wall(0, 0, 0, 230,560, 250, 40)
            #wall6 = Wall(0, 0, 0, 450,550, 40, 250)
            walls = []
            walls.append(wall)
            walls.append(wall2)
            walls.append(wall3)
            #walls.append(wall4)
            #walls.append(wall5)
            #walls.append(wall6)
            #######


    if level2:
        display.update()
        clock.tick(60)
        for e in event.get():
            if e.type == QUIT:
                game = False



        window.blit(picture,(0,0))
        anti_mage.reset()
        pudge.reset()
        Krip.reset()
        Rune1.reset()
        Rune2.reset()
        next_level.reset()
        anti_mage.move()
        pudge.move2()
        Krip.move3()
        wall.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        #wall5.draw_wall()
        #wall6.draw_wall()

        if sprite.collide_rect(anti_mage, pudge) or sprite.collide_rect(anti_mage, Krip):
            game = False
        if sprite.collide_rect(anti_mage, Rune1):
            Rune1.rect.x = -500
            wall3.rect.x = -1243
        if sprite.collide_rect(anti_mage, Rune2):
            Rune2.rect.x = -500
            wall6.rect.x = -2347
        if sprite.collide_rect(anti_mage, next_level):
            next_level.rect.x = -4325


    
        
        