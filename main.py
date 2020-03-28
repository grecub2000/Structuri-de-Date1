from copy import copy
from random import *
from math import log
from time import time


# bubble sort

def bubble_sort(vector):
    if len(vector) == 0:
        return vector
    if len(vector) >= 10000:
        return "Sortare inoptima"
    aux = copy(vector)
    for i in range(len(aux)):
        for j in range(0, len(aux) - i - 1):
            if aux[j] > aux[j + 1]:
                aux[j], aux[j + 1] = aux[j + 1], aux[j]

    return aux


# count sort

def cmmdc(vector):
    if len(vector)==0:
        return 0
    
    i=0
    while len(vector)>i and vector[i] == 0:
        i+=1
    if i>=len(vector):
        return 1
        
    a = vector[i]
    
    for i in range(1,len(vector)):
        b = vector[i]
        if b == 0:
            break
        while b != 0:
            if b >= a:
                b = b - a
            else:
                a = a - b
    return a


def count_sort(vector):
    if len(vector) == 0:
        return vector
    mx = max(vector)
    mn = min(vector)
    d = cmmdc(vector)
    if mx==0:
        return vector
    if (mx - mn) // d >= 11000:
        return "Sortare inoptima"
    mn //= d
    aux = copy(vector)
    
    if mx // d - mn // d < 1000:
        for i in range(len(aux)):
            aux[i] = aux[i] // d - mn
        mx = mx - mn
    
    fr = [0] * (mx + 1)

    for i in aux:
        fr[i] +=1
    
    j = 0
    for i in range(mx + 1):
        while fr[i] > 0:
            aux[j] = i
            j += 1
            fr[i] -=1
    if d > 1:
        for i in range(len(aux)):
            aux[i] = (aux[i] + mn) * d
            
    return aux


# radix sort

def transf(dict):
    aux = []
    for l in dict.values():
        for j in l:
            aux.append(j)

    return aux


def radix_sort(vector):
    baza = 256
    if len(vector) == 0 or max(vector) == 0:
        return vector
    l = copy(vector)
    k = 1
    dict = {}
    if max(vector) == 0:
        return l
    n = (int(log(max(vector), baza)) + 1)
    for i in range(n):
        for j in range(baza):
            dict[j] = []
        for j in l:
            dict[(j // k) % baza].append(j)
        l = transf(dict)
        k = k * baza
    return l


# merge sort

def ms(vector):
    if len(vector) > 1:
        mijloc = len(vector) // 2
        L = vector[:mijloc]
        R = vector[mijloc:]

        ms(L)
        ms(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vector[k] = L[i]
                i += 1
            else:
                vector[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            vector[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            vector[k] = R[j]
            j += 1
            k += 1

    return vector


def merge_sort(vector):
    aux = copy(vector)
    return ms(aux)


# quick sort

def pivot(a, b, c):
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c
    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c


def partition(vector, st, dr):
    p = pivot(choice(vector[st:dr + 1]), choice(vector[st:dr + 1]), choice(vector[st:dr + 1]))
    i = st - 1
    j = dr + 1
    while 1:
        i += 1
        while vector[i] < p:
            i += 1
        j -= 1
        while vector[j] > p:
            j -= 1
        if i < j:
            vector[i], vector[j] = vector[j], vector[i]
        else:
            return j


def qs(vector, st, dr):
    if st < dr:
        p = partition(vector, st, dr)
        qs(vector, st, p)
        qs(vector, p + 1, dr)


def quick_sort(vector):
    l = copy(vector)
    qs(l, 0, int(len(l) - 1))
    return l


# testarea sortarii

def test_sort(vector_inital, vector_sortat):
    vector_inital.sort()
    for i in range(len(vector_inital)):
        if vector_inital[i] != vector_sortat[i]:
            return 'Sortare incorecta'

    return 'Sortare corecta'


# generator

def generator(n, max):
    vector = []
    for i in range(n):
        x = randrange(0, max + 1)
        vector.append(x)

    return vector

#testare optimalitate
def optim(sortare, vector):
    rez = sortare(vector)
    if rez == "Sortare inoptima":
        return -1


with open ("date.txt") as f:

    
    t=int(f.readline())
    for i in range(1,t+1):
        n,mx = f.readline().split()
        n,mx = int(n), int(mx)
        print("Testul numarul {} : {} numere, cu maximul {} \n".format(i,n,mx))
        
        vector = generator(n, mx)
        sortari = [bubble_sort, count_sort, radix_sort, merge_sort, quick_sort]
        
        for sort in sortari:
            if optim(sort, vector) == -1:
                print(sort.__name__ , ": Sortare inoptima")
            else:
                timp_start = time()
                sort(vector)
                timp_end = time()
                print(sort.__name__ , ': timp->', timp_end - timp_start, 'secunde, ', test_sort(vector, sort(vector)))
            
        print('\n')
   
