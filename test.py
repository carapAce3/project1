from pygame import *
import pygame_menu
from ping_pong import starting
init()
font1 = pygame_menu.font.FONT_MUNRO
window = display.set_mode((600,400))

def start():
    window = display.set_mode((600,520))
    starting()
window = display.set_mode((600,400))
def end():
    exit()
def help():
    mytheme = pygame_menu.Theme(widget_font=font1,background_color=(0,0,0),
                                title_background_color = (153,0,153),
                                widget_font_color = (153,0,153))
    
    help_menu = pygame_menu.Menu('Main Menu', 600, 400, theme=mytheme)
    help_menu.add.label('Information')
    help_menu.add.label('Press [Start] to start')
    help_menu.add.label('Press key [Stop] to stop')
    
    def back():
        menu.enable()
        help_menu.disable()
        menu.mainloop(window)
    help_menu.add.button('Back', back)
    menu.disable()
    help_menu.mainloop(window)

font2 = pygame_menu.pygame_menu.font.FONT_8BIT
        
mytheme = pygame_menu.Theme(widget_font=font2,background_color=(153,0,153),
                                title_background_color = (0,0,0),
                                widget_font_color = (0,0,0))


menu = pygame_menu.Menu('Main Menu', 600, 400, theme=mytheme)
menu.add.button('Start',start)
menu.add.button('Stop',end)
menu.add.button('Help', help)


menu.mainloop(window)