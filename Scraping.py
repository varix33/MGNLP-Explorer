from huggingface_hub import HfApi, get_hf_file_metadata, hf_hub_url
from huggingface_hub.hf_api import DatasetInfo

import requests
import json

# https://huggingface.co/docs/huggingface_hub/v0.21.4/en/package_reference/hf_api#huggingface_hub.HfApi.list_datasets
# https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.hf_api.DatasetInfo

# https://huggingface.co/docs/huggingface_hub/v0.21.4/en/package_reference/file_download#huggingface_hub.hf_hub_url
# https://huggingface.co/docs/huggingface_hub/v0.21.4/en/package_reference/file_download#huggingface_hub.get_hf_file_metadata


api = HfApi()
models = api.list_datasets()

for model in models:
    print(model.id)
    print(model.author)
    print(model.created_at)
    url = hf_hub_url(repo_id=model.id, filename="")
    print(url)
    print(get_hf_file_metadata(url=url))
    break
quit()
print(DatasetInfo())


quit()

API_URL = "https://datasets-server.huggingface.co/info?dataset=acronym_identification&config=default"
response = requests.get(API_URL)
data = response.json()
print(data)

import requests
API_URL = "https://datasets-server.huggingface.co/rows?dataset=rotten_tomatoes&config=default&split=train&offset=150&length=10"

response = requests.get(API_URL)

with open("answer.json", "w", encoding="utf8") as file:
    json.dump(response.json(), file, indent=2)
