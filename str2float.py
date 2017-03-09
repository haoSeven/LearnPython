from functools import reduce

def str2float(s):
    L = list(map(int, s.split('.')))   #str.split()分割为两部分, [123, 456]
    return reduce(lambda x, y: x+y*0.1**len(str(y)), L)   #lambda创建临时的匿名函数, x[123], y[456], 0.1**len(str(y))表示0.1的多少次方 

if __name__ == '__main__':
    help(str2float)
    print('str2float(\'123.456\') =', str2float('123.456'))
