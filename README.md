# textmining-example
Pythonテキストマイニングサンプル  

# 辞書作成

```
/usr/lib/mecab/mecab-dict-index -d /var/lib/mecab/dic/ipadic-utf8 -u user.dic -f utf-8 -t utf-8 user_dic.csv
```

csvの末尾に改行があるとエラーになる  
```
reading user_dic.csv ... dictionary_rewriter.cpp(136) [ifs] no such file or directory: /var/lib/mecab/dic/ipadic-utf8/rewrite.def
```

# 参考文献

[python3で文章解析をしてみる【テキストマイニングを気軽に始めてみた vol.1】 – MarketEnterprise Tech Blog](https://tech.marketenterprise.co.jp/2016/11/04/python3%E3%81%A7%E6%96%87%E7%AB%A0%E8%A7%A3%E6%9E%90%E3%82%92%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B%E3%80%90%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%83%9E%E3%82%A4%E3%83%8B%E3%83%B3%E3%82%B0%E3%82%92/)  
