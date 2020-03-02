
# 前準備
# pip install -r requirements.txt
# aws configureで接続設定をする
# もしくは aws.config, aws.credentials に記載する

import boto3
import time

def main():
    client = boto3.client('transcribe')

    client.start_transcription_job(
        TranscriptionJobName='Example_{}'.format(time.time()),
        Media={
            'MediaFileUri': 'https://s3.amazonaws.com/transcribe-example-ns20200220/0003.wav',
        },
        MediaFormat='wav',
#        MediaSampleRateHertz=44100,
        LanguageCode='ja-JP',
        Settings={
            'ShowSpeakerLabels': True,
            'MaxSpeakerLabels': 2,
#            'ShowAlternatives': True,
#            'MaxAlternatives': 2
#            'VocabularyName': 'aws',
        }
    )

if __name__ == '__main__' :
    main()
