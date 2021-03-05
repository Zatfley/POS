import os
class Barang:
	def __init__ (self,nama,harga=0):
		self.nama = nama
		self.harga = harga

	def info(self):
		return self.nama+': Rp.'+str(self.harga)

	def total(self,jumlah):
		bayar = jumlah * self.harga

		return round(bayar)
	def pembayaran(self,duit,kembalian=0):
		self.kembalian = duit - self.total_semua

		return 'Kembalian Pelanggan: '+str(self.kembalian)

	def total_belanja(self,total_semua=0):
		self.total_semua = 0
		for daftar in range(len(list_belanja)):
			self.total_semua += list_belanja[daftar][2]

		return 'Total Keseluruhan: %s'%(self.total_semua)

file_barang = open('Data_barang.txt','r')
baca_file = file_barang.readlines()
list_barang = []
list_belanja = []

tambah = 'Y'
while tambah == 'y' or tambah == 'Y':
	os.system('cls')
	if len(list_belanja) == 0:
		print('Selamat Datang')
	else:
		print('Daftar Belanja: ')
		index = 0
		for daftar in list_belanja:
			print(str(index)+'. '+list_belanja[index][0]+' Qty: '+str(list_belanja[index][1])+' Rp.'+str(list_belanja[index][2])) 
			index +=1
			print('-------------------------------------')
	index = 0
	for data in baca_file:
		barang = data.split()
		data_barang = Barang(barang[2],int(barang[3]))
		list_barang.append(data_barang)
		print(str(index) +'. '+ data_barang.info())
		index += 1

	pilihan = int(input('Pilih Menu yang diinput: '))
	barang_pilihan = list_barang[pilihan]
	jumlah = int(input('Mau beli berapa %s: ' %(barang_pilihan.nama)))

	total_belanja = barang_pilihan.total(jumlah)

	print('Total belanja: '+ str(total_belanja))
	struk_belanjaan = [barang_pilihan.nama,jumlah,total_belanja]
	list_belanja.append(struk_belanjaan)
	tambah = input('Tambah Belanjaan(Y/N)? ')


print(data_barang.total_belanja())

duit = int(input('Masukkan Uang Pelanggan: Rp.'))
print(data_barang.pembayaran(duit))

menu = input('Keluar toko? ')
if menu == 'y':
	exit()

if __name__ == '__main__':
	main()

file_barang.close()