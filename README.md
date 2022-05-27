# Blog Maker
Markdown形式で書いた文書から、静的なブログを生成するツールです。

## 使い方
1. ブログ用のフォルダを作成する
2. その直下にMarkdown形式で書いた記事を置く
3. `blog.py`を叩く

記事を書く際は、冒頭に次のYAMLヘッダを書いてください。<br>
例:
```md
---
title: ページのタイトルを指定
tag: ページに付けたいタグを書く
date: yyyy-mm-dd で日付を指定する
---

# みだし1
こんにちは。
```

タグを複数つけたい際は、次のようにします。
```md
---
title: ページのタイトルを指定
tag:
- タグ1
- タグ2
date: yyyy-mm-dd で日付を指定する
---
```

`blog.py`を叩くと、ブログ用のフォルダにサブディレクトリ`docs`が作成されます。
その中にある`index.html`(自動生成されます)がブログのトップページとなります。

# プラグインの有効化
YAMLヘッダを次のように書くことで、便利なプラグイン(js)が有効化されます。
```yaml
plug:
    # コードブロックでgraphvizが使えるようになります (言語名にgraphvizを指定)
    graphviz: true
    # コードブロックでlatex記法の擬似コードが使えるようになります (言語名にalgorithmを指定)
    pseudocode: true
    # コードブロックでmermaidが使えるようになります (言語名にmermaidを指定)
    mermaid: true
```
