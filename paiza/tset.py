from paiza_test import*
import pandas as pd
import numpy as np

input_text="""5
1 4 1 20
3
130 1 0 0 0
150 0 2 0 0
100 1 0 0 0
"""

def_input(input_text)

n=int(input())

N = int(input())
line = [(input()) for _ in range(N)]
line = [list(map(int, i.rstrip().split(" "))) for i in line]
# print(line)
df = pd.DataFrame(line,columns=['value', 'c500', 'c100', 'c50','c10'])
# print(df)
# print(coin)
for i in range(N):
    
    お釣り = (df["c500"][i]*500) + (df["c100"][i]*100) + (df["c50"][i]*50) + (df["c10"][i]*10) - df["value"][i]
    res = np.array(list(map(int,list(str(お釣り).zfill(4)))))
    # print(coin)
    # print(res)
    cost_arr = [0]
    cost = 0
    skip = 0
    
    # １００円
    if coin[1] >= res[1]:
        cost = res[1]
    else:
        cost = coin[1]
        skip = res[1] - coin[1]
            
    cost_arr.append(cost)
    
    # ５０円
    if coin[2]*5 != 0:
        cost = int((res[2] + skip) / (coin[2]*5))
        skip = (res[2]+skip) % (coin[2] *5)
        cost_arr.append(cost)
    else:
        skip = res[2] + skip
        cost_arr.append(0)
    print(skip)
    
    #  1０円
    if coin[3] >= res[3] + skip:
        cost = res[3] + skip 
    else:
        print("impossible")
        break
    cost_arr.append(cost)
    np_cost = np.array(cost_arr)
    print(cost_arr)
    # print(coin)
    add = df.iloc[i,1:].to_list()
    # print(add)
    coin = coin - cost_arr + add
    print(coin)