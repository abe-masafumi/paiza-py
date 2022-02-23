# scrapy

----

[document](https://docs.scrapy.org/en/latest/index.html)

[事前レンダリング](https://docs.scrapy.org/en/latest/topics/developer-tools.html#topics-network-tool)

[scrapy_おさない](https://www.youtube.com/watch?v=bXBa-88BiYA&list=PL3PnJ18ZwZncApcwG-6YTInB_ZEhjx952&index=2)

[scrapy_環境構築の記事](https://qiita.com/chiguh28/items/7ffd88015c1793ac5a9e)

[xpath css についての記事](https://python.civic-apps.com/scrapy-xpath-css/)

----

- projectの始め方

[doc](https://docs.scrapy.org/en/latest/topics/commands.html)

```bsh
// scrapyをインストール
pip install Scrapy
```

```
// プロジェクトの作成
scrapy startproject levtech
// levtechフォルダが表示されるまで時間がかかる
```

```bsh
cd levtech
```

```bsh
// プロジェクトの管理
scrapy startproject myproject [project_dir]
```


----MAC バージョンアップ後の処置----

brewコマンド

export PATH=/opt/homebrew/bin:/usr/local/bin:$PATH

caskコマンドの仕様変更

https://www.mathkuro.com/mac/brew-cask-command-error/

 googleChromeのバージョンを確認してそれにあったgoogleDriveのバージョンをインストール

 https://pypi.org/project/chromedriver-binary/#history