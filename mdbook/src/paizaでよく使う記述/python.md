# python

pythonの環境構築 実行方法

[youtube_ Pythonの超基本的な部分をたった1時間で学べます](https://www.youtube.com/watch?v=HyU3XL2F9GE&t=827s)

[再帰関数](https://qiita.com/drken/items/23a4f604fa3f505dd5ad)

----

1. for文の使い方
   [for文_range](https://blog.kikagaku.co.jp/python-for-range)
   ```py
   names = ['太郎', '花子', '一郎']
   for name in names:
    print(name +'さん')
   ```

   ```py
   for i in range(3):
   # or
   # 5 から 9 まで連番を出力
   for i in range(5,10):
   # or
   # 5 から 9 まで２コ飛ばしで出力
   for i in range(5,10,2):
   ```

   ```py
   
   ```



   for_in 文で"key"と"value"を取得
   ```py
   arr = ["a","b","c"]
   for key,ar in enumerate(arr):
   print(key,ar)
    # 0 a
    # 1 b
    # 2 c
   ```

2. jsonファイルの読み込み

   [jsonファイルの読み込み](https://qiita.com/kikuchiTakuya/items/53990fca06fb9ba1d8a7)