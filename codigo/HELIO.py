from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global POSX
global POSY

POSY = 3
POSX = 3

def peao():
    glPushMatrix()               
    for i in range(50):
        color = 1-(i*2*.01)
        glColor3f(color, 0.0, color)
        glutSolidSphere(0.01, 20, 20)
        glTranslate(0.0, 0.0, 0.005)
        glScale(1.05, 1.05, 1.05)
    glPopMatrix()

def piso():
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f( 0.0, 0.0, 0.0)       
    glVertex3f( 0.0, 6.0, 0.0)       
    glVertex3f( 6.0, 6.0, 0.0)      
    glVertex3f( 6.0, 0.0, 0.0)     
    glEnd()
    glPopMatrix()

def desenho():
    global POSY
    global POSX
    
    piso()
    glPushMatrix()
    glTranslate(POSX, POSY, 0.0)
    peao()
    glPopMatrix()

def iluminacao():
    RGBA = [1.0, 1.0, 1.0, 1.0]
    luzA = [1.0, 1.0, 1.0, 1.0]
    luzD = RGBA
    luzE = RGBA
    posxyz = [0.0, 5.0, 0.0, 0.0]

    especularidade=[1.0, 1.0, 1.0, 1.0]
    especMaterial = 60;
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glShadeModel(GL_SMOOTH) 
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzA)

    glLightfv(GL_LIGHT0, GL_AMBIENT, luzA)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzD)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzE)
    glLightfv(GL_LIGHT0, GL_POSITION, posxyz)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    glEnable(GL_DEPTH_TEST)
        
def tela():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glShadeModel(GL_SMOOTH)

    gluPerspective(45, 1, 0.1, 200)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(3, 1, 9, 3, 3, 0, 0, 1, 0)
    iluminacao()
    glEnable(GL_DEPTH_TEST)

    desenho()                    
    glFlush()         

def ControleMouse(button, state, x, y):
    global POSY
    global POSX      
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):
            POSY = 3
            POSX = 3
    tela()
    glutPostRedisplay()

def Normal(valor):
    if valor > 6:
        return 6
    elif valor < 0:
        return 0
    else:
        return valor

def MousePressionado(x, y):
    global POSY
    global POSX

    POSX = Normal(x*.01)
    POSY = 6-Normal(y*.01)

    print "("+str(POSX)+", "+str(POSY)+", 0.0)"

    tela()
    glutPostRedisplay()


def main():
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutCreateWindow(b"TABULEIRO")
    glutDisplayFunc(tela)
    glutMouseFunc(ControleMouse)
    glutMotionFunc(MousePressionado)
    glutMainLoop()


main()
