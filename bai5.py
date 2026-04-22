import matplotlib.pyplot as plt

so_luong = {'Laptop': 10, 'Mouse': 50, 'Keyboard': 30}

gia_tien = {'Laptop': 20*10**6, 'Mouse': 20*10**3, 'Keyboard': 50*10**3}

doanh_thu = {}
for mat_hang, sl in so_luong.items():
    gia = gia_tien[mat_hang]
    doanh_thu[mat_hang] = sl * gia

tong_doanh_thu = sum(doanh_thu.values())

print("Báo cáo doanh thu")
for mat_hang in so_luong:
    print(f"{mat_hang}: {so_luong[mat_hang]} sản phẩm x {gia_tien[mat_hang]} VND = {doanh_thu[mat_hang]} VND")
print(f"\nTỔNG DOANH THU: {tong_doanh_thu} VND")

mat_hangs = list(so_luong.keys())
so_luongs = list(so_luong.values())

plt.figure(figsize=(8, 5), dpi=100)
plt.bar(mat_hangs, so_luongs, color=['blue', 'green', 'red'])
plt.title('Số lượng sản phẩm đã bán', fontsize=14)
plt.xlabel('Mặt hàng', fontsize=12)
plt.ylabel('Số lượng (chiếc)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(so_luongs):
    plt.text(i, v + 1, str(v), ha='center', va='bottom', fontweight='bold')

plt.tight_layout(pad=2.0)
plt.savefig('bieu_do_doanh_thu.png', dpi=300, bbox_inches='tight')
print("Đã lưu hình ảnh: bieu_do_doanh_thu.png")
plt.show()