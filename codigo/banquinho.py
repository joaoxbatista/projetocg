# coding=latin1

import random
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

global esqdir
global cimabaixo
global aux1
global aux2
global angulo
global distanciamax
global estadoluz0
global estadoluz2u
global r
global g
global b

esqdir = 0
cimabaixo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 45
distanciamax = 500    #distancia max para renderizar objs na proj. testar com 10.
estadoluz0 = 1
estadoluz2 = 0
estadoluz3 = 0
r = 0.0
g = 0.0
b = 0.0



def eixos():      #desenha os eixos x e y do plano cartesiano.
    glColor3f(.9, .1, .1) # cor RGB  eixo X
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 0.0, 1.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .1, .9) # cor RGB  eixo Y
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix()

    glColor3f(.1, .9, .1) # cor RGB  eixo z
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glTranslate( 0.0, 0.0, -2.0)  #Transtaçao do objeto
    glutSolidCylinder(0.01, 4.0, 4, 10)
    glPopMatrix() 
  
def banquinho():
    global preto

    glPushMatrix()
    #glTranslate(1.0, 0.0, 0.0)
    #glScalef(1.0, 2.0, 1.0)

    #assento
    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, -1.7)
    glutSolidCylinder(0.6, 0.05, 40, 3)
    glPopMatrix()

    #estofado
    glColor3f(0.0, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, -1.796)
    glutSolidCylinder(0.54, 0.05, 40, 3)
    glPopMatrix()

    glColor3f(0.0, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.0, -1.7)
    glutSolidTorus(0.1,0.5,100,100)
    glPopMatrix()

    #1a perna
    glPushMatrix()
    glRotate(10, 0.0, 0.0, 1.0)
    glTranslate(0.0, 1.6, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.7, 0.0, 0.0)
    glutSolidCylinder(0.04, 1.76, 40, 3)
    glPopMatrix()

    glPopMatrix()

    #2a perna
    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotate(10, 0.0, 0.0, 1.0)
    glTranslate(0.0, 1.6, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.7, 0.0, 0.0)
    glutSolidCylinder(0.04, 1.76, 40, 3)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #3a perna
    glPushMatrix()
    glRotate(180, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotate(10, 0.0, 0.0, 1.0)
    glTranslate(0.0, 1.6, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.7, 0.0, 0.0)
    glutSolidCylinder(0.04, 1.76, 40, 3)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #4a perna
    glPushMatrix()
    glRotate(-90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotate(10, 0.0, 0.0, 1.0)
    glTranslate(0.0, 1.6, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.7, 0.0, 0.0)
    glutSolidCylinder(0.04, 1.76, 40, 3)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #1o apoio
    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(-45, 0.0, 1.0, 0.0)
    glTranslate(0.417, 0.7, -0.4)
    glutSolidCylinder(0.04, 0.8, 40, 3)
    glPopMatrix()


    #2o apoio
    glPushMatrix()
    glRotate(90, 0.0, 1.0, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(-45, 0.0, 1.0, 0.0)
    glTranslate(0.417, 0.7, -0.4)
    glutSolidCylinder(0.04, 0.8, 40, 3)
    glPopMatrix()

    glPopMatrix()

    #3o apoio
    glPushMatrix()
    glRotate(180, 0.0, 1.0, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(-45, 0.0, 1.0, 0.0)
    glTranslate(0.417, 0.7, -0.4)
    glutSolidCylinder(0.04, 0.8, 40, 3)
    glPopMatrix()

    glPopMatrix()

    #4o apoio
    glPushMatrix()
    glRotate(-90, 0.0, 1.0, 0.0)

    glColor3f(0.9, 0.6, 0.5)
    glPushMatrix()
    glRotatef(-45, 0.0, 1.0, 0.0)
    glTranslate(0.417, 0.7, -0.4)
    glutSolidCylinder(0.04, 0.8, 40, 3)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()



def desenho():
    
    eixos()
    banquinho()

# ILUMINAÇÃO E APARÊNCIA DOS OBJETOS

def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]


    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    
    r1 = [random.random(), random.random(), random.random(), 0.1]
    r2 = [random.random(), random.random(), random.random(), 0.1]
    r3 = [random.random(), random.random(), random.random(), 0.1]
    r4 = [random.random(), random.random(), random.random(), 0.1]
    r5 = [random.random(), random.random(), random.random(), 0.1]


    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[0.0,1.0,1.0,1.0]  # ; // "cor"
    luzEspecular2 = [0.2, 0.0, 0.0, 0.2]  #;// "brilho"
    posicaoLuz2=[0.0, 1.0, 0.0, 1.0]  # última coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -1.0, 0.0]  # direção do vetor do spot
    luzDifusa3 = (1.0, 1.0, 1.0, 1.0)

    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa3 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 50); # angulo do cone, de 0 a 180.


    pos = [20, 0, 20, 1]
    direction = [-1.0, 0.0, -1.0]
    spotAngle = 1.1
    glLightfv(GL_LIGHT3, GL_DIFFUSE, r2 )
    glLightfv(GL_LIGHT3, GL_SPECULAR, [1.0, 0.0, 0.0, 1.0] )
    glLightfv(GL_LIGHT3, GL_POSITION, pos)
    glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, spotAngle)
    glLightfv(GL_LIGHT3, GL_SPOT_DIRECTION, direction)
    glLightf(GL_LIGHT3, GL_SPOT_EXPONENT, 2)

    pos1 = [-20, 60, 20, 1]
    direction1 = [1.0, -3.0, -1.0]
    glLightfv(GL_LIGHT4, GL_DIFFUSE, r3 )
    glLightfv(GL_LIGHT4, GL_SPECULAR, [1.0, 0.0, 0.0, 1.0] )
    glLightfv(GL_LIGHT4, GL_POSITION, pos1)
    glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 1.1)
    glLightfv(GL_LIGHT4, GL_SPOT_DIRECTION, direction1)
    glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 2)

    pos2 = [-20, 40, -20, 1]
    direction2 = [1.0, -2.0, 1.0]
    glLightfv(GL_LIGHT5, GL_DIFFUSE, r4 )
    glLightfv(GL_LIGHT5, GL_SPECULAR, [1.0, 0.0, 0.0, 1.0] )
    glLightfv(GL_LIGHT5, GL_POSITION, pos2)
    glLightf(GL_LIGHT5, GL_SPOT_CUTOFF, 1.1)
    glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, direction2)
    glLightf(GL_LIGHT5, GL_SPOT_EXPONENT, 2)


    pos3 = [20, 60, -20, 1]
    direction3 = [-1.0, -3.0, 1.0]
    glLightfv(GL_LIGHT6, GL_DIFFUSE, r5 )
    glLightfv(GL_LIGHT6, GL_SPECULAR, [1.0, 0.0, 0.0, 1.0] )
    glLightfv(GL_LIGHT6, GL_POSITION, pos3)
    glLightf(GL_LIGHT6, GL_SPOT_CUTOFF, 1.1)
    glLightfv(GL_LIGHT6, GL_SPOT_DIRECTION, direction3)
    glLightf(GL_LIGHT6, GL_SPOT_EXPONENT, 2)

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)

    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
        print('Luz Spot ligada.')
        preto = 1.0
    else:
        glDisable(GL_LIGHT2)
    if estadoluz3 == 1:
        glEnable(GL_LIGHT3)
        glEnable(GL_LIGHT4)
        glEnable(GL_LIGHT5)
        glEnable(GL_LIGHT6)
    else:
        glDisable(GL_LIGHT3)
        glDisable(GL_LIGHT4)
        glDisable(GL_LIGHT5)
        glDisable(GL_LIGHT6)


    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2

