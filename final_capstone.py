from tabulate import tabulate

#=========================================
#Data stock awal
#=========================================
data_stock = [
    {"MaterialID": "M001", "MaterialName": "FDT 48",     "BeginningBalance": 10, "Purchases": 5,  "CurrentBalance": 15, "IssuedQuantity": 3,  "EndingBalance": 12, "UnitCost": 1200000, "UnitSellingPrice": 3500000},
    {"MaterialID": "M002", "MaterialName": "Closure 12", "BeginningBalance": 5,  "Purchases": 10, "CurrentBalance": 15, "IssuedQuantity": 2,  "EndingBalance": 13, "UnitCost": 250000,  "UnitSellingPrice": 825000},
    {"MaterialID": "M003", "MaterialName": "Closure 24", "BeginningBalance": 20, "Purchases": 0,  "CurrentBalance": 20, "IssuedQuantity": 5,  "EndingBalance": 15, "UnitCost": 400000,  "UnitSellingPrice": 835000},
    {"MaterialID": "M004", "MaterialName": "Closure 48", "BeginningBalance": 15, "Purchases": 8,  "CurrentBalance": 23, "IssuedQuantity": 7,  "EndingBalance": 16, "UnitCost": 475000,  "UnitSellingPrice": 900000},
    {"MaterialID": "M005", "MaterialName": "Kabel 24",   "BeginningBalance": 50, "Purchases": 10, "CurrentBalance": 60, "IssuedQuantity": 20, "EndingBalance": 40, "UnitCost": 500000,  "UnitSellingPrice": 1500000},
    {"MaterialID": "M006", "MaterialName": "Kabel 28",   "BeginningBalance": 30, "Purchases": 15, "CurrentBalance": 45, "IssuedQuantity": 10, "EndingBalance": 35, "UnitCost": 550000,  "UnitSellingPrice": 1600000},
    {"MaterialID": "M007", "MaterialName": "Pole 7",     "BeginningBalance": 12, "Purchases": 5,  "CurrentBalance": 17, "IssuedQuantity": 4,  "EndingBalance": 13, "UnitCost": 700000,  "UnitSellingPrice": 2000000},
    {"MaterialID": "M008", "MaterialName": "Pigtail",    "BeginningBalance": 25, "Purchases": 10, "CurrentBalance": 35, "IssuedQuantity": 12, "EndingBalance": 23, "UnitCost": 150000,  "UnitSellingPrice": 500000},
    {"MaterialID": "M009", "MaterialName": "Closure 12", "BeginningBalance": 18, "Purchases": 6,  "CurrentBalance": 24, "IssuedQuantity": 8,  "EndingBalance": 16, "UnitCost": 250000,  "UnitSellingPrice": 825000},
    {"MaterialID": "M010", "MaterialName": "Splitter",   "BeginningBalance": 8,  "Purchases": 12, "CurrentBalance": 20, "IssuedQuantity": 6,  "EndingBalance": 14, "UnitCost": 900000,  "UnitSellingPrice": 2000000}
]

#===========================================================
#Fungsi utama
#===========================================================
#Function untuk narik dict dari data_stock dan netralisir data

def cari_record(data, key, value):
    value=str(value).strip().lower()
    for baris in data:
        if str(baris.get(key, "")).strip().lower()==value:  #pake .get bakal safety net biar ga error kl salah input
            return baris
    return None
     
 #fungsi untuk nampilin tabel 
 
def show_stock():
    if data_stock:
        print("\n=== Material Inventory ===")
        print(tabulate(data_stock, headers="keys", tablefmt="fancy_grid")) 
    else:
        print("Data stock kosong.")
        
 
 #===========================================================
 #Fungsi buat stockist (tambah, lihat, update (sub-update), hapus)
 #==========================================================

