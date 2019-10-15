import math

class Whiteboard(object):
    def __init__( self, p, l):
        self.panjang = p
        self.lebar = l

    def LuasWhiteboard(self):
        return self.panjang * self.lebar

    def KelilingWhiteboard(self):
        return 2* (self.panjang + self.lebar)

class RuangKelas(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
    def LuasRuangKelas(self):
        return 2 * (self.panjang * self.lebar + self.panjang * self.tinggi + self.lebar * self.tinggi)

    def VolumeRuangKelas(self):
        return self.panjang * self.lebar * self.tinggi

class AlatBelajar(object):
    def __init__(self, jk, jm, k, m):
        self.jumlahkursi = jk
        self.jumlahmeja = jm
        self.kursi = k
        self.meja = m
    
    def TotalBarang(self):
        return self.jumlahkursi + self.jumlahmeja
        
    def JumlahHargaBarang (self):
        return (self.jumlahkursi * self.jumlahkursi) + (self.jumlahmeja * self.jumlahmeja)
        
