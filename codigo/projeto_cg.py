#-*- coding: utf-8 -*-
# Aula sobre composição de objetos e uso do teclado.


from math import cos
from math import pi
from math import sin
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLE import *   


global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global distanciamax
global estadoluz0
global estadoluz1
global estadoluz2

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45
distanciamax = 500    #distancia max para renderizar objs na proj. testar com 10.
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0
lastx=0
lasty=0


def piso():
    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -2.0, 0.0)  #Transtaçao do objeto
    #glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(3.0, -0.0, -3.0)       # P1
    glVertex3f(3.0, -0.0, 3.0)       # P2
    glVertex3f(-3.0, -0.0, 3.0)       # P3
    glVertex3f(-3.0, -0.0, -3.0)       # P4
    glEnd()
    glPopMatrix()



def fogao_bocas():
    #boca de fogões
    glPushMatrix()
    
    glTranslatef(0, 0, -0.4)
    
    #boca do fogao 1
    glPushMatrix()
    glTranslatef(0.32, 0.8, 0.2)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()

    #boca do fogao 2
    glPushMatrix()
    glTranslatef(0, 0.8, 0.2)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()

    #boca do fogao 3
    glPushMatrix()
    glTranslatef(-0.32, 0.8, 0.2)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()

    #boca do fogao 4
    glPushMatrix()
    glTranslatef(0.32, 0.8, 0.6)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()

    #boca do fogao 5
    glPushMatrix()
    glTranslatef(0, 0.8, 0.6)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()

    #boca do fogao 6
    glPushMatrix()
    glTranslatef(-0.32, 0.8, 0.6)
    glRotatef(90, 1, 0, 0)
    glutSolidCylinder(0.08, 0.04, 20, 10)
    glPopMatrix()
    glPopMatrix()

def fogao_painel():
    glPushMatrix()
    glTranslatef(0, 0.5, 0.54)
    glScalef(1, 0.2, 0.10)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.4, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.3, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.2, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.1, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.0, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.1, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.2, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.04, 0.04, 20, 10)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.35, 0.5, 0.58)
    glRotatef(90, 0, 0, 1)
    glutSolidCylinder(0.06, 0.04, 20, 10)
    glPopMatrix()

def fogao_forno():
    glPushMatrix()
    glTranslatef(0, -0.1, .5)
    glScalef(1, 1, 0.2)
    glutSolidCube(0.8)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.22, .6)
    glScalef(1, 0.2, 0.2)
    glutSolidCube(0.8)
    glPopMatrix()

def fogao_tampa():
    glPushMatrix()
    glTranslatef(0, 1.25, -0.5)
    glScalef(1, 1, 0.05)
    glutSolidCube(1)
    glPopMatrix()

def fogao(): 
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(0, -1.25, -2.4)
    fogao_tampa()
    fogao_painel()
    fogao_bocas()
    fogao_forno()
    glScalef(1, 1.5, 1)
    glutSolidCube(1)

    glPopMatrix()


def paredes():

    #PAREDE 1
    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, 1.0, 3.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(3.0, -0.0, -3.0)       # P1
    glVertex3f(3.0, -0.0, 3.0)       # P2
    glVertex3f(-3.0, -0.0, 3.0)       # P3
    glVertex3f(-3.0, -0.0, -3.0)       # P4
    glEnd()
    glPopMatrix()

    #PAREDE 2
    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, 1.0, -3.0)  #Transtaçao do objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(3.0, -0.0, -3.0)       # P1
    glVertex3f(3.0, -0.0, 3.0)       # P2
    glVertex3f(-3.0, -0.0, 3.0)       # P3
    glVertex3f(-3.0, -0.0, -3.0)       # P4
    glEnd()
    glPopMatrix()

    #PAREDE 3
    glColor3f(1, 1, 1) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(3.0, 1.0, 0.0)  #Transtaçao do objeto
    glRotatef(90, 0.0, 0.0, 1.0)     #Rotaçao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(3.0, -0.0, -3.0)       # P1
    glVertex3f(3.0, -0.0, 3.0)       # P2
    glVertex3f(-3.0, -0.0, 3.0)       # P3
    glVertex3f(-3.0, -0.0, -3.0)       # P4
    glEnd()
    glPopMatrix()


def bancada():

    #tabua
    glColor3f(0.0, 0.6, 0.5) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -0.7, 0.0)  #Transtaçao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.5, 1.5, 0.09)
    glutSolidCube(1.2)
    glPopMatrix()
    
    #base
    glColor3f(0.9, 0.6, 0.5) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -1.35, 0.0)  #Transtaçao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1, 1, 1)
    glutSolidCube(1.2)
    glPopMatrix()


def bule():
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(-0.32, -0.37, -2.2)  #Transçao do objeto
    glutSolidTeapot(0.1)
    glPopMatrix()




def desenho():
    global aux1
    global aux2
   
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)


    piso()
    paredes()
    bancada()
    bule()
    fogao()

    

    #OBJETO 7 - PRATO

    glColor3f(0, 0, 0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -0.35, 0.0)  #Transtaçao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.3, 0.3, 0.1)
    glutSolidTorus(0.8, 0.5 ,100, 100)
    glPopMatrix()
    
    
    glPopMatrix()





