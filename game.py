from pygame import *

window = display.set_mode((1100,700), RESIZABLE)
picture = transform.scale(image.load("bg1.png"),(1100,700))
anti_mage = transform.scale(image.load("anti-mage.png"),(100,150))
pudge = transform.scale(image.load("pudge.png"),(100,150))
pudge1 = transform.scale(image.load("hook.webp"),(100,150))
clock = time.Clock()
x1, y1 = 100,100
x2, y2 = 100,100
x3, y3 = 100,100
#створення головного циклу
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False



    window.blit(picture,(0,0))
    window.blit(anti_mage,(x1,y1))
    window.blit(pudge,(x2,y2))
    
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1 > 0:
        x1 -= 5
    if key_pressed[K_RIGHT] and x1 < 1000:
        x1 += 5
    if key_pressed[K_UP] and y1 > 0:
        y1 -= 5
    if key_pressed[K_DOWN] and y1 < 600:
        y1 += 5

    if key_pressed[K_a] and x2 > 0:
        x2 -= 5
    if key_pressed[K_d] and x2 < 1000:
        x2 += 5
    if key_pressed[K_w] and y2 > 0:
        y2 -= 5
    if key_pressed[K_s] and y2 < 600:
        y2 += 5
    if key_pressed[K_q]:
        window.blit(pudge1,(x2 - 80,y2 + 50))
        



    

    
    display.update()
    clock.tick(60)