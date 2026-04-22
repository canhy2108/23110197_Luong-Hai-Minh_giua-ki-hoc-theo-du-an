def input_value():
    quan_ly = []
    while True:
        ten = input("Nhập tên món hàng (nhấn Enter để dừng): ")
        if ten == "":
            break
        try:
            gia = float(input(f"Nhập giá tiền cho {ten}: "))
        except ValueError:
            print("Giá tiền phải là số. Vui lòng nhập lại.")
            continue
        quan_ly.append((ten, gia))
    return quan_ly

def count_and_find_max(quan_ly):
    tong = 0
    for ten, gia in quan_ly:
     tong += gia

    max_price = 0
    for ten, gia in quan_ly:
        if gia > max_price:
            max_item = (ten, gia)
    return tong, max_item

def xuat_file(quan_ly, tong, max_item, ten_file="ket_qua_chi_tieu.txt"):
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("Danh sách chi tiêu:\n")
        for ten, gia in quan_ly:
            f.write(f"- {ten}: {int(gia) if gia % 1 == 0 else gia} VND\n")
        f.write(f"\nTổng số tiền: {int(tong) if tong % 1 == 0 else tong} VND\n")
        f.write(f"Món hàng có giá trị cao nhất: {max_item[0]} ({int(max_item[1]) if max_item[1] % 1 == 0 else max_item[1]} VND)\n")
    print(f"Đã xuất kết quả ra file {ten_file}")

if __name__ == "__main__":
    ds = input_value()
    tong, max_item = count_and_find_max(ds)
    xuat_file(ds, tong, max_item)