# AJUSTE DE APARÊNCIA

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0,0,0,0)

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
    global esqdir
    global cimabaixo
    global estadoluz0
    global estadoluz2
    global estadoluz3
    global r
    global g
    global b
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

    if tecla == b'r':
        esqdir = 1.2
        cimabaixo = 3.0

    if tecla == b't':
        esqdir = -1.2
        cimabaixo = -2.75

    if tecla == b'y':
        esqdir = 0
        cimabaixo = 7.44
        aux1 = 0.7

    if tecla == b't':
        r3 = 3
    if tecla == b'0': # 0
        if estadoluz0 == 0:
            estadoluz0 = 1
            glEnable(GL_LIGHT0)
        else:
            estadoluz0 = 0
            glDisable(GL_LIGHT0)
    if tecla == b'2': # 2
        if estadoluz2 == 0:
            estadoluz2 = 1
            glEnable(GL_LIGHT2)
            r = 1.0
            g = 1.0
            b = 0.0
        else:
            estadoluz2 = 0
            glDisable(GL_LIGHT2)
            r = 0.0
            g = 0.0
            b = 0.0
    if tecla == b'3': # 2
        if estadoluz3 == 0:
            estadoluz3 = 1
            glEnable(GL_LIGHT3)
            glEnable(GL_LIGHT4)
            glEnable(GL_LIGHT5)
            glEnable(GL_LIGHT6)
        else:
            estadoluz3 = 0
            glDisable(GL_LIGHT3)
            glDisable(GL_LIGHT4)
            glDisable(GL_LIGHT5)
            glDisable(GL_LIGHT6)

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
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (angulo <= 130):
                angulo += 2
    tela()
    glutPostRedisplay()


# PROGRAMA PRINCIPAL

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(600,600)
glutCreateWindow(b"Exercicio CG - RLF")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT