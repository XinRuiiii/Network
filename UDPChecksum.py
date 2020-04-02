# -*- coding: utf-8 -*-
# @Time    : 2020/4
# @Author  : 张心蕊
# @Site    :
# @File    : UDPChecksum+.py
# @Description  : 计算UDP16位校验和


def checksum(numbers):
    result = 0
    # 计算校验和
    for number in numbers:
        result = add(result, number)
    return format(result ^ 0b1111111111111111, '016b')


def add(result, num):
    # 直接相加
    result = result + num
    # 判断是否超过16位
    if result & 0b11111111111111110000000000000000:
        # 若超过则回卷至在16位之内
        result = add(result % 0b10000000000000000, result // 0b10000000000000000)
    return result


print("校验和："+ checksum([0b0110011001100000, 0b0101010101010101, 0b1000111100001100]))
