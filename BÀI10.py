# Nhập mức lương cơ bản và số ngày công
luong_co_ban = float(input("Nhập mức lương cơ bản: "))
so_ngay_cong = float(input("Nhập số ngày công trong tháng: "))

# Lương một ngày
luong_1_ngay = luong_co_ban / 22

# Tính lương theo số ngày công
luong_thuc_nhan = luong_1_ngay * so_ngay_cong

# Tính tiền thưởng hoặc tiền phạt
if so_ngay_cong > 22:
    luong_thuc_nhan += luong_thuc_nhan * 0.1  # thưởng 10%
elif so_ngay_cong < 22:
    luong_thuc_nhan -= luong_thuc_nhan * 0.05  # phạt 5%

# In kết quả, làm tròn 2 chữ số thập phân
print("Tổng lương thực nhận: ", round(luong_thuc_nhan, 2))