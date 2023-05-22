from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=0
GLOBAL_Y=0
FPS=60
DIR=1

PEND_LEN = float(int(input("Enter pend length: ")))
BOB_RAD = float(int(input("Enter the bob radius: ")))
MAX_THETA = float(int(input("Enter max angle of swing: ")))
THETA=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def circle(x,y):
    i=0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,360,1):
        glVertex2f(BOB_RAD*math.cos(math.radians(i))+x,BOB_RAD*math.sin(math.radians(i))+y)
    glEnd()

def drawPendulum():
    global GLOBAL_X
    global GLOBAL_Y
    global MAX_THETA
    global THETA
    global DIR

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)

    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glEnd()

    circle(GLOBAL_X,GLOBAL_Y)
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global MAX_THETA
    global THETA
    global DIR

    
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),animate,int(0))

    if DIR == 1:
        if(THETA <= MAX_THETA):
            THETA=THETA+1
        else:
            DIR=0

    elif DIR ==0:
        if(THETA >= -MAX_THETA):
            THETA = THETA-1
        else:
            DIR=1

    GLOBAL_X=PEND_LEN*math.sin(math.radians(THETA))
    GLOBAL_Y=-PEND_LEN*math.cos(math.radians(THETA))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(drawPendulum)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawPendulum)
    init()
    glutMainLoop()
main()
