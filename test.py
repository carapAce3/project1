from pygame import *
import pygame_menu

init()
font = pygame_menu.font.FONT_MUNRO
window = display.set_mode((600,400))

def start():
    print('starting...')
def end():
    exit()
def help():
    mytheme = pygame_menu.Theme(widget_font=font,background_color=(0,0,0,0),
                                title_background_color = (0,0,0))
    
    help_menu = pygame_menu.Menu('Головне меню', 600, 400, theme=mytheme)
    help_menu.add.label('Information')
    help_menu.add.label('Press [Start] to start')
    help_menu.add.label('Press key [Stop] to stop')
    
    def back():
        menu.enable()
        help_menu.disable()
        menu.mainloop(window)
    help_menu.add.button('Назад', back)
    menu.disable()
    help_menu.mainloop(window)
        


menu = pygame_menu.Menu('Головне меню', 600, 400, theme=pygame_menu.themes.THEME_SOLARIZED.copy())
menu.add.button('Запустити гру',start)
menu.add.button('Завершити гру',end)
menu.add.button('Допомога', help)


menu.mainloop(window)