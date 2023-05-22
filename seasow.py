from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math 
import sys

WINDOW_SIZE=500
xc=150
yc=20
theta=0

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def triangle():
    glBegin(GL_POLYGON)
    glVertex2f(0,0)
    glVertex2f(-50,50)
    glVertex2f(50,-50)
    
def rod():
    glLineWidth(15)
    glBegin(GL_LINES)
    glVertex2f(xc*math.cos(math.radians(theta))-yc*math.sin(math.radians(theta)),xc*math.sin(math.radians(theta))+yc*math.cos(math.radians(theta)))
    glVertex2f(-xc*math.cos(math.radians(theta))-yc*math.sin(math.radians(theta)),-xc*math.sin(math.radians(theta))+yc*math.cos(math.radians(theta)))
    glEnd()
def sea():
    glClear(GL_COLOR_BUFFER_BIT)
    triangle()
    rod()
    glutSwapBuffers()
def animate(temp):
    global theta,dir

    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))

    if theta<=20:
        dir=1
    if theta>20:
        dir=0
    if(dir==1):
        theta+=0.1
    else:
        theta-=0.1
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("seasow")
    glutDisplayFunc(sea)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(sea)
    init()
    glutMainLoop()
main()
