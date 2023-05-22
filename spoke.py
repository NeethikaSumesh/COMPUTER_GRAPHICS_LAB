from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
THETA=0.0
angle1=90
angle2=180
angle3=270
angle4=360


def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def CircleSpoke():
    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    i=0.0
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    for i in range(0,360,1):
        glVertex2f(80*math.cos(math.pi*i/180)+GLOBAL_X,80*math.sin(math.pi*i/180)+GLOBAL_Y)
    glEnd()

    glColor3f(1.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glVertex2f(80*math.cos(math.pi*angle1/180)+GLOBAL_X,80*math.sin(math.pi*angle1/180)+GLOBAL_Y)
    glEnd()

    glColor3f(1.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glVertex2f(80*math.cos(math.pi*angle2/180)+GLOBAL_X,80*math.sin(math.pi*angle2/180)+GLOBAL_Y)
    glEnd()

    glColor3f(1.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glVertex2f(80*math.cos(math.pi*angle3/180)+GLOBAL_X,80*math.sin(math.pi*angle3/180)+GLOBAL_Y)
    glEnd()


    glColor3f(1.0,0.0,0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex2f(GLOBAL_X,GLOBAL_Y)
    glVertex2f(80*math.cos(math.pi*angle4/180)+GLOBAL_X,80*math.sin(math.pi*angle4/180)+GLOBAL_Y)
    glEnd()


    glutSwapBuffers()

def animate(temp):

    global GLOBAL_X
    global GLOBAL_Y
    global THETA
    global angle1
    global angle2
    global angle3
    global angle4


    
    GLOBAL_X=GLOBAL_X+1
    angle1+=1
    angle2+=1
    angle3+=1
    angle4+=1

    if(GLOBAL_X>500):
        GLOBAL_X=-400
        


    glutPostRedisplay()
    glutTimerFunc(10,animate,int(0))
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Circle")
    glutDisplayFunc(CircleSpoke)
    glutTimerFunc(10,animate,0)
    glutIdleFunc(CircleSpoke)
    init()
    glutMainLoop()
main()

