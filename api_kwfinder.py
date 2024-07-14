import pandas as pd
import requests
import hmac
import hashlib
import base64
import time
import random
import urllib.parse
import json
from data_convertor import json_to_spreadsheet


class HumanService:
    api_key = "put yors"

    @staticmethod
    def gets():
        a = 'yIHdas83xd2do9obDAS8FNX'
        b = '4lBdsNANmdsaQ6321DWVb'
        return a + b + 'daspC5eUosr3t1fMBH50'

    @staticmethod
    def getu():
        uuid = []
        for ii in range(32):
            if ii in [8, 20]:
                uuid.append('-')
                uuid.append(format(random.randint(0, 15), 'x'))
            elif ii == 12:
                uuid.append('-')
                uuid.append('4')
            elif ii == 16:
                uuid.append('-')
                uuid.append(format(random.randint(8, 11), 'x'))
            else:
                uuid.append(format(random.randint(0, 15), 'x'))
        return ''.join(uuid)

    @staticmethod
    def gen():
        svalue = HumanService.gets()
        rvalue = HumanService.getu()

        hmac_result = hmac.new(
            svalue.encode(), rvalue.encode(), hashlib.sha1).digest()
        hvalue = base64.b64encode(hmac_result).decode('utf-8')

        return f"{rvalue}::{hvalue}"

    @staticmethod
    def utf8_to_urlencode(utf8_string):
        """
        Convert a UTF-8 string to URL-encoded format.

        Args:
            utf8_string (str): The UTF-8 string to convert.

        Returns:
            str: The URL-encoded string.
        """
        return urllib.parse.quote(utf8_string)


# Example usage
human_service = HumanService()
# print(human_service.gen())


def req_func(query):

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"ba75-czk3SRSPeoGA8DfLWXcPhA"',
        'Origin': 'https://app.mangools.com',
        'Referer': f'https://app.mangools.com/kwfinder/dashboard?language_id=1064&location_id=0&query={human_service.utf8_to_urlencode(query)}&source_id=0&sub_source_id=0',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-Access-Token': human_service.api_key,
        'X-Human-Token': human_service.gen(),
        'X-Mangools-Client': 'app',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    params = {
        'kw': query,
        'language_id': '1064',
        'location_id': '0',
    }

    response = requests.get(
        'https://api.mangools.com/v3/kwfinder/related-keywords', params=params, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(response)
        return None


def iter_keywords(excel_file, keyword_column_name='Keyword'):
    # Load the Excel file
    df = pd.read_excel(excel_file)

    # Check if the keyword column exists
    if keyword_column_name not in df.columns:
        raise ValueError(
            f"Column '{keyword_column_name}' does not exist in the spreadsheet.")

    # Iterate over each keyword and print it
    for keyword in df[keyword_column_name]:
        print(keyword)
        time.sleep(5)
        data = req_func(keyword)
        with open(f'json/data-{keyword}.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False)

        json_to_spreadsheet(
            f'json/data-{keyword}.json', f'out/data-{keyword}.xlsx')


name = "قیمت آهن آلات"
data = req_func(name)
with open(f'json/data-{name}.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)

json_to_spreadsheet(f'json/data-{name}.json', f'out/data-{name}.xlsx')


# Path to the Excel file
excel_file = f'out/data-{name}.xlsx'

# Print the keywords
iter_keywords(excel_file)
