
# 前準備
# pip install google-cloud-dlp
# pip install python-dotenv
# /.env に PROJECT_ID=XXX を設定
# サービスアカウントのキーを /gcp.json に配置
# export GOOGLE_APPLICATION_CREDENTIALS="/gcp.json"

import os
from dotenv import load_dotenv

load_dotenv('/.env')

from google.cloud import dlp_v2

client = dlp_v2.DlpServiceClient()

parent = client.project_path(os.environ.get('PROJECT_ID'))

name = 'EMAIL_ADDRESS'
info_types_elements = {'name' : name }
info_types = [info_types_elements]
inspect_config = {'info_types' : info_types}

deidentify_config = {
    'info_type_transformations': {
        'transformations': [
            {
                'primitive_transformation': {
                    'character_mask_config': {
                        'masking_character': 'x',
                        'number_to_mask': 20
                    }
                }
            }
        ]
    }
}

value = 'My email is not example@example.com , aaa@bbb.com , xxxx@xxxxx.co.jp '
items = {'value' : value }

response = client.deidentify_content(parent, deidentify_config,inspect_config, items)

print(response)
