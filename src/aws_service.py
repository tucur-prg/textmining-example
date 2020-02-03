
# 前準備
# pip install -r requirements.txt
# aws configureで接続設定をする
# もしくは aws.config, aws.credentials に記載する

import boto3
import json

def main():
    #text = '私は、お腹が空いたので、カレーを食べました。'
    text = '斎藤です、購入した商品が欠陥だらけで使い物にならない、返品したいんだけど'
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
