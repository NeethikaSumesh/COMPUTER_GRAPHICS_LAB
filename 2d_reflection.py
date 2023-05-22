from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def ClearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-100,100,-100,100)

def call_function(x1,y1,x2,y2,x3,y3):
    plot_triangle(x1,y1,x2,y2,x3,y3)
    reflection(x1,y1,x2,y2,x3,y3)

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

def reflection(x1,y1,x2,y2,x3,y3):
    c = int(input("Enter 1.Reflection abt x axis\nEnter 2.Reflection abt y axis\n3.Enter 2.Reflection abt origin\n4.Enter 2.Reflection abt x=y: "))
    if c==1:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,-y1)
        glVertex2f(x2,-y2)
        glVertex2f(x3,-y3)
        glEnd()
        glFlush()
    elif c==2:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,y1)
        glVertex2f(-x2,y2)
        glVertex2f(-x3,y3)
        glEnd()
        glFlush()
    elif c==3:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(-x1,-y1)
        glVertex2f(-x2,-y2)
        glVertex2f(-x3,-y3)
        glEnd()
        glFlush()
    elif c==4:
        glColor3f(0.0,1.0,0.0)
        glPointSize(10)
        glBegin(GL_TRIANGLES)
        glVertex2f(x1,y1)
        glVertex2f(x2,y2)
        glVertex2f(x3,y3)
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

    glutCreateWindow("Reflection")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutDisplayFunc(lambda: call_function(x1,y1,x2,y2,x3,y3))
    ClearScreen()
    glutMainLoop()

main()




