class MhsTIF(object):
    def __init__(self,nama,nim,tinggal,us):
        self.nama = nama
        self.nim = nim
        self.tinggal = tinggal
        self.us = us


c0 = MhsTIF('Dillah', "L200180074", 'Klaten', 300000)
c1 = MhsTIF('berlian', "L200180107", 'Sragen', 125000)
c2 = MhsTIF('ayudhia', "L200180096", 'Palembang', 20500)
c3 = MhsTIF('dika', "L200180097", 'Bekasi', 350000)
c4 = MhsTIF('annisa', "L200180066", 'Sragen', 500000)
c5 = MhsTIF('Tomi', "L200180056", 'Lampung', 430000)
c6 = MhsTIF('taufik', "L200180069", 'Surakarta', 450000)
c7 = MhsTIF('rohmad', "L200180101", 'Riau', 430000)
c8 = MhsTIF('Defa', "L200180068", 'Sragen', 235000)
c9 = MhsTIF('dhim', "L200180148", 'Sragen', 350000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9]

def mergeSort2(A, awal, akhir):
    mid = (awal+akhir)//2
    if awal < akhir:
        mergeSort2(A, awal, mid)
        mergeSort2(A, mid+1, akhir)

    a, f, l = 0, awal, mid+1
    tmp = [None] * (akhir - awal + 1)
    while f <= mid and l <= akhir:
        if A[f] < A[l]:
            tmp[a] = A[f]
            f += 1
        else:
            tmp[a] = A[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = A[f:mid+1]

    if l <= akhir:
        tmp[a:] = A[l:akhir+1]

    a = 0
    while awal <= akhir:
        A[awal] = tmp[a]
        awal += 1
        a += 1
        
def mergeSort(A):
    mergeSort2(A, 0, len(A)-1)

def convert(arr, obj):
    hasil=[]
    for x in range (len(arr)):
        for i in range (len(arr)):
            if arr[x] == obj[i].nim:
                hasil.append(obj[i])
    return hasil

A = []
for x in Daftar:
    A.append(x.nim)

print("MERGE SORT v2 BY NIM")
mergeSort(A)
for i in convert(A, Daftar):
    print ("[", i.nama,i.nim,i.tinggal,i.us, "]")
