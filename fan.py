from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

import math

globalx=0.0
globaly=0.0

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-300,300,-300,300)
	
def draw(x,y):
	glColor3f(0.0,0.0,1.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(25*math.cos(math.pi*i/180.0)+x,25*math.sin(math.pi*i/180.0)+y)
	glEnd()
	
def Petal1(x,y):
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x-25,y)
	glVertex2f(x-25,y)
	glVertex2f(x-25,y+100)
	glVertex2f(x+25,y+100)
	glVertex2f(x+25,y+100)
	glVertex2f(x+25,y)
	glVertex2f(x+25,y)
	glVertex2f(x,y)
	glEnd()
	
def Petal2(x,y):
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x,y+25)
	glVertex2f(x,y+25)
	glVertex2f(x-100,y+25)
	glVertex2f(x-100,y+25)
	glVertex2f(x-100,y-25)
	glVertex2f(x-100,y-25)
	glVertex2f(x,y-25)
	glEnd()

def Petal3(x,y):
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x-25,y)
	glVertex2f(x-25,y)
	glVertex2f(x-25,y-100)
	glVertex2f(x+25,y-100)
	glVertex2f(x+25,y-100)
	glVertex2f(x+25,y)
	glVertex2f(x+25,y)
	glVertex2f(x,y)
	glEnd()

def Petal4(x,y):
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POLYGON)
	glVertex2f(x,y)
	glVertex2f(x,y+25)
	glVertex2f(x,y+25)
	glVertex2f(x+100,y+25)
	glVertex2f(x+100,y+25)
	glVertex2f(x+100,y-25)
	glVertex2f(x+100,y-25)
	glVertex2f(x,y-25)
	glEnd()
def display():
	global globalx,globaly
	glClear(GL_COLOR_BUFFER_BIT)
	draw(globalx,globaly)
	Petal1(globalx,globaly+25)
	Petal2(globalx-25,globaly)
	Petal3(globalx,globaly-25)
	Petal4(globalx+25,globaly)
	glutSwapBuffers()
def animate():
	global globalx,globaly
	glTranslatef(globalx,globaly,0)
	glRotatef(45,0,0,1)
	glTranslatef(-globalx,-globaly,0)
	glutPostRedisplay()
	glutTimerFunc(50,animate,0)
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	glutCreateWindow("fan")
	glutDisplayFunc(display)
	glutTimerFunc(50,animate,0)
	init()
	glutMainLoop()
main()
