from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=0
GLOBAL_Y=0
angle1=90
theta=90

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)


def drawClock():
   global GLOBAL_X
   global GLOBAL_Y
   global angle1
   global theta

   glClear(GL_COLOR_BUFFER_BIT)
   glColor3f(1.0,1.0,0.0)
   i=0.0
   glBegin(GL_TRIANGLE_FAN)
   glVertex2f(0,0)
   for i in range(0,360,1):
    glVertex2f(80*math.cos(math.pi*i/180),80*math.sin(math.pi*i/180))

   glEnd()

   glColor3f(1.0,0.0,0.0)
   glLineWidth(2)
   glBegin(GL_LINES)
   glVertex2f(GLOBAL_X,GLOBAL_Y)
   glVertex2f(60*math.cos(math.pi*angle1/180),60*math.sin(math.pi*angle1/180))
   glEnd()

   glColor3f(0.0,0.0,1.0)
   glLineWidth(4)
   glBegin(GL_LINES)
   glVertex2f(70*math.cos(math.pi*theta/180),70*math.sin(math.pi*theta/180))
   glVertex2f(GLOBAL_X,GLOBAL_Y)
   glEnd()


   glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y
    global angle1
    global theta

    if angle1>=360:
        angle1=0
    else:
        angle1-=1
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),animate,int(0))


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(500,500)
    glutCreateWindow("clock")
    glutDisplayFunc(drawClock)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(drawClock)
    init()
    glutMainLoop()
main()
