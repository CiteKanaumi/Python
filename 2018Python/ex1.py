#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import datetime
import codecs

file = codecs.open('./post/user_id.txt', 'r', 'utf-8')
id_list = file.readlines()
file.close()

file = codecs.open('./post/user_nick.txt', 'r', 'utf-8')
nick_list = file.readlines()
file.close()

file = codecs.open('test.csv', 'w', 'utf-8')

for (id, nick) in zip(id_list, nick_list) :
    nick = nick.split('\n')
    nick = nick[0].split('\r')
    nick = nick[0]
    id = id.split('\n')
    id = id[0].split('\r')
    id = id[0]
    
    user_list = [nick, ',', id, '\n']
    print(user_list)
    file.writelines(user_list)
file.close()