#if stockist pilih nambah material
def tambah_stock():
    show_stock()
    print("\n--- Add New Material ---")
    material_id=input("Enter Material ID: ")
    if cari_record(data_stock, "MaterialID", material_id):  #pake if dulu. kalo umpan baliknya false, berarti ga ada duplikat
        print("Error: Material ID already exists!")
        return
    nama = (input("Enter Material Name: "))
    begi = int(input("Enter Beginning Balance: "))
    purch =int(input("Enter Purchases: "))
    h_satuan=int(input("Enter Unit Cost: "))
    h_po=int(input("Enter Unit Selling Price: "))

    curr=begi+purch
    issued = 0
    ending = curr

    stock_tambah={                                          #hasil input, bikin dict baru
        "MaterialID": material_id.strip().upper(),
        "MaterialName": nama,
        "BeginningBalance": begi,
        "Purchases": purch,
        "CurrentBalance": curr,
        "IssuedQuantity": issued,
        "EndingBalance": ending,
        "UnitCost": h_satuan,
        "UnitSellingPrice": h_po
    }
    data_stock.append(stock_tambah)
    print("Material successfully added!")

#if stockist pilih liat stock
def lihat_stock():
    show_stock()

#if stockist pilih update stock
def update_stock():
    show_stock()
    print("\n--- Update Material ---")
    material_id=input("Enter Material ID to update: ")
    record=cari_record(data_stock, "MaterialID", material_id)       #simpen hasil di variable record
    if not record:                                                  #safety net
        print("Error: Material not found.")
        return
    print("1. Add Purchases")                                       #kasih dua pilihan update
    print("2. Issue Stock (Usage)")
    choice=input("Choose option (1/2): ")
    if choice=="1":
        qty=int(input("Enter quantity puchased (masukan dalam angka): "))
        record["Purchases"]+=qty                                     #update variable record
        record["CurrentBalance"]+=qty
        record["EndingBalance"]+=qty
        print("Purchases updated successfully!")
    elif choice=="2":
        qty=int(input("Enter quantity issued (masukan dalam angka): "))
        if qty>record["EndingBalance"]:                             #safety net bila pemakaian di atas stock
            print("Error: Not enough stock to issue.")
        else:                                                       #berhasil issued
            record["IssuedQuantity"]+=qty
            record["EndingBalance"]-=qty
            print("Stock issued successfully!")
    else:
        print("Invalid choice.")

#if stockist pilih hapus stock
def hapus_stock():
    show_stock()
    print("\n--- Delete Material ---")
    material_id=input("Enter Material ID to delete: ")
    record=cari_record(data_stock, "MaterialID", material_id)
    if not record:                                                  #safety net
        print("Error: Material not found.")
        return
    confirm=input(f"Are you sure you want to delete Material ID {material_id}? (y/n): ")
    if confirm.lower()=="y":
        data_stock.remove(record)
        print("Material deleted successfully!")
    elif confirm.lower()=="n":
        print("Deletion cancelled.")
    else:
        print("Invalid choice. Deletion cancelled.")
    
#===========================================================
 #Fungsi buat investor (table report, sub tabel & summary)
 #==========================================================


#snapshot
def lihat_snapshot():
    if not data_stock:                                                              #safety_net
        print("No stock data available for investor report. Please contact stockist")
        return "investor"                                                                 

    snapshot = []
    for s in data_stock:
        unitsacquired = s["BeginningBalance"] + s["Purchases"]
        unitcost = s["UnitCost"]
        total_acq= unitsacquired * unitcost
        
        snapshot.append({
            "MaterialID": s["MaterialID"],
            "Units_Acquired": unitsacquired,
            "Unit_Cost": unitcost,
            "Total Acqusition Cost": total_acq,
        })
    print("\n=== Inventory Snapshot ===")
    print(tabulate(snapshot, headers="keys", tablefmt="fancy_grid"))

    print("\n---------------------")
    print("1. Back to Investor Menu")
    print("2. Back to Main Menu")
    pilih = input("Choose option: ").strip()
    return "main" if pilih=="2" else "investor"
   
