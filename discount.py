harga = float(input('Masukan jumlah pembelian '))
anggota = input('Status anggota(Premium/Reguler/bukan anggota): ').lower()
diskon = 0

if harga >= 500000:
    if anggota == "premium":
        diskon = 0.25
    elif anggota == "reguler":
        diskon = 0.15
    else :
        diskon = 0.10
elif 200000 <= harga <= 500000:
    if anggota == "premium":
        diskon = 0.15
    elif anggota == "reguler":
        diskon = 0.10
    else :
        diskon = 0.05
else:
    if anggota == "premium":
        diskon = 0.10
    elif anggota == "reguler":
        diskon = 0.05
    else :
        diskon = 0
        
        
total_diskon = harga * diskon
total_harga = harga - total_diskon

print(f"Diskon yang didapat: {diskon * 100}%")
print(f"Total diskon: Rp {total_diskon}")
print(f"Total Harga : Rp {total_harga}")