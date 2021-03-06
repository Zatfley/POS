import listvar as lv
from tabulate import tabulate
class Barang:
	def __init__ (self,nama,harga=0,total_semua=0):
		self.nama = nama
		self.harga = harga
		self.total_semua = total_semua

	def info(self):
		return self.nama+': Rp.{:,.2f}'.format(self.harga)

	def total(self,jumlah):
		bayar = jumlah * self.harga

		return round(bayar)
	def pembayaran(self,duit,kembalian=0):
		self.kembalian = duit - self.total_semua

		return 'Kembalian Pelanggan: Rp.{:,.2f}'.format(self.kembalian)

	def total_belanja(self):
		for daftar in range(len(lv.list_belanja)):
			self.total_semua += lv.list_belanja[daftar][2]
		return self.total_semua

	def struk(self):
		print('-------- STRUK BELANJA --------')
		print(tabulate(lv.list_belanja,tablefmt='pretty',headers=['Nama Barang','Qty','Total'],showindex='Always'))
		#for daftar in range(len(lv.list_belanja)):
		#	list_struk = str(daftar)+'. '+str(lv.list_belanja[daftar][0])+' Qty: '+str(lv.list_belanja[daftar][1])+' Rp.{:,.2f}'.format(lv.list_belanja[daftar][2])
		#	print('| '+list_struk+' |')
		print('--------------------------------')
		print('| Total Semua Belanja: Rp.{:,.2f}'.format(self.total_semua))
		print('---------------------------------')
		
