import pygame
import socket
import time

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("game")


main_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_socket.connect(("localhost",10000))

run = True
while run:
    main_socket.send("hello".encode())
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False
    x = main_socket.recv(1024).decode()
    screen.fill("white")
    pygame.draw.circle(screen,"red",(400,300),50)
    pygame.display.flip()

pygame.quit()
