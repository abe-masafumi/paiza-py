from paiza_test import*
input_text="""5
1 4 1 20
3
130 1 0 0 0
150 0 2 0 0
100 1 0 0 0
"""

def_input(input_text)

n=int(input())

input_list = list(map(int, input().split(" ")))
# print(input_list)
N = int(input())
# print(N)
line = [list(map(int, input().split(" "))) for _ in range(N)]
# print(line)

for i in line:
  print(input_list)
  value = i[0]
  投入コイン = i[1:]
  # print(投入コイン)
  # print(use)
  投入金額 = 投入コイン[0] * 500 + 投入コイン[1] * 100 + 投入コイン[2] * 50 + 投入コイン[3] * 10
  # print(投入金額)
  お釣り = 投入金額 - value
  お釣りコイン = list(map(int,list(str(お釣り).zfill(4))))
  print(お釣りコイン)
  index_list = [0,1,2,3]
  new = []
  for index, cinput , coin in zip(index_list,input_list,お釣りコイン):
    if index == 2:
      fix_index = 2
      break
    print(f"index : {index},", cinput, coin)
    noname = cinput - coin
    if noname >= 0:
      new.append(noname)
      print("計算できる")
    else:
      print("計算できない")
      fix_index = index
      break
  
  print(fix_index)
  print(new)
  def i100():
    noname3 = input_list[1] - お釣りコイン[1]
    if input_list[1] == 0:
      return お釣りコイン[1]
    elif noname3 >= 0:
      new.append(noname3)
      return 0 
    elif noname3 <= 0:
      new.append(input_list[1])
      return お釣りコイン[1] - input_list[1] * 2
    
    
  def i50(skip = 0):
    # 例
    if input_list[2] == 0 or お釣りコイン[2] + skip < 5:
      new.append(0)
      return お釣りコイン[2] + skip
    # 通常
    else:
      new.append(input_list[2] - 1)
      return お釣りコイン[2] + skip - 5
    
  def i10(skip):
    noname2 = input_list[3] - (お釣りコイン[3] + skip)
    if noname2 >= 0 and noname2 < 10:
      new.append(noname2)
      return True
    else:
      print("impossible")
      return False
      
  if fix_index == 1:
    skip = i100()
    skip = i50(skip)
    a = i10(skip)
    
  elif fix_index == 2:
    skip = i50()
    print(skip)
    a = i10(skip)
  
  elif fix_index == 3:
    a = i10(skip)
    
  if a:
    result = list(map(lambda x,y: x-y ,input_list,new))
    print(" ".join(list(map(str,result))))
    input_list = new
  

  
      
    
    
  

    

  
  
  
  
      
      
  
  
  
  
  
  
  end = "--------------"
  print(end)

 

