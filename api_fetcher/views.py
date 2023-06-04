from django.shortcuts import render
from .gmail_api import GmailAPI
from django.contrib import messages


GMAIL_DATA = GmailAPI()

INBOX_DATA = GMAIL_DATA.data_getter("me", 100, "inbox")
SPAM_DATA = GMAIL_DATA.data_getter("me", 50, "spam")


INBOX_DATA_LENGTH = len(INBOX_DATA)
SPAM_DATA_LENGTH = len(SPAM_DATA)


def data_fetcher(data):
    data_list = list()
    for headers in data:
        data_dict = dict()
        for header in headers:
            if header['name'] == 'Date':
                date = header["value"]
                data_dict[header["name"]] = date
            if header['name'] == 'From':
                sender = header["value"]
                data_dict[header["name"]] = sender
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
        'title': 'Spam Checker:Home',
        'inbox_count': INBOX_DATA_LENGTH,
        'spam_count': SPAM_DATA_LENGTH,
        }
    return render(request, 'gmail_api/index.html', context)



def inbox(request):
    if INBOX_DATA_LENGTH == 0:
        messages.info(request, "You don't have anything on your inbox.")

    context = {
        'title': 'Spam_Checker/Inbox',
        'fetch_data': data_fetcher(INBOX_DATA),
    }
    return render(request, 'gmail_api/inbox.html', context)


def spam(request):
    if SPAM_DATA_LENGTH == 0:
        messages.info(request, "You don't have anything on your spam.")
    context = {
        'title': 'Spam_Checker/Spam',
        'fetch_data': data_fetcher(SPAM_DATA)
    }
    return render(request, 'gmail_api/spam.html', context)


