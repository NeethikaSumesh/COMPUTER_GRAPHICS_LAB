from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import math
import sys

GLOBAL_X=0.0
GLOBAL_Y=0.0
WINDOW_SIZE=500
time=0.0
speed=math.pi/8
radius=50

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawline(x,y):
    glColor3f(1.0,1.0,1.0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x,y)
    glVertex2f(x,y-300)
    glEnd()

def drawCircle1(x,y):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(radius*math.cos(math.pi*i/180)+x,radius*math.sin(math.pi*i/180)+y)
    glEnd()

def drawCircle2(x,y):
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x,y)
    for i in range(0,361,1):
        glVertex2f(radius*math.cos(math.pi*i/180)+x,radius*math.sin(math.pi*i/180)+y)
    glEnd()

def solar():
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    drawline(GLOBAL_X,GLOBAL_Y)
    drawCircle1(GLOBAL_X,GLOBAL_Y)
    drawCircle2(GLOBAL_X,GLOBAL_Y-300)

    glutSwapBuffers()

def animate(temp):
    global GLOBAL_X
    global GLOBAL_Y

    glutPostRedisplay()
    glutTimerFunc(50,animate,int(0))

    glTranslatef(GLOBAL_X,GLOBAL_Y,0)
    glRotatef(45,0,0,1)
    glTranslatef(-GLOBAL_X,-GLOBAL_Y,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Solar")
    glutDisplayFunc(solar)
    glutTimerFunc(50,animate,0)
    glutIdleFunc(solar)
    init()
    glutMainLoop()
main()



    
