file_barang = open('Data_barang.txt','r') #buka file Data_barang
baca_file = file_barang.readlines() #baca file
import listvar as lv

import os
from kelas_penjualan import Penjualan

buka = 'y' # selama toko buka
tambah = 'y' # selama ada penambahan barang
while (buka == 'y' or buka == 'Y'):
	while tambah == 'y' or tambah == 'Y':
		
		os.system('cls') #bersihkan layar
		if len(lv.list_belanja) == 0: #jika list belanja kosong
			print('Selamat Datang')

		else:	#jika tidak
			print('Daftar Belanja: ') #cetak list belanja
			index = 0
			for daftar in lv.list_belanja:
				print(str(index)+'. '+lv.list_belanja[index][0]+' Qty: '+str(lv.list_belanja[index][1])+' Rp.'+str(lv.list_belanja[index][2])) 
				index +=1
				print('-------------------------------------')
		index = 0

		print('---------------------')

		for data in baca_file: #menampilkan data barang yang ada di file Data_barang.txt
			barang = data.split()
			data_barang = Penjualan(barang[2],int(barang[3])) #memasukkan data barang pada kelas penjualan
			lv.list_barang.append(data_barang) #menambahkan data barang ke list barang
			print(str(index) +'. '+ data_barang.info())
			index += 1
		print('---------------------')

		pilihan = int(input('Pilih Menu yang diinput: ')) #ambil input user untuk barang
		barang_pilihan = lv.list_barang[pilihan]
		jumlah = int(input('Mau beli berapa %s: ' %(barang_pilihan.nama)))

		total_belanja = barang_pilihan.total(jumlah) #total belanja user (harga barang * total beli)
		print('Total belanja: Rp.{:,.2f}'.format(total_belanja))

		daftar_belanja = [barang_pilihan.nama,jumlah,total_belanja]
		lv.list_belanja.append(daftar_belanja) #menambah barang ke daftar belanja

		tambah = input('Tambah Belanjaan(Y/N)? ') #ambil input user untuk tambah daftar belanja
		if tambah == 'n' or tambah == 'N':
			break
		#akhir dari perulangan pembahan daftar belanja

	data_barang.total_belanja() 
	print(data_barang.struk()) #menampilkan struk belanja

	duit = int(input('Masukkan Uang Pelanggan: Rp.')) #ambil input user untuk uang user
	print(data_barang.pembayaran(duit))

	cetak_struk = input('Simpan Struk(Y/N)? ')
	if cetak_struk == 'y' or cetak_struk == 'Y':
		hasil = data_barang.cetak_struk()
		if hasil:
			print('Struk berhasil disimpan')
		else:
			print('Struk gagal disimpan')

	menu = input('Kembali ke penjualan? ') #ambil input user untuk kembali ke penjualan
	if menu == 'y' or menu == 'Y':
		buka = 'y'
		tambah = 'y'
		lv.list_belanja.clear()
	else:
		print('Keluar toko')
		exit()
	#akhir dari perulangan toko

file_barang.close() #tutup file
