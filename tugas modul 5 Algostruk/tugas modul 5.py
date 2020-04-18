class MhsTIF(object):
    def __init__ (self ,nama,nim,alamat,us):
        self.nama = nama
        self.nim = nim
        self.alamat = alamat
        self.us = us


c0 = MhsTIF('Defa',"L312314",'Klaten',30000)
c1 = MhsTIF('raffy',"N332425",'Jogonalan',40000)
c2 = MhsTIF('Zanuar',"M464545",'KebonArum',50000)
c3 = MhsTIF('Reonaldy',"H346742","Prambanan",60000)
c4 = MhsTIF('Tomy',"G464345",'Salatiga',10000)
c5 = MhsTIF('Satmoko',"K56435",'Ampel',70000)
c5 = MhsTIF('Aji',"B464653",'Boyolali',80000)
c6 = MhsTIF('Abdilah',"E346332",'Ceper',90000)
c7 = MhsTIF('Ahmad',"F547748",'Pedan',20000)
c8 = MhsTIF('Nur',"C534646",'Pacitan',100000)
c9 = MhsTIF('Hidayat',"A674744",'Nganjuk',200000)


Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

#nomer 1
def swap(a,b,c):
    tmp=a[b]
    a[b]=a[c]
    a[c]=tmp


def ceknim(b):
    for i in b:
        print(i.nama,i.nim,i.alamat)


def urutnim(a):
    n = len(a)
    for x in range(n-1):
        for y in range(n-x-1):
            if a[y].nim > a[y+1].nim:
                swap(a,y,y+1)
                
#nomer 2
a = [13, 18, 25, 44, 66, 78, 89, 107]
b = [2, 4, 5, 10, 13, 18, 23, 29]

def urutC(a, b):
    c = a +b
    for i in range(1,len(c)):
        nilai = c[i]
        pos = i
        while pos > 0 and nilai<c[pos - 1]:
            c[pos]=c[pos-1]
            pos -= 1
        c[pos]=nilai
    print(c)


#nomer 3
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[1] < A[posisiTerkecil]:
            posisiTerkecil = 1
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)

def selectionSort(A):
    n = len(A)
    for i in range (n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai

from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubbleSort(u_bub);ak=detak();print("Bubble :%g detik"%(ak-aw));
aw = detak();selectionSort(u_sel);ak=detak();print("Selection :%g detik"%(ak-aw));
aw = detak();insertionSort(u_ins);ak=detak();print("Insertion :%g detik"%(ak-aw));

       
