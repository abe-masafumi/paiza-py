# 配列の操作

---

# 配列の置換

[配列の置換と回転](https://qiita.com/rudorufu1981/items/5341d9603ecb1f9c2e5c)
[配列の置換_zip](https://jackee777.hatenablog.com/entry/2019/05/03/223646)

    ```py
    print([1, 2, 3])
    print([4, 5, 6])
    print([7, 8, 9])
    # 右回転
    S = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for x in zip(*S[::-1]):
      print(*x,sep='')

    # 左回転
    S = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    T_S = list(zip(*S))
    for x in T_S[::-1]:
        print(*x,sep='')
    ```

# listの重複を削除

  [Pythonでリスト（配列）に重複した要素があるか判定](https://note.nkmk.me/python-list-duplicate-check/)
