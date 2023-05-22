from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def ClearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def call_function(x1,y1,x2,y2,x3,y3):
    plot_triangle(x1,y1,x2,y2,x3,y3)
    scaling(x1,y1,x2,y2,x3,y3)

def plot_triangle(x1,y1,x2,y2,x3,y3):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPointSize(10.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glFlush()

def scaling(x1,y1,x2,y2,x3,y3):
    sx = float(input("Enter scaling in x: "))
    sy = float(input("Enter scaling in y: "))
    glColor3f(1.0,0.0,1.0)
    glPointSize(10)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1*sx, y1*sy)
    glVertex2f(x2*sx, y2*sy)
    glVertex2f(x3*sx, y3*sy)    
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    
    x1=float(input("Enter x1: "))
    y1=float(input("Enter y1: "))
    x2=float(input("Enter x2: "))
    y2=float(input("Enter y2: "))
    x3=float(input("Enter x3: "))
    y3=float(input("Enter y3: "))

    glutCreateWindow("Scaling")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()

main()

