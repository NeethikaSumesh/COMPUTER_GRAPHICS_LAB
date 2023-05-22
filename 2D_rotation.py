import OpenGL 
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math

def ClearScreen():
    glClearColor(1.0,1.0,1.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def call_function(x1,y1,x2,y2,x3,y3):
    plotted_triangle(x1,y1,x2,y2,x3,y3)
    rotation(x1,y1,x2,y2,x3,y3)

def plotted_triangle(x1,y1,x2,y2,x3,y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glFlush()

def rotation(x1,y1,x2,y2,x3,y3):
    theta = int(input("Enter the angle: "))
    angle = ((math.pi/180)*theta)

    x11 = x1*math.cos(angle)-y1*math.sin(angle)
    y11 = x1*math.sin(angle)+y1*math.cos(angle)
    x22 = x2*math.cos(angle)-y2*math.sin(angle)
    y22 = x2*math.sin(angle)+y2*math.cos(angle)
    x33 = x3*math.cos(angle)-y3*math.sin(angle)
    y33 = x3*math.sin(angle)+y3*math.cos(angle)

    glColor3f(0.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x11,y11)
    glVertex2f(x22,y22)
    glVertex2f(x33,y33)

    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    x3 = float(input("Enter x3: "))
    y3 = float(input("Enter y3: "))

    glutCreateWindow("ROTATION")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()
main()
