#coding=utf-8
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from app.google.google_sharesheet.google_sharesheet import SpreadsheetSnippets
from base.small_tool import stool
from loguru import logger

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['bug_conf']['google_spreadsheet_id']
SAMPLE_RANGE_NAME = stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['bug_conf']['google_bug_range']

class SaveDataToSheet(object):

    def __init__(self):
        # 链接上google,获取服务句柄
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    @logger.catch()
    def save_bug(self, value):
        ss = SpreadsheetSnippets(self.service)
        ss.append_values(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, 'RAW', value)
        logger.info(
            '保存缺陷到google成功,保存的数据是:\n' + str(value))
        print(
            '保存缺陷到google成功,保存的数据是:\n' + str(value))
        logger.info('保存缺陷到google成功,保存的地址是:\n' + stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['bug_conf']['google_bug_url'])
        print(
            '保存缺陷到google成功,保存的地址是:\n' + stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['bug_conf']['google_bug_url'])

    def get_values(self):
        service = self.service
        # [START sheets_get_values]
        result = service.spreadsheets().values().get(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=stool.get_config_dict_yaml['WINDOW']['WINDOW_DATA']['bug_conf']['bug_title_range']).execute()
        rows = result.get('values', [])
        # print('{0} rows retrieved.'.format(len(rows)))
        # [END sheets_get_values]
        return result

    def updata_bug_id(self, bug_title_data_list, compare_data, bug_id):
        bug_id_locate = None
        for i in range(len(bug_title_data_list)):
            if bug_title_data_list[i][0] == compare_data:
                bug_id_locate = 'bug!A%d' % (i+1)

        service = self.service
        # [START sheets_update_values]
        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        # [START_EXCLUDE silent]
        values = [[bug_id]]
        # [END_EXCLUDE]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=bug_id_locate,
            valueInputOption='RAW', body=body).execute()
        # print('{0} cells updated.'.format(result.get('updatedCells')))
        logger.info('更新成功,ID为:' + bug_id)
        print('更新成功,ID为:' + bug_id)
        # [END sheets_update_values]
        return result

    def updata_bug_url(self, bug_title_data_list, compare_data, bug_url):
        bug_id_locate = None
        for i in range(len(bug_title_data_list)):
            if bug_title_data_list[i][0] == compare_data:
                bug_id_locate = 'bug!L%d' % (i+1)

        service = self.service
        # [START sheets_update_values]
        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        # [START_EXCLUDE silent]
        values = [[bug_url]]
        # [END_EXCLUDE]
        body = {
            'values': values
        }
        result = service.spreadsheets().values().update(
            spreadsheetId=SAMPLE_SPREADSHEET_ID, range=bug_id_locate,
            valueInputOption='RAW', body=body).execute()
        # print('{0} cells updated.'.format(result.get('updatedCells')))
        logger.info('更新成功,url为:' + bug_url)
        print('更新成功,url为:' + bug_url)
        # [END sheets_update_values]
        return result


# savedatatosheet = SaveDataToSheet()

# if __name__ == '__main__':
    # print(SAMPLE_SPREADSHEET_ID)
    # data = SaveDataToSheet().updata_bug_id(SAMPLE_SPREADSHEET_ID, 'bug!A4', 'RAW', [['123']])
    # print(data, data['values'])