##ModulePythonPertamaku
def ucapkanSalam():
    print ("Assalamu'alaikum!")

def kuadratkan(x):
    return x*x
buah = 'Mangga'
daftarBaju = ['batik', 'loreng', 'resmi berdasi']
jumlahBaju = len(daftarBaju)


##LatOOP2

class Pesan(object):
    """
        Sebuah class bernama Pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self) :
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai ', len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru


##LatOOP3

class Manusia(object):
    """ Class 'Manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ", self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self,k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

p1 = Manusia('Fatimah')
p1.ucapkanSalam()


##LatOOP4
class Mahasiswa(Manusia):
    """ Class Mahasiswa yang dibangun dari class Manusia"""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + ', Tinggal di ' + self.kotaTinggal \
            + ', Uang Saku Rp. ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self,s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'


##LatOOP5
class MhsTIF(Mahasiswa):
    """ Class MhsTIF yang dibangun dari class Mahasiswa"""
    def katakanPy(self):
        print('Python is cool...')

##LatOOP6
##melanjutkan latihan 2.4

        
##LatOOP7
class kelasKosongan(object):
    pass

    ##Sekarang kita coba
k = kelasKosongan()
k.x = 23
k.y = 47
print(k.x + k.y)
k.mystr = 'Indonesia'
print(k.mystr)
