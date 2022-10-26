"""
OpenGL en pygame
Author: Alecraft Gomez
Fecha: 25/10/2022
"""

# Imports
import pygame as glfw
from OpenGL.GL import *


# Window
glfw.init()
window = glfw.display.set_mode((800, 600), glfw.OPENGL | glfw.DOUBLEBUF)

# Draw a pixel
def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 10, 10)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


# Draw a bar
def pixelBar(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 10, 100)
    glClearColor(color[0], color[1], color[2], 1)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)


# Clean screen
def CleanScreen():
    glClearColor(0.0, 0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)


# Flip framebuffer
def FlipScreen():
    glfw.display.flip()


x = 0
speed = 1
funcionar = True

# Until window is closed
while funcionar:
    CleanScreen()
    pixel(x, 30, (0, 1, 0))
    x += speed

    if x == 800:
        speed = -1

    if x == 0:
        speed = 1

    FlipScreen()
    for e in glfw.event.get():

        if e.type == glfw.QUIT:
            funcionar = False

# WIP function to recreate PONG game
def PongGame():
    CleanScreen()
    pixelBar(10, x, (1, 1, 1))
    pixelBar(780, x - 1, (1, 1, 1))
    pixel(x, x + 5, (0, 1, 0))
    x += speed

    if x == 800:
        speed = -1

    if x == 0:
        speed = 1

    FlipScreen()
    for e in glfw.event.get():
        if e.type == glfw.QUIT:
            funcionar = False
