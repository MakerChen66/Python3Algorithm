'''
！usr/bin/env python3
- * - encoding=utf-8 - * -
@author     :  makerchen
@time       :  2019-5-9
@IDE        :  PyCharm/Sublime Text
@微信公众号 ：小鸿星空科技
- * - encoding=utf-8 - * -
'''


def permute(value):
    values = list(value)
    n = len(values)

    # i: 找到递减序列前的那一个支点
    for i in reversed(range(n - 1)):
        if values[i] < values[i + 1]:
            break
    else:
        # 否则逆转列表里的元素
        values[:] = reversed(values[:])
        return values

    # j: 要和i支点交换值的递减序列的次小项
    for j in reversed(range(i, n)):
        if values[i] < values[j]:
            # i支点和递减序列的次小项交换值，并且把交换后的递减序列逆转，也就是把i支点后的元素逆转
            values[i], values[j] = values[j], values[i]
            values[i + 1:] = reversed(values[i + 1:])
            break

    print(values)

permute('HIJT')
