from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0
cores = ( (1,0,0), (0,0,0) ) # cores fla

def calcPrisma(r, l, a, pb, pt, an):
    glBegin(GL_POLYGON)
    #Retorna base do poligono
    for i in range(0,l):
        x1 = r * math.cos(i*an)
        y1 = r * math.sin(i*an)
        pb += [ (x1,y1) ]
        glVertex3f(x1,y1,0.0)
    glEnd()
    glBegin(GL_POLYGON)
    #Retorna topo do poligono
    for i in range(0,l):
        x2 = r * math.cos(i*an)
        y2 = r * math.sin(i*an)
        pt += [ (x2,y2) ]
        glVertex3f(x2,y2,a)
    glEnd()
    glBegin(GL_QUADS)
    #Retorna lateral do poligono
    for i in range(0,l):
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(pb[i][0],pb[i][1],a)
        glVertex3f(pb[i][0],pb[i][1],0.0)
        glVertex3f(pb[(i+1)%l][0],pb[(i+1)%l][1],0.0)
        glVertex3f(pb[(i+1)%l][0],pb[(i+1)%l][1],a)
    glEnd()

def prisma():
    raio = 3
    lados = 8 # Quantidade de lados
    altura = 3 # altura
    pontosBase = []
    pontosTopo = []
    angulo = (2*math.pi)/lados
    glPushMatrix()
    glTranslatef(0,-2,0)
    glRotatef(a,0.0,1.0,0.0)
    glRotatef(-110,1.0,0.0,0.0)
    glColor3fv(cores[0])
    calcPrisma(raio, lados, altura, pontosBase, pontosTopo, angulo)
    glPopMatrix()

def plot():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    prisma()
    a+=1
    glutSwapBuffers()
  
def count(i):
    glutPostRedisplay()
    glutTimerFunc(10,count,1)

def main():
    glutInit(sys.argv)
    glutInitWindowSize(1000,800)
    glutCreateWindow('pisma 3')
    glutDisplayFunc(plot)
    glEnable(GL_DEPTH_TEST)
    glClearColor(1,1,1,1)
    gluPerspective(45,1000/800,0.1,100.0)
    glTranslatef(0.0,0.0,-10)
    glutTimerFunc(10,count,1)
    glutMainLoop()

main()