from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys

WINDOW_SIZE=500

def init():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def square():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    
    glBegin(GL_QUADS)
    glVertex2f(100,100)
    glVertex2f(200,100)
    glVertex2f(200,200)
    glVertex2f(100,200)
    glEnd()

    glTranslatef(150,150,0)
    glRotatef(45,0,0,1)
    glTranslatef(-150,-150,0)

    glFlush()

def animate(temp):
    glutPostRedisplay()
    glutTimerFunc(50,animate,int(0))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Square rotate")
    glutDisplayFunc(square)
    glutTimerFunc(50,animate,0)
    init()
    glutMainLoop()
main()

