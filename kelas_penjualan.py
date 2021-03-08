import listvar as lv #import file list
from tabulate import tabulate #import tabulate
from datetime import datetime #import datetime

class Penjualan:
	def __init__ (self,nama,harga=0,total_semua=0):
		self.nama = nama
		self.harga = harga
		self.total_semua = total_semua

	def info(self): #menampilkan info barang
		return self.nama+': Rp.{:,.2f}'.format(self.harga)

	def total(self,jumlah): #method total barang
		bayar = jumlah * self.harga

		return round(bayar)

	def pembayaran(self,duit,kembalian=0): #method pembayaran
		self.duit = duit
		self.kembalian = duit - self.total_semua

		return 'Kembalian Pelanggan: Rp.{:,.2f}'.format(self.kembalian)

	def total_belanja(self): #method total belanja
		for daftar in range(len(lv.list_belanja)):
			self.total_semua += lv.list_belanja[daftar][2]
		return self.total_semua

	def struk(self): #method struk
		struk_total = [['Total Semua Belanja: Rp.{:,.2f}'.format(self.total_semua)]]
		print('-------- STRUK BELANJA --------')
		print(tabulate(lv.list_belanja,tablefmt='pretty',headers=['Nama Barang','Qty','Total'],showindex='Always'))
		

		return tabulate(struk_total)

	def cetak_struk(self): #simpan struk
		waktu = 'Tanggal dan Jam: '+str(datetime.now())
		judul = '-------- STRUK BELANJA --------'
		pembatas = '--------------------------------'
		struk = tabulate(lv.list_belanja,tablefmt='pretty',headers=['Nama Barang','Qty','Total'],showindex='Always')
		total = 'Total belanja: Rp.{:,.2f}'.format(self.total_semua)
		uang = 'Uang Pelanggan: Rp.{:,.2f}'.format(self.duit)
		kembali = 'Kembalian Pelanggan: Rp.{:,.2f}'.format(self.kembalian)
		n = '\n'
		buka_file = open('log_penjualan','r+')
		isi = n+judul+n+waktu+n+pembatas+n+struk+n+total+n+pembatas+n+uang+n+kembali+n+pembatas+n
		if buka_file.write(isi):
			hasil = True
		else:
			hasil = False

		return hasil

		
