
# 前準備
# pip install -r requirements.txt
# aws configureで接続設定をする
# もしくは aws.config, aws.credentials に記載する

import boto3
import json

def main():
    text = '「ナチュラルハイ20周年記念作品 接客中に顔を紅潮させながら感じまくるバイト娘 真夏の看板娘中出しSP 〜海の家、ガソリンスタンド、祭りの的屋、ビアガーデン〜 総勢27人総集編付き2枚組480分 超豪華版」を動画配信で購入しましたが、ストリーミングで前半の二人分（約2時間40分）しかなく、後半の二人分及び総集編を見ることができません。ご確認お願いします。'
    #text = '斎藤です、購入した商品が欠陥だらけで使い物にならない、返品したいんだけど'
    lang = 'ja'

    comprehend = boto3.client('comprehend', region_name='us-west-2')

    result = comprehend.detect_dominant_language(Text=text)
    print('Detect Domainant Language.')
    print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))

    result = comprehend.detect_entities(Text=text, LanguageCode=lang)
    print('Detect Entities.')
    print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))

    result = comprehend.detect_key_phrases(Text=text, LanguageCode=lang)
    print('Detect Key Phrases.')
    print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))

    result = comprehend.detect_sentiment(Text=text, LanguageCode=lang)
    print('Detect Sentiment.')
    print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))

if __name__ == '__main__' :
    main()
