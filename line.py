from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

def ClearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)

def plot_line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10)
    glBegin(GL_LINES)
    glVertex2f(0.0,0.0)
    glVertex2f(3.0,3.0)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("LINES")
    glutInitWindowSize(500,500)
    glutInitWindowPosition(400,400)
    glutDisplayFunc(plot_line)
    ClearScreen()
    glutMainLoop()
main()
