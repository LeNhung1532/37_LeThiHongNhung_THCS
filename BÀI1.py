# Nhập giá sản phẩm và số lượng mua
gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))

# Tính tổng chi phí (chưa thuế)
tong_chi_phi = gia * so_luong

# Tính thuế VAT 10%
thue_vat = tong_chi_phi * 0.10

# Tính tổng tiền phải trả
tong_tien = tong_chi_phi + thue_vat

# In kết quả, làm tròn 2 chữ số thập phân
print("Tổng chi phí (chưa thuế):", round(tong_chi_phi, 2))
print("Thuế VAT (10%):", round(thue_vat, 2))
print("Tổng tiền phải trả:", round(tong_tien, 2))