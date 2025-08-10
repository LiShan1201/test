import random

def guess_number_game():
    # 生成1-100之间的随机数
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字，你有10次机会猜它。")
    
    while attempts < 10:
        try:
            guess = int(input("\n请输入你猜的数字: "))
            attempts += 1
            
            if guess < secret_number:
                print("太小了！再试一次。")
            elif guess > secret_number:
                print("太大了！再试一次。")
            else:
                print(f"恭喜你！你在第{attempts}次猜中了数字{secret_number}！")
                return
                
            print(f"你还剩{10 - attempts}次机会。")
            
        except ValueError:
            print("请输入有效的数字！")
    
    print(f"\n游戏结束！正确的数字是{secret_number}。")

# 启动游戏
if __name__ == "__main__":
    guess_number_game()