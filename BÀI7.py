import getpass

username = input("Nhập tên đăng nhập: ")
password = getpass.getpass("Nhập mật khẩu: ")

if username == "admin" and password != "password123":
    print("Quyền truy cập được cấp.")
else:
    print("Không được cấp quyền.")
