# Nhập số tiền VNĐ từ bàn phím
vnd = float(input("Nhập số tiền (VNĐ): "))

# Tỷ giá quy đổi
ty_gia = 24500

# Chuyển đổi sang USD
usd = vnd / ty_gia

# In kết quả, làm tròn đến 2 chữ số thập phân
print("Số tiền tương đương:", round(usd, 2), "USD")