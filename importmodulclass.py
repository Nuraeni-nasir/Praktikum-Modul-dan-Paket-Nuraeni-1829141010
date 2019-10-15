import modulclass as C

def main():
#class Whiteboard
    p = float (input("Panjang \t: "))
    l = float (input("Lebar\t\t: "))

    obj = C.Whiteboard(p,l)
    luas = obj.LuasWhiteboard()
    kel = obj.KelilingWhiteboard()
    print("-------------------------------------")
    print("Panjang Whiteboard\t: ",p," m")
    print("Lebar Whiteboard\t: ",l," m")
    print("-------------------------------------")
    print("MENGHITUNG LUAS & KELILING  WHITEBOARD")
    print("-------------------------------------")
    print("Luas  WHITEBOARD\t\t: ",luas)
    print("Keliling  WHITEBOARD\t: ",kel)
    print("=====================================")

#class RuangKelas
    print("-------------------------------------")
    p = float (input("Panjang\t: "))
    l = float (input("Lebar\t: "))
    t = float (input("Tinggi\t\t: "))
    
    obj2 = C.RuangKelas(p,l,t)
    vol = obj2.VolumeRuangKelas()

    print("-------------------------------------")
    print("Pangjang\t: ", p)
    print("Lebar\t: ", l)
    print("Tinggi \t: ", t)
    print("-------------------------------------")
    print("MENGHITUNG VOLUME RUANGKELAS")
    print("-------------------------------------")
    print("Volume  RuangKelas\t: ",vol)
    print("=====================================")

#class AlatBelajar
    k = 300000
    m = 500000

    print("\n-------------------------------------")
    print("Daftar Harga Barang")
    print("-------------------------------------")
    print("Kursi\t: Rp.",k)
    print("Meja\t\t: Rp.",m)
    print("-------------------------------------")
    print("Barang Yang Di Beli")
    print("-------------------------------------")

    jk = float (input("Jumlah Kursi\t: "))
    jm = float (input("Jumlah Meja\t: "))
    at = C.AlatBelajar(jk, jm, k, m)
    TB = at.TotalBarang()
    JHB = at.JumlahHargaBarang()

    print("-------------------------------------")
    print("MENGHITUNG BELANJAAN ANDA")
    print("-------------------------------------")
    print("Total Barang\t: ",TB)
    print("Total Harga\t: Rp.",JHB)
    print("=====================================")

if __name__ == "__main__":
    main()
