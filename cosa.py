#problema 2 : Cake-Candles
import sys

def birthdayCakeCandles(n, ar):
    #la lista es acomodada de forma decendente
    ar.sort(reverse=True)

    max = ar[0]
    #se inicializa un contador de las velas que tengan el mismo tamaño
    c = 0
    for objeto in ar:
        #por cada núm de la lista:
        #si el tamaño maximo es igual con el actual, lo cuenta
        if max == objeto:
            c = c + 1
        #si ya no coinciden, se termina el ciclo
        else:
            break
    #regresa la cuenta
    return c

if __name__ == '__main__':

    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))

    result = birthdayCakeCandles(n, ar)
    print(result)
