from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def ClearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plot_point():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,1.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(0.5,0.5)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("POINT")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(400,400)
    glutDisplayFunc(plot_point)
    ClearScreen()
    glutMainLoop()
main()