#profit and loss
def lihat_pnl():
    if not data_stock:                                                              #safety_net
        print("No stock data available for investor report. Please contact stockist")
        return "investor"
    pnl = []
    for s in data_stock:
        unitdipake = s["IssuedQuantity"]
        p_unit_po = s["UnitSellingPrice"]
        unit_cost = s["UnitCost"]

        revenue = unitdipake * p_unit_po
        cogs = unitdipake * unit_cost
        gross_profit = revenue - cogs
        pph = round(revenue * 0.04)
        net_profit = gross_profit - pph
        net_margin=round((net_profit/revenue)*100,2) if revenue>0 else 0 #biar ga error kl revenue di bawah 0
        roi=round((net_profit/cogs)*100,2) if cogs>0 else 0               #biar ga error kl cogs di bawah 0

        pnl.append({
            "MaterialID": s["MaterialID"],
            "Units_Issued": unitdipake,
            "Cost Of Goods Sold": cogs,
            "Revenue": revenue,
            "Gross Profit": gross_profit,
            "pph (%)": pph,
            "Net_Profit": net_profit,
            "Net_Margin (%)": net_margin,
            "ROI (%)": roi

        })
    print("\n=== Profit and Loss Report ===")
    print(tabulate(pnl, headers="keys", tablefmt="fancy_grid"))

    #summary
    total_cogs = sum(item["Cost Of Goods Sold"] for item in pnl)            #pake generator expression biar ringkas
    total_revenue = sum(item["Revenue"] for item in pnl)
    total_gross = sum(item["Gross Profit"] for item in pnl)
    total_tax = sum(item['pph (%)']for item in pnl)
    total_net = sum(item["Net_Profit"] for item in pnl)
    net_margin=round((total_net/total_revenue)*100,2) if total_revenue>0 else 0
    roi=round((total_net/total_cogs)*100,2) if total_cogs>0 else 0

    print("\n=== Investor Summary Report ===")
    print(f"Total Cost Of Goods Sold: {total_cogs}")
    print(f"Total Revenue: {total_revenue}")
    print(f"Total Gross Profit: {total_gross}")
    print(f"Total Tax (PPH 4%): {total_tax}")
    print(f"Total Net Profit: {total_net}")
    print(f"Overall Net Margin (%): {net_margin}")
    print(f"Overall ROI (%): {roi}")
    print("\n---------------------")
    print("1. Back to Investor Menu")
    print("2. Back to Main Menu")
    pilih = input("Choose option: ").strip()
    return "main" if pilih == "2" else "investor"   
          


#===========================================================
 # Sub-Menu
 #==========================================================

#Menu Stockist
def menu_stockist():
    while True:
        print("\n=== Stockist Menu ===")
        print("1. Add Material")
        print("2. View Materials")
        print("3. Update Material")
        print("4. Delete Material")
        print("5. Back to Main Menu")
        choice=input("Choose an option (1-5): ")
        if choice=="1":
            tambah_stock()
        elif choice=="2":
            lihat_stock()
        elif choice=="3":
            update_stock()
        elif choice=="4":
            hapus_stock()
        elif choice=="5":
            break
        else:
            print("Invalid choice. Please try again.")

#Menu Investor
def menu_investor():
    while True:
        print("\n=== Investor Menu ===")
        print("1. View Inventory Snapshot")
        print("2. View Profit and Loss Report")
        print("3. Back to Main Menu")
        choice=input("Choose an option (1-3): ")

        if choice=="1":
            next_menu=lihat_snapshot()
            if next_menu=="main":                   #nerima umpan balik dari fungsi jeroan
                return
        elif choice=="2":
            next_menu=lihat_pnl()
            if next_menu=="main":                   #nerima umpan balik dari fungsi jeroan
                return
        elif choice=="3":
            return                                  #keluar ke menu utama
        else:
            print("Invalid choice.")

#===========================================================
 # Menu Utama
 #==========================================================
judul = "Fiber Optic Maintenance Inventory & Investment Dashboard"

def menu_utama():
    while True:
        print("\n" + "=" * 70)
        print(judul.center(70))
        print("=" * 70)
        print("\nSelect User Role:")
        print("[1] Stockist")
        print("[2] Investor")
        print("[3] Exit")

        pilih = input("Choose option (1-3): ").strip()

        if pilih == "1":
            menu_stockist()       # fungsi menu stockist
        elif pilih == "2":
            menu_investor()    # fungsi menu investor
        elif pilih == "3":
            print("Exiting program...")
            break              # keluar dari while True → selesai
        else:
            print("Invalid choice. Please try again.")


#===============================
#trigger
#===============================
menu_utama()