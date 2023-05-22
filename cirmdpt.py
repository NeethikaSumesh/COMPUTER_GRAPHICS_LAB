from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

xc=0
yc=0
r=1

WINDOW_SIZE=500

def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPointSize(3.0)
    gluOrtho2D(-100,100,-100,100)

def mdpt_circle():
    global xc,yc,r
    x=0
    y=r
    p=1-r
    glBegin(GL_POINTS)
    plot_symmetric(x,y)

    while x<y:
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*x+1-2*y
        plot_symmetric(x,y)
    glEnd()
    glFlush()

def plot_symmetric(x,y):
    global xc,yc
    glVertex2f(xc+x, yc+y)
    glVertex2f(xc+x, yc-y)
    glVertex2f(xc-x, yc+y)
    glVertex2f(xc-x, yc-y)
    glVertex2f(xc+y, yc+x)
    glVertex2f(xc+y, yc-x)
    glVertex2f(xc-y, yc+x)
    glVertex2f(xc-y, yc-x)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutCreateWindow("MDPT_CIRCLE")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)

    global xc,yc,r
    xc = int(input("Enter x coordinate of center: "))
    yc = int(input("Enter y coordinate of center: "))
    r = int(input("Enter the radius: "))

    glutDisplayFunc(mdpt_circle)
    init_display()
    glutMainLoop()
main()







