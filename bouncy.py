#!/usr/bin/env python
##Autor: Manuel Machacon Cantillo
## Ejecutar con Python 3

def is_bouncy(number):
    number_sorted = sorted(str(number))
    number_sorted_reversed = sorted(str(number), reverse=True)
    
    return str(number) not in (''.join(number_sorted), ''.join(number_sorted_reversed))



def calc_bouncy():
    n = 0
    total_bouncy = 0
    percent = 0

    while(percent < 0.99):
        if is_bouncy(n):
            total_bouncy += 1
            percent = total_bouncy / n

        print("Número: {}, Porcentaje: {}".format(n, percent))
        n += 1

    print("\n\n99% de números bouncy alcanzados en "+str(n-1))



if __name__ == '__main__':
    calc_bouncy()
    input("Presione cualquier tecla para terminar")


    
    
    
