'''
！usr/bin/env python3
- * - encoding=utf-8 - * -
author     :  makerchen
time       :  2019-5-8
IDE        :  PyCharm/Sublime Text
微信公众号 ：小鸿星空科技
- * - encoding=utf-8 - * -
'''


def mult(chain):
    n = len(chain)
    aux = {(i, i): (0,) + chain[i] for i in range(n)}
    # i: 子链的长度
    for i in range(1, n):
        # j: 子链开始的索引
        for j in range(0, n - i):
            best = float('inf')
            # k: 子链的分割点
            for k in range(j, j + i):
                # 分割点的多个子链
                lcost, lname, lrow, lcol = aux[j, k]
                rcost, rname, rrow, rcol = aux[k + 1, j + i]
                cost = lcost + rcost + lrow * lcol * rcol
                var = '(%s%s)' % (lname, rname)
                # 选择最优解
                if cost < best:
                    best = cost
                    aux[j, j + i] = cost, var, lrow, rcol
    matrixchain =  dict(zip(['cost', 'order', 'rows', 'cols'], aux[0, n - 1]))
    print(matrixchain)

mult([('A', 10, 20), ('B', 20, 30), ('C', 30, 40)])