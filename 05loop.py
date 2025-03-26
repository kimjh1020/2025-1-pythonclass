#2025.3.26 2학년 1학기 파이썬 수업
#순환문 (반복문) : loop

for i in range(10):
    print(f'{i=}')

for j in range(1,10,3):
    print(f'{j=}')

for looper in [1,2,3,4,5,'끝']:
    print(f'{looper=}')

cities = ['서울','부산','인천','의정부','대전','강릉','논산','포항']
for city in cities:
    print(f'{city=}')

string = 'python'
for c in string:
    print(f'{c=}')