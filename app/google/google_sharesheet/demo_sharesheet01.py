#coding=utf-8

# from biz.chandao import chandao_bug_write_page,chandao_login_page
#
# a = chandao_login_page.ChandaoLoginPage()
#
# b = chandao_bug_write_page.ChandaoBugWritePage()
#
# a.open_login_url()
# a.login('dajun', 'Dajun123')
# b.open_bug_cat_url()
# b.product_chosen()


from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bot.google.google_sharesheet import SpreadsheetSnippets

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '19iHCdYgDuijyjvqH067HYpXwd9lR7rwpGICNj4xpxFE'
SAMPLE_RANGE_NAME = u'工作表1!B1:C'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    #If there are no (valid) credentials available, let the user log in.
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

    service = build('sheets', 'v4', credentials=creds)

    ss = SpreadsheetSnippets(service)

    print(ss.append_values(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, 'RAW', [['t'], [123], ['ojge']]))
    print(ss.get_values(SAMPLE_SPREADSHEET_ID, u'工作表1'))


if __name__ == '__main__':
    main()