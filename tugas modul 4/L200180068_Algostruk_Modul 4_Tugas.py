class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

##1. Fungsi pencarian yang mengembalikan semua index lokasi elemen yang dicari dan
##    mengembalikan list kosong bila tidak ditemukan

def cariKotaTinggal(list, target):
    a = []
    for i in list :
        if i.kotaTinggal == target:
            a.append(list.index(i))
    return a

a = cariKotaTinggal(Daftar, "Klaten")
print(a)

#### 2. Fungsi untuk menemukan uang saku yang terkecil
##
##def cariUangSakuTerkecil(list):
##    temp = list[0].uangSaku
##    for i in list[1:]:
##        if i.uangSaku < temp:
##            temp = i.uangSaku
##    return temp
##
##a = cariUangSakuTerkecil(Daftar)
##print(a)

#### 3. Program mengembalikan objek mahasiswa yang mempunyai uang saku
####    terkecil
##
##def cariUangSakuTerkecilObject(list):
##    temp = list[0].uangSaku
##    obj = list[0].nama
##    for i in list[1:]:
##        if i.uangSaku < temp:
##            temp = i.uangSaku
##            obj = i.nama
##        elif i.uangSaku == temp:
##            temp.append(i)
##            obj.append(i)
##    return obj
##
##a = cariUangSakuTerkecilObject(Daftar)
##print(a)

#### 4. Fungsi untuk mengembalikan semua objek mahasiswa yang uang sakunya
####    kurang dari 250000
##
##def cariUangSakuKurang250k(list):
##    temp = []
##    for i in list:
##        if i.uangSaku < 250000:
##            temp.append(i)
##    return temp
##
##a = cariUangSakuKurang250k(Daftar)
##for i in a:
##    print(i.nama)

## 5. Program untuk mencari suatu item di sebuah linked list
##class node(object):
##    def __init__(self, data, next = None):
##        self.data = data
##        self.next = next
##
##    def cariLinkedList(self, dicari):
##        curNode = self
##        while curNode is not None:
##            if curNode.next != None:
##                if curNode.data != dicari:
##                    curNode = curNode.next
##                else:
##                    print("Data", dicari, "ada dalam linked list")
##                    break
##            elif curNode.next == None:
##                print ("Data", dicari, "tidak ada dalam linked list")
##                break
##a = node(12)
##menu = a
##a.next = node(34)
##a = a.next
##a.next = node(10)
##a = a.next
##a.next = node(45)
##
##menu.cariLinkedList(10)
##menu.cariLinkedList(110)

## 6. Fungsi binSe mengembalikan index lokasi elemen yang ditentukan,
##    kalau tidak ketemu mengembalikan False 
##
##def binSe(kumpulan, target):
##    low = 0
##    high = len(kumpulan)-1
##    while low <= high:
##        mid = (high+low)//2
##        if kumpulan[mid] == target:
##            return mid
##        elif target < kumpulan[mid]:
##            high = mid-1
##        else:
##            low = mid+1
##    return False
##
##kumpulan = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
##print(binSe(kumpulan, 5))

## 7. Fungsi binSe mengembalikan semua index lokasi elemen yg ditemukan
##
##def binSeAll(kumpulan, target):
##    temp = []
##    low = 0
##    high = len(kumpulan)-1
##    while low <= high :
##        mid = (high+low)//2
##        if kumpulan[mid] == target:
##            midKiri = mid-1
##            while kumpulan[midKiri] == target:
##                temp.append(midKiri)
##                midKiri = midKiri-1
##            temp.append(mid)
##            midKanan = mid+1
##            while kumpulan[midKanan] == target:
##                temp.append(midKanan)
##                midKanan = midKanan+1
##            return temp
##        elif target < kumpulan[mid]:
##            high = mid-1
##        else:
##            low = mid+1
##    return False
##
##kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
##print(binSeAll(kumpulan, 6))

#### No. 8
##Tidak membuat program, hanya menjelaskan tentang pola dari suatu program, penjelasannya terdapat pada file .pdf
