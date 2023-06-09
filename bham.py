from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,1.0)
    glPointSize(3.0)
    gluOrtho2D(-100,100,-100,100)

def plot_point():
    global x1,y1,x2,y2
    x=x1 
    y=y1 
    dy=y2-y1 
    dx=x2-x1

    p=2*dy-dx
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    while x<x2:
        x+=1
        if p<0:
            p+=2*dy
        else:
            p+=2*dy-2*dx
        glVertex2f(x,y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow("BHAM LINE")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)

    global x1,y1,x2,y2
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))  

    glutDisplayFunc(plot_point)
    init_display()
    glutMainLoop()
main()

