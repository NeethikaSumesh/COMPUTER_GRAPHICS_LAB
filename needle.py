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
    gluOrtho2D(WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE)

def drawLength(x,y):
    glColor3f(0,0,0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x,y-300)
    glEnd()

def drawPolygon(x,y):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_POLYGON)
    glVertex2f(x,y)
    glVertex2f(x-30,y)
    glVertex2f(x-30,y)
    glVertex2f(x,y-50)
    glVertex2f(x,y-50)
    glVertex2f(x+30,y)
    glVertex2f(x+30,y)
    glVertex2f(x,y)
    glEnd()

def needle():
    global GLOBAL_X
    global GLOBAL_Y

    glClear(GL_COLOR_BUFFER_BIT)
    drawLength(GLOBAL_X,GLOBAL_Y)
    drawPolygon(GLOBAL_X,GLOBAL_Y-300)

    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y

    glTranslatef(GLOBAL_X,GLOBAL_Y,0)
    glRotatef(45,0,0,1)
    glTranslatef(GLOBAL_X,GLOBAL_Y,0)

    glutPostRedisplay()
    glutTimerFunc(50,animate,int(0))
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("NEEDLE")
    glutDisplayFunc(needle)
    glutTimerFunc(50,animate,0)
    glutIdleFunc(needle)
    
    init()
    glutMainLoop()
main()



