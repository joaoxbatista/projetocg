#-*- coding: utf-8 -*-

from math import cos
from math import pi
from math import sin
import timeit
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
distanciamax = 500
estadoluz0 = 1
estadoluz1 = 0
estadoluz2 = 0
lastx=0
lasty=0



def piso():
    glColor3f(0.9, 0.9, 0.2) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -2.0, 0.0)  #Transtaçao do objeto
    #glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glBegin(GL_POLYGON)
    glVertex3f(3.0, -0.0, -3.0)       # P1
    glVertex3f(3.0, -0.0, 1.5)       # P2
    glVertex3f(-3.0, -0.0, 1.5)       # P3
    glVertex3f(-3.0, -0.0, -3.0)       # P4
    glEnd()
    glPopMatrix()

'''
Componente: Fogão
Aluno: João Batista Gome Silva
'''
def fogao_bocas():
    #boca de fogões
    glColor3f(0.0, 0.0, 0.0)
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

    glColor3f(0.0, 0.0, 0.0) #deixa os botoes pretos
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
    glColor3f(0.99, 0.99, 0.99)
    glPushMatrix()
    glTranslatef(0, -1.25, -2.4)
    fogao_tampa()

    fogao_forno()

    glPushMatrix()
    glScalef(1, 1.5, 1)
    glutSolidCube(1)
    glPopMatrix()

    fogao_painel()
    fogao_bocas()
    glPopMatrix()

'''
Componente: Luminária
Aluno: Monaly
'''
def luminaria():
    glPushMatrix()
    glTranslate(0.0, 1.0, 0.0)
    glColor3f(1.0, 0.4, 0.0) # cor RGB

    glPushMatrix()
    glRotatef(-90, 1.0, 0.0, 0.0)
    glTranslate( 0.0, 0.0, 0.3)
    glutSolidCylinder(0.04,1.0,40,8)
    glPopMatrix()

    glColor3f(1.0, 0.4, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    #glTranslate( -0.5, 0.0, 0.0)  #TranstaÃ§ao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto

    cont = 1
    while (cont <= 8): #quanto maior mais fino a ponta( a quant de voltas)
        cont += 0.3
        glutSolidTorus(0.06,0.5,20,20)
        glTranslate( 0.0, 0.0001, 0.035)
        glScale( 0.9 , 0.9, 0.9)
    glPopMatrix()

    glPopMatrix()

'''
Componente: Bancada
Aluno: Gabriel
'''
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
    glTranslate(0.0, -1.36, 0.0)  #Transtaçao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1, 1, 1.1)
    glutSolidCube(1.2)
    glPopMatrix()

'''
Componente: Bule
Aluno: Gabriel
'''
def bule():
    glColor3f(1.0, 0.1, 0.6) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(-0.32, -0.23, -2.2)
    glScale(1.5, 3.0, 1.5)  #Transçao do objeto
    glutSolidTeapot(0.1)
    glPopMatrix()


'''
Componente: Banquinho
Aluno: Raí
'''

def banquinho():
    glPushMatrix()

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

'''
Componente: Geladeira
Aluno: Mauricésar
'''

def porta1():

    glPushMatrix()
    glTranslate(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(-180, 1.0, 0.0, 0.0)
    glTranslate( 0.25, 0.75, 0.25)
    glutSolidCylinder(0.04,0.1,50,8)
    glPopMatrix()

    glColor3f(0.0, 1.0, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( -0.5, 0.0, 0.0)  #TranstaÃ§ao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    cont = 1
    glPopMatrix()
    glPopMatrix()


def porta2():

    glPushMatrix()
    glTranslate(0.0, 1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(-180, 1.0, 0.0, 0.0)
    glTranslate( 0.25, 0.19, 0.25)
    glutSolidCylinder(0.04,0.1,50,8)
    glPopMatrix()

    glColor3f(0.0, 1.0, 0.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaÃ§oes no objeto
    glTranslate( -0.5, 0.0, 1.0)  #TranstaÃ§ao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #RotaÃ§ao do objeto
    cont = 1
    glPopMatrix()
    glPopMatrix()

def geladeira():

    porta1()
    porta2()

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)

    #Gelão
    glColor3f(0.5, 0.5, 0.5) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -0.49, 0.0)  #Transtaçao do objeto
    glScale(0.6, 0.8, 0.8)
    glutSolidCube(1)
    glPopMatrix()


    #Gelão2
    glColor3f(0.5, 0.5, 0.5) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, 0.25, 0.0)  #Transtaçao do objeto
    glScale(0.6, 0.8, 0.8)
    glutSolidCube(1)
    glPopMatrix()

    #Gelão3
    glColor3f(0.5, 0.5, 0.5)# cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, 0.90, 0.0)  #Transtaçao do objeto
    glScale(0.6, 0.8, 0.8)
    #glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glutSolidCube(1)
    glPopMatrix()

     #Gelão4
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.2, -0.2, 0.0)  #Transtaçao do objeto
    glScale(0.25, 1.0, 0.7)
    glutSolidCube(1.1)
    glPopMatrix()


    #Gelão5
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.2, 0.85, 0.0)  #Transtaçao do objeto
    glScale(0.25, 0.7, 0.7)
    glutSolidCube(1)
    glPopMatrix()


    glPopMatrix()

