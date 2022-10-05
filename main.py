# ----------------------------------------------------------------
# Author: wayneferdon wayneferdon@hotmail.com
# Date: 2022-02-12 06:25:55
# LastEditors: wayneferdon wayneferdon@hotmail.com
# LastEditTime: 2022-10-05 18:17:19
# FilePath: \Wox.Plugin.Where\main.py
# ----------------------------------------------------------------
# Copyright (c) 2022 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

# -*- coding: utf-8 -*-
import os
from RegexList import *
from WoxQuery import *

class Where(WoxQuery):
    def query(self, queryString):
        pathList = os.environ['path'].split(';')
        regex = RegexList(queryString)
        icon = './Images/shellIcon.png'
        subTitle = 'Press Enter key to copy path'
        results = list()

        for pathFolder in pathList:
            if not os.path.isdir(pathFolder):
                continue
            for file in os.scandir(pathFolder):
                fileName = file.name
                if not regex.match(fileName):
                    continue
                filePath = os.path.join(pathFolder, fileName)
                filePath = filePath.replace('\\', '/')
                title = '[ ' + fileName + ' ] ' + filePath
                results.append(WoxResult(title,subTitle,icon,None,self.copyData.__name__,True,filePath).toDict())
        return results

if __name__ == '__main__':
    Where()
