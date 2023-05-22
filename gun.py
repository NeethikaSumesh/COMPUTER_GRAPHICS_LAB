from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import sys

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def body():
    glColor3f(206/255,163/255,69/255)
    glBegin(GL_QUADS)
    glVertex2f(-200,0)
    glVertex2f(-160,0)
    glVertex2f(-160,100)
    glVertex2f(-200,100)
    glEnd()

    glBegin(GL_QUADS)
    glVertex2f(-200,100)
    glVertex2f(-20,100)
    glVertex2f(-20,140)
    glVertex2f(-200,140)
    glEnd()

def circle(x,y):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(10*math.cos(math.pi*i/180)+x,10*math.sin(math.pi*i/180)+y)
    glEnd()

def gun():
    global GLOBAL_X
    global GLOBAL_Y

    glClear(GL_COLOR_BUFFER_BIT)
    body()
    circle(GLOBAL_X-20,GLOBAL_Y+120)
    glutSwapBuffers()
def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y

    if GLOBAL_X+10<500:
        GLOBAL_X+=1
    glutPostRedisplay()
    glutTimerFunc(50,animate,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("GUN")
    glutDisplayFunc(gun)
    glutTimerFunc(50,animate,0)
    glutIdleFunc(gun)
    init()
    glutMainLoop()
main()

