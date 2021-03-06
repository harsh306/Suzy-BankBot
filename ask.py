import aiml,os
import pygame
from pygame.locals import *

def name():
    pygame.init()
    screen = pygame.display.set_mode((1080, 560))
    name = ""
    font = pygame.font.Font(None, 50)
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_SPACE:
                    name= name[0:]+" " 	
                elif evt.key == K_DELETE:
                    name = ""             
                elif evt.key == K_RETURN:
                    x=name
                    name=suzy.respond(x)
                    os.system("say  %s" %name)	
            elif evt.type == QUIT:
                return
        screen.fill((0, 0, 0))
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    suzy=aiml.Kernel()
    suzy.learn("myAiml.aiml")
    name()
    pygame.quit()
