from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=WINDOW_SIZE+50
GLOBAL_Y=0.0
AMP=200
i=0.0
theta=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def path():
    glColor3f(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(-WINDOW_SIZE,250)
    glVertex2f(WINDOW_SIZE,250)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(-WINDOW_SIZE,-50)
    glVertex2f(WINDOW_SIZE,-50)
    glEnd()
    
def circle(x,y):
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(80*math.cos(math.pi*i/180)+x,80*math.sin(math.pi*i/180)+y)

    glEnd()

def bounceball():
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    path()
    circle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global AMP
    global i

    GLOBAL_X=GLOBAL_X+2
    GLOBAL_Y=(AMP)*math.sin(math.radians(i))
    AMP-=0.25
    i+=1

    if(i>180):
        i=0
    if(GLOBAL_X>WINDOW_SIZE):
        GLOBAL_X=GLOBAL_X-WINDOW_SIZE
    if(GLOBAL_Y<0):
        GLOBAL_Y=0
    glutPostRedisplay()
    glutTimerFunc(10,animate,int(0))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("bounce ball")
    glutDisplayFunc(bounceball)
    glutTimerFunc(10,animate,int(0))
    glutIdleFunc(bounceball)
    init()
    glutMainLoop()
main()
