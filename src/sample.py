import MeCab

#mecab = MeCab.Tagger('-u /app/user.dic')
#mecab = MeCab.Tagger('-Ochasen') #デフォルト辞書を使う場合
mecab = MeCab.Tagger('-r /app/mecabrc')

text = '「ナチュラルハイ20周年記念作品 接客中に顔を紅潮させながら感じまくるバイト娘 真夏の看板娘中出しSP 〜海の家、ガソリンスタンド、祭りの的屋、ビアガーデン〜 総勢27人総集編付き2枚組480分 超豪華版」を動画配信で購入しましたが、ストリーミングで前半の二人分（約2時間40分）しかなく、後半の二人分及び総集編を見ることができません。ご確認お願いします。'

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
