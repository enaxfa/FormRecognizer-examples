import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential


# use your `key` and `endpoint` environment variables
key = os.environ.get('FR_KEY')
endpoint = os.environ.get('FR_ENDPOINT')
form_recognizer_client = FormRecognizerClient(endpoint = endpoint, credential = AzureKeyCredential(key))


"""
Analyze a Receipe 
"""
path_to_sample_forms = r'C:\Users\enaf\Pictures\walmart.jpg'

with open(path_to_sample_forms, "rb") as f:
       poller = form_recognizer_client.begin_recognize_receipts(receipt=f, locale="en-US")

receipts = poller.result()
print(receipts)

for receipt in receipts:
       for name, field in receipt.fields.items():
              print(name, field)
              print("\n")


