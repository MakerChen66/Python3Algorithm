'''
！usr/bin/env python3
- * - encoding=utf-8 - * -
@author     :  makerchen
@time       :  2019-5-9
@IDE        :  PyCharm/Sublime Text
@微信公众号 ：小鸿星空科技
- * - encoding=utf-8 - * -
'''


math = {
  '+': float.__add__,
  '-': float.__sub__,
  '*': float.__mul__,
  '/': float.__truediv__,
  '^': float.__pow__,
}
def postfix(expression):
	stack = []

	for x in expression.split():
		if x in math:
			x = math[x](stack.pop(-2), stack.pop(-1))
		else:
			x = float(x)
		stack.append(x)

	print(stack.pop())

postfix('1 2 + 4 3 - + 10 5 / *')  # 相当于计算 ((1+2)+(4-3))*(10/5)