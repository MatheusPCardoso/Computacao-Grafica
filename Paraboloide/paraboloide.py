from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from sys import argv
import math

#variaveis
window_name = "Paraboloid 4" # Nome da tela
n1 = 30
n2 = 30
r = 3
M, N = 150, 150
x0, y0 = -5, -5
x1, y1 = 5, 5
wx, wy = (x1 - x0)/M, (y1 - y0)/N
local_start = 0

# funcao responsavel pelo calculo do plot
def return_L(i,j):
    k = (math.pi*i/(n1-1))-(math.pi/2)
    p = 2*math.pi*j/(n2-1)
    x = r*math.cos(k)*math.cos(p)
    y = r*math.sin(k)
    z = r*math.cos(k)*math.sin(p)
    return x,y*y,z 

# funcao que gera a figura
def figure():
    glPushMatrix()
    glRotatef(local_start,1.0,0.0,0.0)
    glBegin(GL_QUAD_STRIP)
    for i in range(0,n1): 
        for j in range(0,n2): 
            x,y,z = return_L(i,j)
            glVertex3f(x,y,z)
            x,y,z = return_L(i+1,j)
            glVertex3f(x,y,z)
    glEnd()
    glPopMatrix()

# Starta o plot
def plot():
    global local_start
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    figure()
    local_start+=1
    glutSwapBuffers()
  
def count(i):
    glutPostRedisplay()
    glutTimerFunc(10,count,1)

#inicio - p
def glCreate():
    glutInit(argv)
    glutInitWindowSize(800, 800)
    glutCreateWindow(window_name)
    glutDisplayFunc(plot)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0,0,0,1)
    gluPerspective(-95, 800 / 800, 0.1, 100.0)
    glTranslatef(0,0,-10)
    glutTimerFunc(10,count,1)
    glutMainLoop()

def main():
    glCreate()

main()