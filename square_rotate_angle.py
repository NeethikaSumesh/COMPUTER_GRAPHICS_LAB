from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
angle=0
GLOBAL_X=0.0
GLOBAL_Y=0.0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def square():
    global angle
    global GLOBAL_X
    global GLOBAL_Y
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_QUADS)
    glVertex2f((GLOBAL_X-100)*math.cos(math.radians(angle))+(GLOBAL_Y-50)*math.sin(math.radians(angle)),(GLOBAL_Y-50)*math.cos(math.radians(angle))+(GLOBAL_X-100)*math.sin(math.radians(angle)))
    glVertex2f((GLOBAL_X+100)*math.cos(math.radians(angle))+(GLOBAL_Y-50)*math.sin(math.radians(angle)),(GLOBAL_Y-50)*math.cos(math.radians(angle))+(GLOBAL_X+100)*math.sin(math.radians(angle)))
    glVertex2f((GLOBAL_X+100)*math.cos(math.radians(angle))+(GLOBAL_Y+50)*math.sin(math.radians(angle)),(GLOBAL_Y+50)*math.cos(math.radians(angle))+(GLOBAL_X+100)*math.sin(math.radians(angle)))
    glVertex2f((GLOBAL_X-100)*math.cos(math.radians(angle))+(GLOBAL_Y+50)*math.sin(math.radians(angle)),(GLOBAL_Y+50)*math.cos(math.radians(angle))+(GLOBAL_X-100)*math.sin(math.radians(angle)))
    glEnd()
def sqRotate():
    global angle
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    square()
    glutSwapBuffers()

def animate(temp):
    global angle
    global GLOBAL_X
    global GLOBAL_Y

    if angle>=360:
        angle=0
    else:
        angle+=1

    glutPostRedisplay()
    glutTimerFunc(10,animate,int(0))
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("sq")
    glutDisplayFunc(sqRotate)
    glutTimerFunc(10,animate,int(0))
    glutIdleFunc(sqRotate)

    init()
    glutMainLoop()
main()





