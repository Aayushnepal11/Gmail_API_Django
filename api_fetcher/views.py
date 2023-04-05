from django.shortcuts import render, HttpResponse
from .gmail_api import GmailAPI

GMAIL_DATA = GmailAPI()

INBOX_DATA = GMAIL_DATA.data_getter("me", 5, "inbox")
SPAM_DATA = GMAIL_DATA.data_getter("me", 10, "spam")
DRAFT_DATA = GMAIL_DATA.data_getter("me", 5, "draft")

INBOX_DATA_LENGTH = len(INBOX_DATA)
SPAM_DATA_LENGTH = len(SPAM_DATA)
DRAFT_DATA_LENGTH = len(DRAFT_DATA)

length_list = [INBOX_DATA_LENGTH, SPAM_DATA_LENGTH, DRAFT_DATA]

def data_fetcher(data):
    data_list = list()
    for headers in data:
        data_dict = dict()
        for header in headers:
            if header['name'] == 'Date':
                date = header['value']
                data_dict[header['name']] = date
            if header['name'] == 'From':
                sender = header['value']
                data_dict[header['name']] = sender
            if header['name'] == 'Subject':
                if not header['value']:
                    subject = "No related subject."
                else:
                    subject = header['value']
                data_dict[header['name']] = subject
        data_list.append(data_dict)
        sorted(data_list[0].get("Date"))
    return data_list


def index(request):
    context = {
        'title': 'Spam_Checker/Inbox',
        'mail_box_data': length_list,
        'fetch_data': data_fetcher(INBOX_DATA),
    }
    return render(request, 'gmail_api/index.html', context)


def spam(request):
    context = {
        'title': 'Spam_Checker/Spam',
        'mail_box_data': length_list,
        'fetch_data': data_fetcher(SPAM_DATA)
    }
    return render(request, 'gmail_api/spam.html', context)


def draft(request):
    pass
