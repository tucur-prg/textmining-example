import spacy
from spacy import displacy

nlp = spacy.load('ja_ginza')

#text = '「ナチュラルハイ20周年記念作品 接客中に顔を紅潮させながら感じまくるバイト娘 真夏の看板娘中出しSP 〜海の家、ガソリンスタンド、祭りの的屋、ビアガーデン〜 総勢27人総集編付き2枚組480分 超豪華版」を動画配信で購入しましたが、ストリーミングで前半の二人分（約2時間40分）しかなく、後半の二人分及び総集編を見ることができません。ご確認お願いします。'
text = 'AI Shiftの杉山です。会社の住所は〒150-6122 東京都渋谷区渋谷渋谷スクランブルスクエアで、2019/12/18生まれです。'

doc = nlp(text)

for sent in doc.sents:
    print(sent)

    for token in sent:
        info = [
            token.i,         # トークン番号
            token.orth_,     # テキスト
            token._.reading, # 読みカナ
            token.lemma_,    # 基本形
            token.pos_,      # 品詞
            token.tag_,      # 品詞詳細
            token._.inf      # 活用情報
        ]
        print(info)

#displacy.render(doc, style="ent")
