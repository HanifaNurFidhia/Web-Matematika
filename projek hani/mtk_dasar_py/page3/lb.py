class Mtk :
    
    def hitung_kecepatan():
        print ('hitung kecepatan ready!')
        jarak = float(input ('masukan jarak: '))
        waktu = float(input ('masukan waktu: '))
        kecepatan = jarak * waktu 
        print ('kecapatan: ', kecepatan,'\n')
        

    def luas_segitiga():
        print ('hitung luas segitiga ready!')
        alas = float(input ('masukan alas: '))
        tinggi = float(input ('masukan tinggi: '))
        luas = 0.5 * (alas * tinggi) 
        print ('luas segitiga adalah: ', luas,'\n')
        
        
    def luas_balok():
        print ('hitung luas balok ready!')
        panjang = float(input ('masukan panjang: '))
        lebar = float(input ('masukan lebar: '))
        tinggi = float(input ('masukan tinggi: '))
        luas = (2*panjang*lebar) + (2*panjang*tinggi) + (2*lebar*tinggi)
        print ('luas balok adalah: ', luas,'\n')  
        
        
    def luas_kubus():
        print ('hitung luas kubus ready!')
        S = float(input ('masukan sisi: '))
        luas = 6 * S * S
        print ('luas kubus adalah: ', luas,'\n')  
        
        
    while True: 
        userInput = int(input("Ketik 1 untuk melanjutkan ")) 
        if(userInput == 1):
            luas_balok()
