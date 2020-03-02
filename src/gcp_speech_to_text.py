#coding:utf8

# 前準備
# pip install -r requirements.txt
# /.env に PROJECT_ID=XXX を設定
# サービスアカウントのキーを /gcp.json に配置
# export GOOGLE_APPLICATION_CREDENTIALS="/gcp.json"

import sys
from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums

filename = sys.argv[1]
bucketname = 'speech-to-text-example-ns20200302'

client = speech_v1p1beta1.SpeechClient()

language_code = 'ja-JP'
sample_rate_hertz = 8000
encoding = enums.RecognitionConfig.AudioEncoding.MULAW

config = {
    "language_code": language_code,
    "sample_rate_hertz": sample_rate_hertz,
    "encoding": encoding,
}
audio = {
    "uri": "gs://{}/{}".format(bucketname, filename)
}

operation = client.long_running_recognize(config, audio)

print('Waiting for operation to complete...')
response = operation.result(timeout=90)

for result in response.results:
    alternative = result.alternatives[0]
    print(u"Transcript: {}".format(alternative.transcript))

