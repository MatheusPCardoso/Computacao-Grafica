from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

def calcPiramide(r,l,a,pb,an):
    # BASE
    glBegin(GL_POLYGON)
    for i in range(0,l):
        x = r * math.cos(i*an)
        y = r * math.sin(i*an)
        pb += [ (x,y) ]
        glVertex3f(x,y,0.0)
    glEnd()

    # LATERAL
    glBegin(GL_TRIANGLES)
    for i in range(0,l):
        glColor3fv(((1,0,0), (0,0,0))[(i+1)%len(((1,0,0), (0,0,0)))])
        glVertex3f(0.0,0.0,a)
        glVertex3f(pb[i][0],pb[i][1],0.0)
        glVertex3f(pb[(i+1)%l][0],pb[(i+1)%l][1],0.0)
    glEnd()

def piramide():
    raio = 2
    lados = 6
    altura = 5
    base = []
    angulo = (2*math.pi)/lados

    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(((1,0,0), (0,0,0))[0])
    calcPiramide(raio,lados,altura,base,angulo)
    glPopMatrix()


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    piramide()
    a+=1
    glutSwapBuffers()
  
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(800,800)
    glutCreateWindow("piramide 3")
    glutDisplayFunc(desenha)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(1,1,1,1)
    gluPerspective(45,800/800,0.1,100.0)
    glTranslatef(0.0,0.0,-10)
    glutTimerFunc(10,timer,1)
    glutMainLoop()

main()