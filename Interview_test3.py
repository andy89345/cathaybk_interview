#國泰世華程式邏輯題目第三題
def circle_QA(n):
    if n!=0:
        colleagues = list(range(1, n + 1))
        current_data = 0
        count = 0

        while len(colleagues) > 1:
            print(f"colleagues : {colleagues} count : {count} current_data : {current_data}")
            count += 1
            
            if count == 3:
                colleagues.pop(current_data)
                count = 0
            else:
            
                current_data = (current_data + 1) % len(colleagues)
        return colleagues[0]
    
    else:
        return 0
    


n = int(input("請輸入同事的人數："))
result = circle_QA(n)
print(f"第 {result} 順位。")

