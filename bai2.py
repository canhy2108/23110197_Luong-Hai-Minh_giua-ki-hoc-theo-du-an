def chuan_hoa(ho_ten):
    start = 0
    end = len(ho_ten) - 1
    while start <= end and ho_ten[start] == ' ':
        start += 1
    while end >= start and ho_ten[end] == ' ':
        end -= 1
    
    if start > end:
        return ""
    
    trimmed = ho_ten[start:end+1]
    
    result = []
    prev_space = False
    length = len(trimmed)
    
    for i in range(length):
        ch = trimmed[i]
        if ch == ' ':
            if not prev_space:
                result.append(' ')
                prev_space = True
        else:
            if i == 0 or trimmed[i-1] == ' ':
                if 'a' <= ch <= 'z':
                    result.append(chr(ord(ch) - 32))
                else:
                    result.append(ch)
            else:
                if 'A' <= ch <= 'Z':
                    result.append(chr(ord(ch) + 32))
                else:
                    result.append(ch)
            prev_space = False
    
    return ''.join(result)

def sap_xep_theo_ten_bubblesort(danh_sach):
    n = len(danh_sach)
    for i in range(n - 1):
        for j in range(n - i - 1):
            ten1 = danh_sach[j].split()[-1]
            ten2 = danh_sach[j + 1].split()[-1]
            if ten1 > ten2:
                # Đổi chỗ
                danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
    return danh_sach

ds = [" nguYen vaN a ", "tRAn tHi b", "  le   van    c "]

ds_chuan = [chuan_hoa(x) for x in ds]

ds_sap_xep = sap_xep_theo_ten_bubblesort(ds_chuan)

print("Danh sách sau khi chuẩn hóa và sắp xếp:")
for ten in ds_sap_xep:
    print(ten)