# ILUMINAÇÃO E APARÊNCIA DOS OBJETOS

def iluminacao_da_cena():
    
    luzAmbiente0=[0.2,0.2,0.2,1.0]
    luzDifusa0=[1,1,0,1.0]  # ; // "cor"
    luzEspecular0 = [0.3, 0.3, 0.3, 0.3]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 50.0, 1.0]

    luzAmbiente1=[1.0,0.0,0.0,1.0]
    luzDifusa1=[0.0,1.0,0.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz1=[0.0, 50.0, -50.0, 1.0]

    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0,0.0,0.0,1.0]  # ; // "cor"
    luzEspecular2 = [1.0, 0.0, 0.0, 1.0]  #;// "brilho"
    posicaoLuz2=[0.0, 5.0, 0.0, 0.0]  # última coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -1,0, 0,0]  # direção do vetor do spot

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização
    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de número 1
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    
    # Define os parametros da luz de número 2
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 5); # angulo do cone, de 0 a 180. 
    

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    
    # Habilita a luz de número 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
        
    # Habilita a luz de número 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de número 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        print('Luz Spot ligada.')
    else:
        glDisable(GL_LIGHT2)
    
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2

# AJUSTE DE APARÊNCIA

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    #gluPerspective(angulo, aspecto , near (perto), far(longe) )
    #  angulo = angulo em graus na direçao y.
    #  aspecto = deformaçao da janela. normalmente e a razao entre a largura e altura
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado
    gluPerspective(angulo, 1, 0.1, distanciamax) # Especifica a projeção perspectiva

    #glOrtho(left,right,bottom, top, near, far)
    #  left,right,bottom, top = limites da projeçao
    #  near = a menor distancia desenhada
    #  far = a maior distancia para que o objeto seja desenhado 
    #glOrtho(-5,5,-5,5,0.1,500) # Especifica a projeção paralela ortogonal

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

#CÂMERA

    #Pense na câmera como um vetor que aponta para o alvo da cena. #
    #Cada ponto desse vetor é em 3D (x, y, z)
    # A última coordenada ajusta a posição da câmera (deitada, de pé, invertida etc)

    #gluLookAt(eyex, eyey, eyez, alvox, alvoy, alvoz, upx, upy, upz)
    #    eyex, eyey, eyez = posiçao da camera
    #    alvox, alvoy, alvoz = coordenada para onde a camera olha.
    #    upx, upy, upz = indica a posiçao vertical da camera.
    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    print('Camera: (' + str( sin(esqdir) * 10) + ',' + str(cimabaixo) + "," + str(cos(esqdir) * 10) + ')')
    print('Alvo: (' + str(aux1) +','+str(aux2)+',0)')

   
    
    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho


# FUNÇÕES DO TECLADO E MOUSE    

# Função callback chamada para gerenciar eventos de teclas normais
# Obs.: maiusculo e minúsculo faz diferença.
def Teclado (tecla, x, y):
    global aux1
    global aux2
    global estadoluz0
    global estadoluz1
    global estadoluz2
    print("*** Tratamento de teclas comuns")
    print(">>> Tecla: ",tecla)
    
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 0.1
        print ("aux1 = ", aux1 )
    
    if tecla == b's': # S
        aux1 = aux1 + 0.1
        print ("aux1 = ", aux1 )
        
    if tecla == b'w': # W
        aux2 = aux2 + 0.1
        print ("aux2 = ", aux2 )

    if tecla == b'z': # Z
        aux2 = aux2 - 0.1
        print ("aux2 = ", aux2 )
        
    if tecla == b'0': # 0
        if estadoluz0 == 0:
            estadoluz0 = 1
            glEnable(GL_LIGHT0)
        else:
            estadoluz0 = 0
            glDisable(GL_LIGHT0)
    if tecla == b'1': # 1
        if estadoluz1 == 0:
            estadoluz1 = 1
            glEnable(GL_LIGHT1)
        else:
            estadoluz1 = 0
            glDisable(GL_LIGHT1)
    if tecla == b'2': # 2
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT2)
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT2)
        
    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    print("*** Tratamento de teclas especiais")
    print ("tecla: ", tecla)
    if tecla == GLUT_KEY_F1:
        print(">>> Tecla F1 pressionada")
    elif tecla == GLUT_KEY_F2:
        print(">>> Tecla F2 pressionada")
    elif tecla == GLUT_KEY_F3:
        print(">>> Tecla F3 pressionada")
    elif tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    else:
        print ("Apertou... " , tecla)
    tela()
    glutPostRedisplay()  



# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
             if (angulo >= 10):
                angulo -= 2


def Limite(valor):
    if valor > 1:
        return 1
    elif valor < -1:
        return -1
    else:
        return valor
        
   
    tela()
    glutPostRedisplay()

def JoinStyle (msg):
    sys.exit(0)



# PROGRAMA PRINCIPAL

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(1280,720)
glutCreateWindow(b"Aula06")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)

# create popup menu */

#glutCreateMenu (JoinStyle)
#glutAddMenuEntry (b"Exit", 99)
#glutAttachMenu (GLUT_RIGHT_BUTTON)

glutMainLoop()  # Inicia o laço de eventos da GLUT




