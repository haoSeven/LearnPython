# 杨辉三角 通过generator生成list

def yhangle():
    
    L = [1]

    while True:
        yield L
        L.append(0)         #用来增加list长度
        L = [L[i - 1] + L[i] for i in range(len(L))]

if __name__ == '__main__':
    n = 0
    for t in yhangle():
        print(t)
        n = n + 1
        if n == 10:
            break
            
                
