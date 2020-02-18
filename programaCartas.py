from funPuntajeCarta import *
from funMayor import*

deno=[2,3,4,5,6,7,8,9,10,'j','q','k','a']
valorDeno=[2,3,4,5,6,7,8,9,10,11,12,13,14]
palo=['d','p','c','t']
valorPalo=[80,70,60,50]
j1Deno=[2,10,'a','q']
j1Palo=['t','c','d','d']
j2Deno=['a',8,2,'a']
j2Palo=['t','c','d','c']
j3Deno=[7,'a','k',10]
j3Palo=['t','p','d','d']

for i in range (len(j1Deno)):
    puntajeJ1=puntaje(j1Deno[i],j1Palo[i],deno,valorDeno,palo,valorPalo)
    print("jugador 1 tuvo: ",puntajeJ1,"puntos")
    puntajeJ2=puntaje(j2Deno[i],j2Palo[i],deno,valorDeno,palo,valorPalo)
    print("jugador 2 tuvo: ",puntajeJ2,"puntos")
    puntajeJ3=puntaje(j3Deno[i],j3Palo[i],deno,valorDeno,palo,valorPalo)
    print("jugador 3 tuvo: ",puntajeJ3,"puntos")
    gano=mayor(puntajeJ1,puntajeJ2,puntajeJ3)
    print("levanta el que obtuvo:",gano,"puntos")
