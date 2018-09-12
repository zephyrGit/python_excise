# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 14:27
@author : Zephyr
@file   : 07future.py
'''

from concurrent.futures import ThreadPoolExecutor
import time


# futures可以实现多核

def doSth(args):
    time.sleep(1)
    print("****", args)


if __name__ == '__main__':

    pool = ThreadPoolExecutor(3)

    list = [1, 2, 3, 4, 5, 6]
    with pool:
        # fn, *iterables 可迭代对象
        pool.map(doSth, list)  # map 是有的

    with ThreadPoolExecutor(2) as exe:
        '''
         fn, 方法 
         *args,  实参
        '''
        for i in list:
            exe.submit(doSth, i)  # submit是无序的
