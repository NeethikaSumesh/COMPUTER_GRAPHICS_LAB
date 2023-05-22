from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import sys

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
THETA=0.0
SPEED=1.0
RADIUS=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

THETA = float(int(input("Enter angle of inclination: ")))
RADIUS = float(int(input("Enter radius: ")))

def path():
    global THETA
    glColor3f(0,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(-500,-500)
    glVertex(500,500*math.tan(THETA))
    glEnd()

def Ball(x,y):
    global RADIUS
    global THETA
    glColor3f(1.0,0.0,0.0)
    i=0.0
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0,360,1):
        glVertex2f(RADIUS*math.cos(math.pi*i/180)+x,RADIUS*math.sin(math.pi*i/180)+y)
    glEnd()

def InclinedBall():
    global GLOBAL_X
    global GLOBAL_Y
    global THETA

    glClear(GL_COLOR_BUFFER_BIT)
    path()
    Ball(GLOBAL_X+500,GLOBAL_Y+500*math.tan(THETA))
    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global SPEED

    GLOBAL_X=GLOBAL_X-0.8
    GLOBAL_Y=GLOBAL_Y-0.8

    glutPostRedisplay()
    glutTimerFunc(10,animate,int(0))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("ball")
    glutDisplayFunc(InclinedBall)
    glutTimerFunc(10,animate,int(0))
    glutIdleFunc(InclinedBall)
    init()
    glutMainLoop()
main()

