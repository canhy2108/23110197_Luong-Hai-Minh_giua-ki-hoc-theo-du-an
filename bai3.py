def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def usd_to_vnd(usd, rate):
    return usd * rate

def vnd_to_usd(vnd, rate):
    return vnd / rate

def main():
    print("Ứng dụng chuyển đổi đơn vị")
    
    while True:
        try:
            exchange_rate = float(input("Nhập tỷ giá USD/VND: "))
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập một số hợp lệ cho tỷ giá!")
    
    while True:
        print("\nChọn chức năng chuyển đổi:")
        print("1. Độ C -> Độ F")
        print("2. Độ F -> Độ C")
        print("3. USD -> VND")
        print("4. VND -> USD")
        print("5. Thoát")
        
        choice = input("Nhập lựa chọn (1-5): ")
        
        if choice == '5':
            print("Cảm ơn bạn đã sử dụng ứng dụng. Tạm biệt!")
            break
        
        if choice in ('1', '2'):
            try:
                temp = float(input("Nhập giá trị nhiệt độ: "))
                if choice == '1':
                    result = celsius_to_fahrenheit(temp)
                    print(f"{temp}°C = {result:.2f}°F")
                else:
                    result = fahrenheit_to_celsius(temp)
                    print(f"{temp}°F = {result:.2f}°C")
            except ValueError:
                print("Lỗi: Bạn phải nhập một số! Vui lòng thử lại.")
        
        elif choice in ('3', '4'):
            try:
                amount = float(input("Nhập số tiền: "))
                if choice == '3':
                    result = usd_to_vnd(amount, exchange_rate)
                    print(f"{amount:.2f} USD = {result:.2f} VND (tỷ giá {exchange_rate})")
                else:
                    result = vnd_to_usd(amount, exchange_rate)
                    print(f"{amount:.2f} VND = {result:.2f} USD (tỷ giá {exchange_rate})")
            except ValueError:
                print("Lỗi: Bạn phải nhập một số! Vui lòng thử lại.")
            except ZeroDivisionError:
                print("Lỗi: Tỷ giá không thể bằng 0 khi chuyển từ VND sang USD.")
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()