from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=-400
GLOBAL_Y=0
ANGLE=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def circle(x,y):

    glColor3f(1.0,1.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(100*math.cos(math.pi*i/180)+x,100*math.sin(math.pi*i/180)+y)
    glEnd()


    glColor3f(1.0,0.0,0.0)
    glLineWidth(2)

    glBegin(GL_LINES)
    glVertex2f(x,y)
    x1=100*math.sin(ANGLE)+x
    y1=100*math.cos(ANGLE)+y
    glVertex2f(x1,y1)
    glEnd()

   

def drawtyre():
    global GLOBAL_X
    global GLOBAL_Y

    circle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global ANGLE

    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if GLOBAL_X<400:
        GLOBAL_X+=1
        ANGLE+=0.01

    else:
        GLOBAL_X=-400
        GLOBAL_Y=0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Circle")
    glutDisplayFunc(drawtyre)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawtyre)
    init()
    glutMainLoop()
main()




from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=-400
GLOBAL_Y=0
ANGLE=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def circle(x,y):

    glColor3f(1.0,1.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(100*math.cos(math.pi*i/180)+x,100*math.sin(math.pi*i/180)+y)
    glEnd()


    glColor3f(1.0,0.0,0.0)
    glLineWidth(2)

    glBegin(GL_LINES)
    glVertex2f(x,y)
    x1=100*math.sin(ANGLE)+x
    y1=100*math.cos(ANGLE)+y
    glVertex2f(x1,y1)
    glEnd()

   

def drawtyre():
    global GLOBAL_X
    global GLOBAL_Y

    circle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global ANGLE

    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if GLOBAL_X<400:
        GLOBAL_X+=1
        ANGLE+=0.01

    else:
        GLOBAL_X=-400
        GLOBAL_Y=0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Circle")
    glutDisplayFunc(drawtyre)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawtyre)
    init()
    glutMainLoop()
main()




