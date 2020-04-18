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

Daftar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9]

def mergeSort(A):
    ##print("Membelah      ",A)
    if len(A) > 1:
        mid = len(A) // 2
        separuhkiri = A[:mid]
        separuhkanan = A[mid:]

        mergeSort(separuhkiri)
        mergeSort(separuhkanan)

        i = 0;j=0;k=0
        while i < len(separuhkiri) and j < len(separuhkanan):
            if separuhkiri[i] < separuhkanan[j]:
                A[k] = separuhkiri[i]
                i = i + 1
            else:
                A[k] = separuhkanan[j]
                j = j + 1
            k=k+1

        while i < len(separuhkiri):
            A[k] = separuhkiri[i]
            i = i + 1
            k=k+1

        while j < len(separuhkanan):
            A[k] = separuhkanan[j]
            j = j + 1
            k=k+1
    ##print("Menggabungkan",A)

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

print("MERGE SORT BY NIM")
mergeSort(A)
for i in convert(A, Daftar):
    print ("[", i.nama,i.nim,i.tinggal,i.us, "]")
