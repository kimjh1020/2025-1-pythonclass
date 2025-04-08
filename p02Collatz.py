# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중, 가장많은 단계를 거처서 1로가는수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3*n+1
#  예: 5 -> 16 ->8 ->4 ->2 ->1 (5단계)


maxvalue = 0
maxvaluen = 0
values = []
n = 0
if n % 2 == 0:
    print('짝수')
else:
    print("홀수")
l = 0
for n in range(1,100):
    print('n=',f'{n}')
    l=0
    nsave =n
    while n != 1 :
        if n % 2 == 0:
            n = n / 2
            l = l + 1
        elif n % 2 == 1:
            n = 3 * n + 1
            l = l + 1
        else:
            break
    values.append(l)
    print(l, '단계')
    #가장 많은 단계를 가진 수 구하기
    if maxvalue < l:
        maxvalue = l
        maxvaluen = nsave




print(f'{maxvalue=},{maxvaluen=}')
print(values)
values.sort(reverse=True)
print('2ndvalue=',values[1],'2ndvaluen')





