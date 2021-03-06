file_barang = open('Data_barang.txt','r')
baca_file = file_barang.readlines()
import listvar as lv

import os
from kelas import Barang

tambah = 'Y'
while tambah == 'y' or tambah == 'Y':
	os.system('cls')
	if len(lv.list_belanja) == 0:
		print('Selamat Datang')
	else:
		print('Daftar Belanja: ')
		index = 0
		for daftar in lv.list_belanja:
			print(str(index)+'. '+lv.list_belanja[index][0]+' Qty: '+str(lv.list_belanja[index][1])+' Rp.'+str(lv.list_belanja[index][2])) 
			index +=1
			print('-------------------------------------')
	index = 0
	for data in baca_file:
		barang = data.split()
		data_barang = Barang(barang[2],int(barang[3]))
		lv.list_barang.append(data_barang)
		print(str(index) +'. '+ data_barang.info())
		index += 1

	pilihan = int(input('Pilih Menu yang diinput: '))
	barang_pilihan = lv.list_barang[pilihan]
	jumlah = int(input('Mau beli berapa %s: ' %(barang_pilihan.nama)))

	total_belanja = barang_pilihan.total(jumlah)

	print('Total belanja: Rp.{:,.2f}'.format(total_belanja))
	daftar_belanja = [barang_pilihan.nama,jumlah,total_belanja]
	lv.list_belanja.append(daftar_belanja)
	tambah = input('Tambah Belanjaan(Y/N)? ')

data_barang.total_belanja()
print(data_barang.struk())

duit = int(input('Masukkan Uang Pelanggan: Rp.'))
print(data_barang.pembayaran(duit))

menu = input('Keluar toko? ')
if menu == 'y':
	exit()

if __name__ == '__main__':
	main()

file_barang.close()