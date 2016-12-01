#!/usr/bin/env python

from __future__ import print_function
import os

import httplib2
from googleapiclient import discovery
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from textsumm import textsummarization

def getsharelink(flacfile,textfile):
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    SCOPES = 'https://www.googleapis.com/auth/drive.file'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store, flags) \
                if flags else tools.run(flow, store)
    DRIVE = build('drive', 'v2', http=creds.authorize(Http()))

    FILES = [

        ('testflac1.flac', True)
    ]

    for filename, convert in FILES:
        metadata = {'title': filename,'role':'reader', 'type':'anyone'}
        res = DRIVE.files().insert(convert=convert, body=metadata,
                media_body=filename, fields='mimeType,exportLinks,webContentLink').execute()

        if res:
            print('Uploaded "%s" (%s)' % (filename, res['mimeType']))
            print(res['webContentLink'])
        textsumm.textsummarization(textfile,res['webContentLink'])


