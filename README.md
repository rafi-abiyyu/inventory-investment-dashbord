# inventory-investment-dashbord
## Fiber Optic Maintenance Inventory & Investment Dashboard

Dashboard berbasis **Python** untuk mengontrol modal material pada pekerjaan pemeliharaan (maintenance) **fiber optik**. Aplikasi menyediakan dua **user role**—**Stokis** dan **Investor**—dengan data yang terintegrasi sehingga setiap perubahan stok langsung tercermin pada perhitungan laporan investor.

---

## User Roles
- **Stokis**: mengelola data material (tambah, lihat, perbarui, hapus).
- **Investor**: melihat snapshot inventori dan laporan investasi (PnL, ROI, Net Margin).

---

## Fitur Stokis
- **Add Material**: menambah material baru.  
- **View Material**: melihat tabel inventori.  
- **Update Material**:
  - Tambah stok material (**Purchases**).
  - Catat pemakaian material (**IssuedQuantity**).
- **Delete Material**: menghapus material.

> **Catatan:** Setiap aksi Stokis otomatis memengaruhi data dan perhitungan di sisi Investor.

---

## Fitur Investor

### 1) Investor Snapshot
Untuk setiap material:
- **Total unit dibeli**: `BeginningBalance + Purchases`  
- **Total biaya akuisisi**: `Units_Acquired × Unit_Cost`

### 2) Profit and Loss (per material)
- **Revenue**: `Units_Issued × Unit_Selling_Price`  
- **Cost of Goods Sold (COGS)**: `Units_Issued × Unit_Cost`  
- **Gross Profit**: `Revenue − COGS`  
- **Tax (PPH 4%)**: `0.04 × Revenue`  
- **Net Profit**: `Gross Profit − Tax`  
- **Net Margin (%)**: `(Net Profit / Revenue) × 100`  
- **ROI (%)**: `(Net Profit / COGS) × 100`

### 3) Summary (agregat semua material)
- **Total Revenue**, **Total COGS**, **Total Gross Profit**, **Total Tax**, **Total Net Profit**,  
  **Overall Net Margin (%)**, **Overall ROI (%)**

---

## Requirements
- **Python** 3.8+  
- **tabulate**

---

