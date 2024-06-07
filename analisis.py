import pandas as pd

# Membaca data dari file CSV
penjualan = pd.read_csv('penjualan.csv')
pembelian = pd.read_csv('pembelian.csv')
persediaan = pd.read_csv('persediaan.csv')
pelanggan = pd.read_csv('pelanggan.csv')
supplier = pd.read_csv('supplier.csv')
invoice_penjualan = pd.read_csv('invoice_penjualan.csv')
invoice_pembelian = pd.read_csv('invoice_pembelian.csv')

# Menampilkan data
print("Data Penjualan:\n", penjualan)
print("\nData Pembelian:\n", pembelian)
print("\nData Persediaan:\n", persediaan)
print("\nData Pelanggan:\n", pelanggan)
print("\nData Supplier:\n", supplier)
print("\nData Invoice Penjualan:\n", invoice_penjualan)
print("\nData Invoice Pembelian:\n", invoice_pembelian)
# Menghitung total penjualan per produk
total_penjualan_per_produk = penjualan.groupby('Kode_Produk')['Total_Harga'].sum().reset_index()
total_penjualan_per_produk.columns = ['Kode_Produk', 'Total_Penjualan']

print("\nTotal Penjualan per Produk:\n", total_penjualan_per_produk)
# Menghitung total pembelian per produk
total_pembelian_per_produk = pembelian.groupby('Kode_Produk')['Total_Harga'].sum().reset_index()
total_pembelian_per_produk.columns = ['Kode_Produk', 'Total_Pembelian']

print("\nTotal Pembelian per Produk:\n", total_pembelian_per_produk)
# Menghitung stok akhir berdasarkan penjualan dan pembelian
stok_awal = persediaan.set_index('Kode_Produk')['Stok_Awal']
jumlah_terjual = penjualan.groupby('Kode_Produk')['Jumlah'].sum()
jumlah_terbeli = pembelian.groupby('Kode_Produk')['Jumlah'].sum()

stok_akhir = stok_awal + jumlah_terbeli - jumlah_terjual
stok_akhir = stok_akhir.reset_index()
stok_akhir.columns = ['Kode_Produk', 'Stok_Akhir']

print("\nStok Akhir Berdasarkan Penjualan dan Pembelian:\n", stok_akhir)
import pandas as pd

# Membaca data dari file CSV
penjualan = pd.read_csv('penjualan.csv')
pembelian = pd.read_csv('pembelian.csv')
persediaan = pd.read_csv('persediaan.csv')
pelanggan = pd.read_csv('pelanggan.csv')
supplier = pd.read_csv('supplier.csv')
invoice_penjualan = pd.read_csv('invoice_penjualan.csv')
invoice_pembelian = pd.read_csv('invoice_pembelian.csv')

# Menampilkan data
print("Data Penjualan:\n", penjualan)
print("\nData Pembelian:\n", pembelian)
print("\nData Persediaan:\n", persediaan)
print("\nData Pelanggan:\n", pelanggan)
print("\nData Supplier:\n", supplier)
print("\nData Invoice Penjualan:\n", invoice_penjualan)
print("\nData Invoice Pembelian:\n", invoice_pembelian)

# Menghitung total penjualan per produk
total_penjualan_per_produk = penjualan.groupby('Kode_Produk')['Total_Harga'].sum().reset_index()
total_penjualan_per_produk.columns = ['Kode_Produk', 'Total_Penjualan']
print("\nTotal Penjualan per Produk:\n", total_penjualan_per_produk)

# Menghitung total pembelian per produk
total_pembelian_per_produk = pembelian.groupby('Kode_Produk')['Total_Harga'].sum().reset_index()
total_pembelian_per_produk.columns = ['Kode_Produk', 'Total_Pembelian']
print("\nTotal Pembelian per Produk:\n", total_pembelian_per_produk)

# Menghitung stok akhir berdasarkan penjualan dan pembelian
stok_awal = persediaan.set_index('Kode_Produk')['Stok_Awal']
jumlah_terjual = penjualan.groupby('Kode_Produk')['Jumlah'].sum()
jumlah_terbeli = pembelian.groupby('Kode_Produk')['Jumlah'].sum()

stok_akhir = stok_awal.add(jumlah_terbeli, fill_value=0).sub(jumlah_terjual, fill_value=0).reset_index()
stok_akhir.columns = ['Kode_Produk', 'Stok_Akhir']
print("\nStok Akhir Berdasarkan Penjualan dan Pembelian:\n", stok_akhir)