'''
Componente: Luz
Aluno: Raí
'''
def luz():
    glColor3f(1.0, 1.0, 1.0)
    glPushMatrix()
    glScale(0.5, 1.7, 0.5)
    glutSolidSphere(0.1,40,40)
    glPopMatrix()


'''
Componente: armarios
Aluno: Raí
'''
def balcao():
	#base inferior
    glPushMatrix()
    glTranslate(0.0, -1.4, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(2.5, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado esquerdo
    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.21, 0.9, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado direito
    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 3.0, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.21, 0.9, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

	#fundo
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.38, 0.0)

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(2.5, 1.185, 0.04)
    glTranslate(0.6, 0.6, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()

    #porta 1
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.36)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.20, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    #porta 2
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.34)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 1.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.2, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #gaveta 1
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.32)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 2.0)

    glColor3f(1.0, 0.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.32, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #gaveta 2
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, -0.39, -0.32)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 2.0)

    glColor3f(1.0, 0.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.32, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #gaveta 3
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, -0.785, -0.32)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 2.0)

    glColor3f(1.0, 0.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.55, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #negocio de abrir. porta 1
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(0.85, -0.7, 1.3)
    glRotatef(90, 0.0, 1.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    #negocio de abrir. porta 2
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(1.13, -0.7, 1.3)
    glRotatef(90, 0.0, 1.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()


    #negocio de abrir. gaveta 1
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(2.5, -0.1, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    #negocio de abrir. gaveta 2
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(2.5, -0.5, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    #negocio de abrir. gaveta 3
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(2.5, -0.9, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    #pé 1
    glPushMatrix()
    glTranslate(0.1, -1.41, 1.38)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.07, 0.2, 40, 40)
    glPopMatrix()


    #pé 2
    glPushMatrix()
    glTranslate(0.1, -1.41, 0.45)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.07, 0.2, 40, 40)
    glPopMatrix()


    #pé 3
    glPushMatrix()
    glTranslate(2.9, -1.41, 1.38)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.07, 0.2, 40, 40)
    glPopMatrix()


    #pé 4
    glPushMatrix()
    glTranslate(2.9, -1.41, 0.45)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidCylinder(0.07, 0.2, 40, 40)
    glPopMatrix()

def pia():
    glPushMatrix()
    glTranslate(0.0, 0.36, 0.0)


    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.8, 0.18, 0.04)
    glTranslate(1.3, 2.6, 8.75)
    glutSolidCube(1.2)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.8, 0.18, 0.04)
    glTranslate(1.3, 7.4, 8.75)
    glutSolidCube(1.2)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.0, -0.35, 0.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.5, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()


    glPushMatrix()
    glTranslate(1.45, -0.35, 0.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(1.3, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado esquerdo pia
    glPushMatrix()
    glTranslate(0.5, -0.6, 0.3)
    glRotatef(90, 0.0, 0.0, 1.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.2, 0.6, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado direito pia
    glPushMatrix()
    glTranslate(1.5, -0.6, 0.3)
    glRotatef(90, 0.0, 0.0, 1.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.2, 0.6, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #frente pia
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-1.75, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.5, -0.6, 0.1)
    glRotatef(90, 0.0, 0.0, 1.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.2, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    #atras pia
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-1.05, 0.0, 0.0)

    glPushMatrix()
    glTranslate(0.5, -0.6, 0.1)
    glRotatef(90, 0.0, 0.0, 1.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.2, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    #fundo pia
    glPushMatrix()
    glTranslate(0.2, -0.6, 1.25)
    glRotatef(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.6, 0.8, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

def armario():
    glPushMatrix()
    #base superior
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(2.5, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    #base inferior
    glPushMatrix()
    glTranslate(0.0, -1.1, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(2.5, 0.9, 0.04)
    glTranslate(0.6, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado esquerdo
    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.94, 0.9, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    #lado direito
    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 3.0, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.94, 0.9, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

	#fundo
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glTranslate(0.0, 0.38, 0.0)

    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(2.5, 0.9, 0.04)
    glTranslate(0.6, 0.6, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()
    glPopMatrix()

    glPopMatrix()


    #porta 1
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.37)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 0.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.94, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()


    #porta 2
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.34)
    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 1.0)

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.94, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #porta 3
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glTranslate(-3.48, 0.0, -0.32)

    glPushMatrix()
    glRotatef(-90, 0.0, 0.0, 1.0)
    glTranslate(0.0, 2.0, 2.0)

    glColor3f(1.0, 0.0, 0.0) # cor RGB
    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.94, 0.84, 0.04)
    glTranslate(0.575, 1.0, 0.0)
    glutSolidCube(1.2)
    glPopMatrix()

    glPopMatrix()

    glPopMatrix()

    #negocio de abrir. porta 1
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(0.45, -1.0, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()


    #negocio de abrir. porta 2
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(1.5, -1.0, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    #negocio de abrir. porta 3
    glColor(0.692, 0.692, 0.692)
    glPushMatrix()
    glTranslate(2.5, -1.0, 1.3)
    glRotatef(90, 1.0, 0.0, 0.0)
    glutSolidTorus(0.04,0.3,40,100)
    glPopMatrix()

    glPopMatrix()

def desenho():
    global aux1
    global aux2

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)

    piso()


    glPushMatrix()
    glTranslate(1.5, 0.0, 0.0)
    fogao()
    bule()
    glPopMatrix()

    #luminarias
    glPushMatrix()
    glScale(1.3, 1.0, 0.5)
    bancada()
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)
    glPushMatrix()
    glScale(0.3, 1.5, 0.3)
    glTranslate(0.0, 0.0, -1.5)
    luminaria()
    glPopMatrix()

    glPushMatrix()
    glScale(0.3, 1.5, 0.3)
    glTranslate(0.0, 0.0, 1.5)
    luminaria()
    glPopMatrix()
    glPopMatrix()

    #luzes
    glPushMatrix()
    glTranslate(0.45, 1.6, 0.0)
    luz()
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.45, 1.6, 0.0)
    luz()
    glPopMatrix()


    #banquinhos
    glPushMatrix()
    glRotatef(90, 0.0, 1.0, 0.0)

    glPushMatrix()
    glScale(0.5, 1.3, 0.5)
    glTranslate(0.5, 0.38, 0.0)

    glPushMatrix()
    glTranslate(-1.7, -1.9, -1.1)
    glScale(0.5, 0.5, 0.5)
    banquinho()
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glScale(0.5, 1.3, 0.5)
    glTranslate(0.5, 0.38, 1.0)

    glPushMatrix()
    glTranslate(-1.7, -1.9, -0.95)
    glScale(0.5, 0.5, 0.5)
    banquinho()
    glPopMatrix()
    glPopMatrix()

    glPushMatrix()
    glScale(0.5, 1.3, 0.5)
    glTranslate(0.5, 0.38, 1.0)

    glPushMatrix()
    glTranslate(-1.7, -1.9, 0.1)
    glScale(0.5, 0.5, 0.5)
    banquinho()
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

    #geladeira
    glPushMatrix()
    glScale(0.9, 1.3, 1.0)
    glTranslate(-1.1, 0.45, 0.0)

    glPushMatrix()
    glRotatef(180, 0.0, 1.0, 0.0)
    glTranslate(-1.0, -1.1, 2.6)
    geladeira()
    glPopMatrix()
    glPopMatrix()

    #balcao
    glPushMatrix()
    glScalef(0.5, 1.0, 0.5)
    glTranslate(-5.0, -0.38, -6.2)
    glPushMatrix()
    glColor3f(0.3,0.3, 0.3)
    pia()
    glPopMatrix()
    balcao()
    glPopMatrix()


    glPushMatrix()
    glScalef(0.5, 1.0, 0.5)
    glTranslate(-5.0, 2.2, -6.2)
    armario()
    glPopMatrix()

    glPushMatrix()
    glScalef(0.5, 1.0, 0.5)
    glTranslate(-2, 2.2, -6.2)
    armario()
    glPopMatrix()





    #OBJETO 7 - PRATO

    glColor3f(1.0, 1.0, 1.0) # cor RGB
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    glTranslate(0.0, -0.6, 0.0)  #Transtaçao do objeto
    glRotatef(-90, 1.0, 0.0, 0.0)     #Rotaçao do objeto
    glScale(0.3, 0.3, 0.1)
    glutSolidTorus(0.8, 0.5 ,100, 100)
    glPopMatrix()


    glPopMatrix()


def iluminacao_da_cena():

    luzAmbiente0=[0.2,0.2,0.2,1.0]
    luzDifusa0=[0.3,0.3,0.3,1.0]  # ; // "cor"
    luzEspecular0 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz0=[0.0, 50.0, 50.0, 1.0]

    luzAmbiente1=[0.0,0.0,0.0,1.0]
    luzDifusa1=[1.0,1.0,1.0,1.0]  # ; // "cor"
    luzEspecular1 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz1=[0.0, 2.1, -0.45, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao1 = [0.0, -2.0, 0.0]


    luzAmbiente2=[0.0,0.0,0.0,1.0]
    luzDifusa2=[1.0, 1.0, 1.0, 1.0]  # ; // "cor"
    luzEspecular2 = [0.0, 0.0, 0.0, 0.0]  #;// "brilho"
    posicaoLuz2=[0.0, 2.1, 0.45, 1.0]  # Ãºltima coord como 0 pra funcionar como vetor da luz direcional
    direcao2 = [0.0, -2.0, 0.0]  # direÃ§Ã£o do vetor do spot

    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    glClearColor(1.0, 1.0, 1.0, 0.0)

    glShadeModel(GL_SMOOTH)   # GL_SMOOTH ou GL_FLAT

    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)

    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)


    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente0)

    # Define os parametros da luz ambiente
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa0 )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular0 )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz0 )

    # Define os parametros da luz de numero 1 / bancada
    glLightfv(GL_LIGHT1, GL_AMBIENT, luzAmbiente1)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, luzDifusa1 )
    glLightfv(GL_LIGHT1, GL_SPECULAR, luzEspecular1 )
    glLightfv(GL_LIGHT1, GL_POSITION, posicaoLuz1 )
    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, direcao1); #direcao da luz
    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 23); # angulo do cone, de 0 a 180.

    # Define os parametros da luz de numero 2 / bancada
    glLightfv(GL_LIGHT2, GL_AMBIENT, luzAmbiente2)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, luzDifusa2 )
    glLightfv(GL_LIGHT2, GL_SPECULAR, luzEspecular2 )
    glLightfv(GL_LIGHT2, GL_POSITION, posicaoLuz2 )
    glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, direcao2); #direcao da luz
    glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 23); # angulo do cone, de 0 a 180.


    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminaÃ§Ã£o
    glEnable(GL_LIGHTING)

    # Habilita a luz de nÃºmero 0
    if estadoluz0 == 1:
        glEnable(GL_LIGHT0)
    else:
        glDisable(GL_LIGHT0)

    # Habilita a luz de nÃºmero 1
    if estadoluz1 == 1:
        glEnable(GL_LIGHT1)
    else:
        glDisable(GL_LIGHT1)

    # Habilita a luz de nÃºmero 2
    if estadoluz2 == 1:
        glEnable(GL_LIGHT2)
    else:
        glDisable(GL_LIGHT2)

    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)

def tela():
    global angulo
    global distanciamax
    global aux1
    global aux2



    glClearColor(0.0, 0.0, 0.0, 1.0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo, 1, 0.1, distanciamax) # Especifica a projeção perspectiva

    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    print('Camera: (' + str( sin(esqdir) * 10) + ',' + str(cimabaixo) + "," + str(cos(esqdir) * 10) + ')')
    print('Alvo: (' + str(aux1) +','+str(aux2)+',0)')



    iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()
    glFlush()                    # Aplica o desenho


def Teclado (tecla, x, y):
    global aux1
    global aux2
    global estadoluz0
    global estadoluz1
    global estadoluz2
    global esqdir
    global cimabaixo
    global angulo
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

    if tecla == b'r':
        esqdir = 1.6
        cimabaixo = 1.2
        angulo = 10

    if tecla == b't':
        esqdir = -1.2
        cimabaixo = 2.75
        angulo = 33

    if tecla == b'y':
        esqdir = 0
        cimabaixo = 1.2
        angulo = 10

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
    print angulo
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN):
             if (angulo >= 10):
                angulo -= 2


#def Limite(valor):
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
glutCreateWindow(b"Cozinha")
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)


glutMainLoop()  # Inicia o laço de eventos da GLUT
