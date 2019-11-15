# -*- coding: utf-8 -*-
import os
import re
from wox import Wox, WoxAPI
import win32con
import win32clipboard


class where(Wox):
    @classmethod
    def query(cls, queryString):
        icon = './Images/shellIcon.png'
        result = []
        pathList = os.environ['path'].split(';')

        queryStringLower = queryString.lower()
        queryList = queryStringLower.split()
        regexList = []
        for query in queryList:
            # pattern = '.*?'.join(query)
            # regexList.append(re.compile(pattern))
            regexList.append(re.compile(query))

        for pathFolder in pathList:
            if os.path.isdir(pathFolder):
                for file in os.scandir(pathFolder):
                    fileName = file.name
                    match = True
                    for regex in regexList:
                        match = regex.search(fileName.lower()) and match
                    if match:
                        filePath = os.path.join(pathFolder, fileName)
                        filePath = filePath.replace('\\', '/')
                        result.append(
                            {
                                'Title': '[' + fileName + '] ' + filePath,
                                'SubTitle': 'Press Enter key to copy path',
                                'IcoPath': icon,
                                'JsonRPCAction': {
                                    'method': 'copyData',
                                    'parameters': [filePath],
                                    "doNotHideAfterAction".replace('oNo', 'on'): False
                                }
                            }
                        )
        return result

    @classmethod
    def copyData(cls, data):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, data)
        win32clipboard.CloseClipboard()


if __name__ == '__main__':
    where()
