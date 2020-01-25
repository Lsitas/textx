import pygame
import time
import socket
pygame.init()

SIZE = (600,400)
BLACK = (0,0,0)


def draw(screen):
    screen.fill(BLACK)
    pygame.display.flip()





if __name__ == "__main__":
    s = socket.socket()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Chat Box")
    done = False

    while not done:
        time.sleep(0.05)
        done = keyHandler()
        draw(screen)