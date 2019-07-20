# -*- coding: utf-8 -*-

# @Author  : Jeffssss
# @Time    : 2019-07-20

import time
import os
#ios相关的包
import wda
import sys
reload(sys)
sys.setdefaultencoding('utf8')

c = wda.Client()
s = c.session()

estimatedCount = 50

def game_fun():
    count = 1
    while True:
        time.sleep(5)
        print('--------------------will trigger video, count=' + str(count))
        s.tap(180,420)
        print('sleep begin')
        time.sleep(35)
        print('sleep end, will close video')
        s.tap(330,40)
        print('finish once')
        count = count + 1
        if count > estimatedCount:
            break


if __name__ == '__main__':
    game_fun()
    