#!/usr/bin/python
#-*- conding: UTF-8 -*-
import json
def read_json():
    jsonfile = file('../key_weicarcar.json')
    s = json.load(jsonfile)
    jsonfile.close()
    return s
# print read_json()