from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

GLOBAL_X=0.0
GLOBAL_Y=0.0
THETA=0.0
WINDOW_SIZE=500

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)


def circle(x,y,s):
    i=0.0
    if s==0:
        y=y-100
        x=x-50
    else:
        y=y-100
        x=x+50
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)

    for i in range(0,360,1):
        glVertex2f(35*math.cos(math.pi*i/180)+x,35*math.sin(math.pi*i/180)+y)
    glEnd()

def Rectangle(x,y):

    glBegin(GL_QUADS)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)
    glVertex2f(x+100,y-100)
    glVertex2f(x-100,y-100)

    glEnd()
   # glFlush()



def drawCar():

    global GLOBAL_X
    global GLOBAL_Y
    global THETA 

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)


    Rectangle(GLOBAL_X,GLOBAL_Y)
    circle(GLOBAL_X,GLOBAL_Y,0)
    circle(GLOBAL_X,GLOBAL_Y,1)

    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global WINDOW_SIZE

    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if(GLOBAL_X+100<WINDOW_SIZE):
        GLOBAL_X=GLOBAL_X+1
    else:
        GLOBAL_X=-400


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Car")
    glutDisplayFunc(drawCar)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()

