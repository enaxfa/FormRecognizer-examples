import os
from azure.core.exceptions import ResourceNotFoundError
from azure.ai.formrecognizer import FormRecognizerClient, FormTrainingClient
from azure.core.credentials import AzureKeyCredential


# use your `key` and `endpoint` environment variables
key = os.environ.get('FR_KEY')
endpoint = os.environ.get('FR_ENDPOINT')


"""
Analyze a Form Table
"""

form_url = 'https://cdn.vertex42.com/ExcelTemplates/Images/excel-invoice-template.png'

form_recognizer_client = FormRecognizerClient(endpoint = endpoint, credential = AzureKeyCredential(key))

poller = form_recognizer_client.begin_recognize_content_from_url(form_url)


form_result = poller.result()

print(form_result)


page = form_result[0]
vars(page)
len(page.tables)

for page in form_result:
    for table in page.tables:
        print('Column Count: {0}'.format(table.column_count))
        print('Row Count: {0}'.format(table.row_count))
        for cell in table.cells:
            print('Cel value: {0}'.format(cell.text))
            print('Location: {0}'.format(cell.bounding_box))
            print('Confidence Score: {0}'.format(cell.confidence))

