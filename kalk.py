def tambah(x, y):
   return x + y
def kurang(x, y):
   return x - y
def kali(x, y):
   return x * y
def bagi(x, y):
   return x / y
 
def hitung():
    print('\n\t=============================')
    print('\tProgram Kalkulator Sederhana')
    print('\t===============================')
    print('\t1. Penjumlahan')
    print('\t2. Pengurangan')
    print('\t3. Pembagian')
    print('\t4. Perkalian')
    print('\t===============================')
    print('\tSilahkan pilih 1-4')
    print('')
     
    pilih = input("Masukkan pilihan(1/2/3/4): ")
    # Meminta input dari user
    nilai1 = int(input("Masukkan bilangan pertama: "))
    nilai2 = int(input("Masukkan bilangan kedua: "))
    if pilih == '1':
       print(nilai1,"+",nilai2,"=", tambah(nilai1,nilai2))
       tanya()
    elif pilih == '2':
       print(nilai1,"-",nilai2,"=", kurang(nilai1,nilai2))
       tanya()
    elif pilih == '3':
       print(nilai1,"*",nilai2,"=", bagi(nilai1,nilai2))
       tanya()
    elif pilih == '4':
       print(nilai1,"/",nilai2,"=", kali(nilai1,nilai2))
       tanya()
    else:
       print("Input salah !!")
        
def tanya():
    tanya = input('\n\tKembali ke menu kalkulator (y/t)?')
    if tanya == 'y':
        hitung()
    elif tanya == 't':
        exit
    else:
        print('\n\tsalah input.........!!!')
 
hitung()
