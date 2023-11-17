#國泰世華程式邏輯題目第二題
from collections import Counter
test_str="Hello welcome to Cathay 60th year anniversary"


def count_str_func(data):
    tmp_list=[]
    tmp_list_lower=[]
    data=str(data)
    for i in data:
        if str(i) not in tmp_list and i !=" ":
            tmp_list.append(str(i))
            tmp_list_lower.append(str(i).lower())

    counter_data=Counter(data.lower())
    for normal_data,lower_data in zip(tmp_list,tmp_list_lower):
        count_data=counter_data[lower_data]
        print(f"{normal_data} {count_data}")


result=count_str_func(test_str)


