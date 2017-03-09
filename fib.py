#斐波拉契数列Python实现算法


def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

if __name__ == '__main__':
    for i in fib(10):
        print(i)
