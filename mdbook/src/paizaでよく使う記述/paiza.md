# pizaでよく使う

---
[inputの取得](https://www.self-study-blog.com/dokugaku/python-standard-input/)
inputの取得方法

```py
N = int(input())
```

```py
a = input().split(' ')
```

```py
X, Y, Z = input().split()
# or
a, b, c  = map(int, input().split())
# or
input_list = list(map(int, input().split(",")))
print(input_list)
```

```py
line = [] 
 
for i in range(10):
    line.append(input())
```

```py
line = [input() for i in range(10)]
print(line)
```

```py
list(map(int, リスト))
```