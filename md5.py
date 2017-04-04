# _*_ coding:utf-8 _*_
"""
摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
"""

import hashlib


def get_md5(strings):
    md5 = hashlib.md5()
    md5.update(strings)
    return md5.hexdigest()

if __name__ == '__main__':
    print get_md5("you are very beautiful")
    print get_md5("you aoe very beautiful")
    print get_md5("you are my")

