#problema 2 : Cake-Candles
import sys

def birthdayCakeCandles(n, ar):

    ar.sort(reverse=True)

    max = ar[0]
    c = 0
    for objeto in ar:

        if max == objeto:
            c = c + 1

        else:
            break

    return c

if __name__ == '__main__':

    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))

    result = birthdayCakeCandles(n, ar)
    print(result)
