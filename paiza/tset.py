from paiza_test import*
input_text="""5
0 10 10 3
3
200 0 2 0 0
160 1 0 0 0
170 1 0 0 0
"""

def_input(input_text)

n=int(input())

input_list = list(map(int, input().split(" ")))
N = int(input())
line = [list(map(int, input().split(" "))) for _ in range(N)]

  
for i in line:
  value = i[0]
  投入コイン = i[1:]
  投入金額 = 投入コイン[0] * 500 + 投入コイン[1] * 100 + 投入コイン[2] * 50 + 投入コイン[3] * 10
  お釣り = 投入金額 - value
  お釣りコイン = list(map(int,list(str(お釣り).zfill(4))))
  print(input_list)
  print(お釣りコイン)

  index_list = [0,1,2,3]
  new = []
    
  for index, cinput , coin in zip(index_list,input_list,お釣りコイン):
    if index == 2:
      fix_index = 2
      break
    noname = cinput - coin
    if noname >= 0:
      new.append(noname)
    else:
      fix_index = index
      break
  
  def i100():
    noname3 = input_list[1] - お釣りコイン[1]
    if input_list[1] == 0:
      return お釣りコイン[1]
    elif noname3 >= 0:
      new.append(noname3)
      return 0 
    elif noname3 < 0:
      new.append(0)
      return (お釣りコイン[1] - input_list[1]) * 2
    
  def i50(skip = 0):
    # 例
    if input_list[2] == 0 and skip >= 2:
      return "False"
    elif input_list[2] == 0 or お釣りコイン[2] + skip < 5:
      new.append(input_list[2])
      return お釣りコイン[2] + skip
    # 通常
    else:
      new.append(input_list[2] - 1)
      return お釣りコイン[2] + skip - 5
    
  def i10(skip):
    if skip == "False":
      print("impossible")
      return False
    noname2 = input_list[3] - (お釣りコイン[3] + skip)
    if noname2 >= 0 and input_list[3] - noname2 < 10:
      new.append(noname2)
      return True
    else:
      print("impossible")
      return False
      
  if fix_index == 1:
    skip = i100()
    if skip >= 2:
      print("impossible")
      continue
    skip = i50(skip)
    a = i10(skip)
    
  elif fix_index == 2:
    skip = i50()
    a = i10(skip)
    
  if a:
    result = list(map(lambda x,y: x-y ,input_list,new))
    print(" ".join(list(map(str,result))))
    input_list = list(map(lambda x,y: x+y ,投入コイン,new))