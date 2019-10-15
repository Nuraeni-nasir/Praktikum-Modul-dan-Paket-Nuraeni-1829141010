from modulclass import Whiteboard as t

def main():
    p = float (input("Panjang \t: "))
    l = float (input("Lebar\t\t: "))
    obj = t (p,l)
    luas = obj.LuasWhiteboard()
    kel = obj.KelilingWhiteboard()
    print("-------------------------------------")
    print("Panjang \t: ",p," m")
    print("Lebar \t: ",l," m")
    print("-------------------------------------")
    print("MENGHITUNG LUAS & KELILING  Whiteboard")
    print("-------------------------------------")
    print("Luas Whiteboard\t\t: ",luas)
    print("Keliling  Whiteboard\t: ",kel)
    
if __name__ == "__main__":
    main()
