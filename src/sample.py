import MeCab

#mecab = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
mecab = MeCab.Tagger('-Ochasen') #デフォルト辞書を使う場合
text = 'イタリアンが食べたいな！'
mecab.parse('')
node = mecab.parseToNode(text)
while node:
    #単語取得
    word = node.surface
    #品詞取得
    pos = node.feature.split(",")[1]
    print('{0} , {1}'.format(word, pos))
    #次の単語へ
    node = node.next
