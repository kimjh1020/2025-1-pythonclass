# 오일러 공식을 이용한 파이 근사값 구하기

#기본계산
n = 1
pi = 1
pi = pi* ((2 * n + 1) ** 2 - 1) / (2 * n + 1) ** 2
n=2
pi = pi* ((2 * n + 1) ** 2 - 1) / (2 * n + 1) ** 2



print(pi*4)

#루프로 변환
n=1
pi= 1
while n< 100:
    pi = pi * ((2 * n + 1) ** 2 - 1) / (2 * n + 1) ** 2
    n=n+1
print(pi*4)

import matplotlib.pyplot as plt
plt.plot([1,3,4])
plt.show()

