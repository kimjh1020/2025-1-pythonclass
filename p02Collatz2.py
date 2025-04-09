# 2025.4.9 우박수프로젝트 두번째" 기본 통계랑 구하기
# numpy 배열, list 두가지 방식으로 시험
# 구하는 통계량: 평균, 중앙값, 표준편차, 최빈값, 최댓값
import numpy as np
import statistics
import time

from numpy.ma.core import append

maxnum=100

def collatz(i):
    ncount = 0
    while i != 1:
        if i % 2 == 0:
            i = i / 2

        elif i % 2 == 1:
            i = 3 * i + 1
        ncount = ncount + 1
    return ncount
#리스트방식
start = time.time()
ncountl = []
for n in range(1,maxnum):
    ncount=collatz(n)
    ncountl.append(ncount)


print(ncountl)
print(sum(ncountl)/len(ncountl))
#평균,최대값,중앙값,최빈값,표준편차
print(f'평균={statistics.mean(ncountl)}')
print(f'최대값={max(ncountl)}')
print(f'중앙값={statistics.median(ncountl)}')
print(f'최빈값={statistics.mode(ncountl)}')
print(f'표준편차={statistics.stdev(ncountl)}')

end = time.time()
print(f'{end - start: 5f} 초가 걸렸습니다')

# numpy
start = time.time()
ncounta = np.zeros(maxnum-1)
for n in range(1,maxnum):
    ncount= collatz(n)
    ncounta[n-1] = ncount





print(sum(ncountl)/len(ncountl))
#평균,최대값,중앙값,최빈값,표준편차
print(f'평균={np.mean(ncounta): 5f}')
print(f'최대값={np.max(ncounta)}')
print(f'중앙값={np.median(ncounta)}')
#print(f'최빈값={np.bincount(ncounta).argmax()}')
print(f'표준편차={np.std(ncounta)}')

end= time.time()
print(f'{end - start: 5f} 초가 걸렸습니다')




