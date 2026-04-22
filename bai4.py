import random
import os

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_hint(secret, used_hints=None):
    if used_hints is None:
        used_hints = []
    
    hints = []
    hints.append(f"Số cần tìm là số {'chẵn' if secret % 2 == 0 else 'lẻ'}.")
    if secret <= 33:
        hints.append("Số cần tìm nằm trong khoảng 1 - 33.")
    elif secret <= 66:
        hints.append("Số cần tìm nằm trong khoảng 34 - 66.")
    else:
        hints.append("Số cần tìm nằm trong khoảng 67 - 100.")
    if secret % 5 == 0:
        hints.append("Số cần tìm chia hết cho 5.")
    if is_prime(secret):
        hints.append("Số cần tìm là số nguyên tố.")
    if secret % 3 == 0:
        hints.append("Số cần tìm chia hết cho 3.")
    
    available_hints = [h for h in hints if h not in used_hints]
    
    if not available_hints:
        available_hints = hints
    
    selected_hint = random.choice(available_hints)
    used_hints.append(selected_hint)
    
    return selected_hint, used_hints

def load_high_score():
    if os.path.exists("high_score.txt"):
        try:
            with open("high_score.txt", "r") as f:
                data = f.read().strip()
                if data:
                    return int(data)
        except:
            pass
    return None

def save_high_score(score):
    with open("high_score.txt", "w") as f:
        f.write(str(score))

def play_game():
    high_score = load_high_score()
    print("Trò chơi Đoán Số Bí Mật")
    print("Máy tính đã chọn một số từ 1 đến 100.")
    print("Bạn có TỐI ĐA 7 LẦN ĐOÁN.")
    if high_score:
        print(f"Kỷ lục của bạn: {high_score} lần đoán.")
    else:
        print("Chưa ghi nhận kỷ lục nào. Hãy chơi thử lần đầu!")
    
    secret = random.randint(1, 100)
    used_hints = []
    hint, used_hints = get_hint(secret, used_hints)
    print(f"\n Gợi ý 1: {hint}")
    
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\n Lượt {attempts + 1}/{max_attempts} (bạn còn {remaining} lượt) ")
        try:
            guess = int(input("Nhập số bạn đoán: "))
            if guess < 1 or guess > 100:
                print("Vui lòng nhập số trong khoảng 1-100.")
                continue
        except ValueError:
            print("Lỗi: Bạn phải nhập một số nguyên trong khoảng 1-100! Hãy thử lại.")
            continue
        
        attempts += 1
        
        if guess == secret:
            print(f"\n CHÚC MỪNG! Bạn đã đoán đúng số bí mật:{secret} sau {attempts} lần đoán!")
            if high_score is None or attempts < high_score:
                print(f"KỶ LỤC MỚI! Bạn đã phá vỡ kỷ lục cũ ({high_score if high_score else 'vô cùng'}) với {attempts} lần đoán!")
                save_high_score(attempts)
            else:
                print(f"Kỷ lục hiện tại vẫn là {high_score} lần đoán. Cố gắng hơn lần sau!")
            return  
        elif guess < secret:
            print("Số cần tìm LỚN HƠN số bạn vừa đoán.")
        else:
            print("Số cần tìm NHỎ HƠN số bạn vừa đoán.")
        
        if attempts >= 5 and attempts < max_attempts and guess != secret:
            extra_hint, used_hints = get_hint(secret, used_hints)
            print(f"Gợi ý thêm: {extra_hint}")
    
    print(f"\n Bạn đã hết lượt! Số bí mật là {secret}. Chúc bạn may mắn lần sau!")

def main():
    while True:
        play_game()
        print("\n" + "=" * 40)
        again = input("Bạn có muốn chơi lại không? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("Cảm ơn bạn đã chơi! Hẹn gặp lại.")
            break
        print("\n" * 2)

if __name__ == "__main__":
    main()