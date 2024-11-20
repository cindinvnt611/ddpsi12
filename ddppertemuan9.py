print('----mencari celcius ke fahrenheit----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))

print('----mencari bilangan genap----')
def is_genap(bilangan_genap):
    return bilangan_genap &2 == 0
#untuk memasukkan value 
print(is_genap(4))
print(is_genap(7))

print('----\n mencetak nilai kelulusan----')
#rata rataa\ nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80: 
        return 'Lulus'
    else :
        return 'Tidak Lulus'
    
#untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))    

print('----cetak bilangan ganjil----')
def bilangan_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
#untuk memasukan value
bilangan_ganjil(20) 