def urai(x):#fungsi urai
    a = [char for char in x]#memasukan huruf ke dalam list a
    b = [] #untuk menampung kata setelah di urai
    c = [] #untuk menggabungkan kata yang sudah diurai
    for i in range(len(x)):#function for i batasan nya sesuai dengan jumlah huruf, untuk menyimpan huruf yang sudah dipisah dan di tambahkan dengan kombinasi huruf berikutnya
        for j in range(i+1):#function for j batasann nya sesuai dengan index i supaya tidak looping ke semua huruf.
            b = a[j] #line ini berfungsi untuk menggabungkan huruf yang sudah dicacah dengan cacahan huruf berikutnya.
            c.append(b)
    return c #fungsi return berfungsi sebagai output ketika function urai dijalankan.
print('')
print(''.join(urai('Code'))) #menggunakan fungsi join untuk menyatukan huruf dalam list c
print(''.join(urai('Python'))) #menggunakan fungsi join untuk menyatukan huruf dalam list c
print(''.join(urai('Purwdhika'))) #menggunakan fungsi join untuk menyatukan huruf dalam list c
print('')
def rajut(x): #fungsi rajut
    a = [] #list untuk menampung nilai index yang akan digunakan untuk mencacah kata
    xList = [char for char in x] #list untuk menampung huruf-huruf dalam kata
    for i in range (len(x)): #for loops untuk mencari nilai index sampai kalau dijumlahkan = jumlah string kata
        a.append(i+1) #memasukan index ke dalam list a
        if sum(a) == len(x): #validasi jika jumlah list a sudah sama dengan jumlah string kata,
            break  #jika memenuhi validasi maka for loops akan stop
    return xList[-(a[-1]):] #output dari function rajut, a[-1] akan mengambil value terakhir dari list a.
print(''.join(rajut('CCoCodCode'))) #menggunakan fungsi join untuk menyatukan huruf saat di print
print(''.join(rajut('PPyPytPythPythoPython'))) #menggunakan fungsi join untuk menyatukan huruf saat di print
print(''.join(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))) #menggunakan fungsi join untuk menyatukan huruf saat di print