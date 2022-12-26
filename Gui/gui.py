import pygame
from pygame.locals import *
from time import sleep
from datetime import datetime as d 

pygame.init()

# Load images
bg_img = pygame.image.load("assets/bg.jpg")
logo = pygame.image.load("assets/logo.png")
bin = pygame.image.load("assets/bin.png")
xplogo = pygame.image.load("assets/xp.png")
browser = pygame.image.load("assets/explorer.png")
terminal = pygame.image.load("assets/terminal.png")
files = pygame.image.load("assets/files.png")
sound0 = pygame.image.load("assets/sound0.png")
sound25 = pygame.image.load("assets/sound25.png")
sound50 = pygame.image.load("assets/sound50.png")
sound100 = pygame.image.load("assets/sound100.png")
battery = pygame.image.load("assets/battery.png")
network = pygame.image.load("assets/network.png")

# Scale images
bin = pygame.transform.scale(bin, (55, 55))
bg_img = pygame.transform.scale(bg_img, (800, 480))
xp_logo = pygame.transform.scale(xplogo, (30, 30))
browser = pygame.transform.scale(browser, (30, 30))
terminal = pygame.transform.scale(terminal, (30, 30))
files = pygame.transform.scale(files, (30, 30))
sound0 = pygame.transform.scale(sound0, (40, 20))
sound25 = pygame.transform.scale(sound25, (40, 20))
sound50 = pygame.transform.scale(sound50, (40, 20))
sound100 = pygame.transform.scale(sound100, (40, 20))
battery = pygame.transform.scale(battery, (50, 30))
network = pygame.transform.scale(network, (20, 20))

# General os colors
taskbar_color = (83, 104, 120)
black = (0, 0, 0)

# Set up the drawing window
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption("It is not linux!")
pygame.display.set_icon(logo)

# Game running variable
running  = True

# General functions
def button(x, y, w, h, ac, img):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    rect = pygame.Rect(x, y, w, h)
    on_button = rect.collidepoint(mouse)
    pygame.draw.rect(screen, ac, rect)
    screen.blit(img, img.get_rect(center = rect.center))
    if on_button:  
        if click[0] == 1:
            return True

# Main loop
while running:  
    screen.blit(bg_img,(0,0))
    pygame.draw.rect(screen, taskbar_color, pygame.Rect(0, 445, 800, 35))


    binb = button(40, 40, 25, 25, taskbar_color, bin)
    xplogo = button(10, 450, 25, 25, taskbar_color, xp_logo)
    browserb = button(48, 450, 25, 25, taskbar_color, browser)
    filesb = button(86, 450, 25, 25, taskbar_color, files)
    terminalb = button(120, 450, 25, 25, taskbar_color, terminal)


    if binb == True:
        print("Bin button.")
        sleep(0.5)
    elif xplogo == True:
        print("Menu button.")
        sleep(0.5)
    elif browserb == True:
        print("Close that bullshit!")
        sleep(0.5)
    elif filesb == True:
        print("Files button.")
        sleep(0.5)
    elif terminalb == True:
        print("Terminal button.")
        sleep(0.5)

    font = pygame.font.SysFont(None, 16)
    date = d.now()
    img = font.render(date.strftime("%H:%M"), True, black)
    screen.blit(img, (760, 451))

    font = pygame.font.SysFont("Roboto", 16)
    date = d.now()
    img = font.render(date.strftime("%Y-%m-%d"), True, black)
    screen.blit(img, (730, 462))

    screen.blit(battery, (680, 447))

    sound100b = button(655, 450, 25, 25, taskbar_color, sound100)

    networkb = button(620, 450, 25, 25, taskbar_color, network)


    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False


    pygame.display.update()


