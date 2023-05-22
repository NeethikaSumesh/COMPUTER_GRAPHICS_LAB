from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import sys

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
THETA=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def Rectangle(x,y):

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,1.0)

    glBegin(GL_QUADS)
    glVertex2f((x-100)*math.cos(THETA)+(y-50)*math.sin(THETA),(y-50)*math.cos(THETA)+(x-100)*math.sin(THETA))
    glVertex2f((x+100)*math.cos(THETA)+(y-50)*math.sin(THETA),(y-50)*math.cos(THETA)+(x+100)*math.sin(THETA))
    glVertex2f((x+100)*math.cos(THETA)+(y+50)*math.sin(THETA),(y+50)*math.cos(THETA)+(x+100)*math.sin(THETA))
    glVertex2f((x-100)*math.cos(THETA)+(y+50)*math.sin(THETA),(y+50)*math.cos(THETA)+(x-100)*math.sin(THETA))

    glEnd()

def drawRect():
    global GLOBAL_X
    global GLOBAL_Y
    global THETA

    Rectangle(GLOBAL_X,GLOBAL_Y)

    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if THETA>=360:
        THETA=0
    THETA+=1

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("RECTANGLE")
    glutDisplayFunc(drawRect)
    glutTimerFunc(0,animate,0)
    init()
    glutMainLoop()
main()

