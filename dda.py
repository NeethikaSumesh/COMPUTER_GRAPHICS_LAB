from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(5.0)
    gluOrtho2D(-100,100,-100,100)

def plot_line():
    global x1,y1,x2,y2
    x=x1 
    y=y1 
    dx=x2-x1 
    dy=y2-y1 
    m=dy/dx

    glBegin(GL_POINTS)
    while y!=y2 and x!=x2:
        if m>1:
            x+=(1/m)
            y+=1
            glVertex2f(round(x),y)
        elif m<1:
            x+=1
            y+=m
            glVertex2f(x,round(y))
        elif m==1:
            x+=1
            y+=1
            glVertex2f(x,y)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow("DDA line")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)

    global x1,y1,x2,y2
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    glutDisplayFunc(plot_line)
    init_display()
    glutMainLoop()
main()
