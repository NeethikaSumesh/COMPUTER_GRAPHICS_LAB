from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

GLOBAL_X=0.0
GLOBAL_Y=0.0
WINDOW_SIZE=500
angle=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def circle(x,y):

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x-50,y-100)
    for i in range(0,360,1):
        glVertex2f(35*math.cos(math.pi*i/180)+x-50,35*math.sin(math.pi*i/180)+y-100)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0,0.0,0.0)
    glVertex2f(x+50,y-100)
    for i in range(0,360,1):
        glVertex2f(35*math.cos(math.pi*i/180)+x+50,35*math.sin(math.pi*i/180)+y-100)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x-50,y-100)
    glVertex2f(35*math.cos(math.pi*angle/180)+x-50,35*math.sin(math.pi*angle/180)+y-100)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0.0,0.0,0.0)
    glVertex2f(x+50,y-100)
    glVertex2f(35*math.cos(math.pi*angle/180)+x+50,35*math.sin(math.pi*angle/180)+y-100)
    glEnd()

def Rectangle(x,y):
    glBegin(GL_QUADS)
    glColor3f(0.0,1.0,0.0)
    glVertex2f(x-100,y+50)
    glVertex2f(x+100,y+50)
    glVertex2f(x+100,y-100)
    glVertex2f(x-100,y-100)
    glEnd()

def Drawcar():

    global GLOBAL_X
    global GLOBAL_Y
    global MAX_THETA
    global THETA 
    #global DIR 

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)

    Rectangle(GLOBAL_X,GLOBAL_Y)
    circle(GLOBAL_X,GLOBAL_Y)
    circle(GLOBAL_X,GLOBAL_Y)

    glutSwapBuffers()

def animate(value,key):
    global GLOBAL_X
    global GLOBAL_Y
    global WINDOW_SIZE
    global angle

    if key == 'a':
        if(GLOBAL_X-100>-WINDOW_SIZE):
            GLOBAL_X=GLOBAL_X+value
            if angle==0:
                angle=360
            else:
                angle = angle+10
        else:
            GLOBAL_X=400
            
    if key == 'd':
        if(GLOBAL_X+100<WINDOW_SIZE):
            GLOBAL_X=GLOBAL_X+value
            if angle==360:
                angle=0
            else:
                angle=angle-10
        else:
            GLOBAL_X=-400
    glutPostRedisplay()
    #glutTimerFunc(int(1000/60),animate,int(0))

def keyboard(key,x,y):
    key = key.decode()
    if key == 'd':
        animate(3,'d')
    elif key == 'a':
        animate(-3,'a')
    elif key == 'f':
        glutFullScreen()
    elif key =='z':
        glutLeaveMainLoop()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Simple car")
    glutDisplayFunc(Drawcar)
    glutKeyboardFunc(keyboard)
    #glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()
