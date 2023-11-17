#國泰世華程式邏輯題目第一題
test_list=[53,64,75,19,92,100,6]

def switch_data_func(data_list):
    tmp_list=[]
    for get_data in data_list:
        get_data=str(get_data)
        if len(get_data)==2:
            for i in range(len(get_data)-1,0,-1):
                print(f"{get_data[i]}{get_data[i-1]}")
                connect_data=get_data[i]+get_data[i-1]
                tmp_list.append(int(connect_data))
                print("----------------")
        elif len(get_data)==3:  #100分的情況出現~
            special_data=get_data[2]+get_data[1]+get_data[0]
            tmp_list.append(special_data) #不過001只能是字串 沒法轉數字xD
            print("----------------")
        else: # 1位數情況
            tmp_list.append(get_data[0])

    return tmp_list


result=switch_data_func(test_list)     
print(result)
