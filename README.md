# inventory-investment-dashbord
**Fiber Optic Maintenance Inventory & Investment Dashbord**

Dashbord berasis python yang secara spesifik dibuat untuk mengontrol modal material pekerjaan pemeliharaaan (maintenance) fiber optik telekomunikasi. Dashbord ini menyediakan dua pilihan pelaku (user role)--**Stokis** dan **Investor**. Dengan berkelindannya dua data dari dua pilihan pelaku, Investor dapat melihat report seketika (real time)

**User Role**
-Meminta user untuk memilih, apakah masuk sebagai Investor atau Stokis.

**Fitur Stokis**
-Add Material: Menambah material baru.
-View Material: Melihat tabel inventori.
-Update Material: 
                  -Menambah stok material.
                  -Menambah penggunaan material
-Delete Material: Menghapus material.
#Catatan: Aksi apa pun yang dilakukan Stockist, akan otomatis memengaruhi keseluruhan data penghitungan (tabel investasi) investor.

**Fitur Investor**
-Investor Snapshot:
Untuk setiap material:
  -Total material yang sudah dibeli (BeginningBalance + Purchases)
  -Total harga material yang sudah dibeli (Units_Acquired × Unit_Cost)

-Profit and Loss
Untuk setiap material:
  -Revenue  (Units_Issued × Unit_Selling_Price)
  -Cost of Goods Sold (COGS) (Units_Issued × Unit_Cost)
  -Gross Profit: (Revenue – COGS)
  -Tax (PPH) (4% x Revenue)
  -Net-Profit  (Gross Profit - Tax)
  - Net Margin ((Net Profit / Revenue) x 100)
  - Return of Investment ((Net Profit / COGS) * 100)

-Summary:
Penjumlahan (sum) dari semua material: revenue, COGS, Gross Profit, Tax, Net Profit,       Overall Net Margin dan Overall ROI

=======================================================================================
**Requirements**
-Python 3.8+
-Package: tabulate


