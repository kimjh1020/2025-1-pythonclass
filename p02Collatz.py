# 2025.4.2 파이썬수업 프로젝트 두번째
# 콜라츠 추측, 또는 우박수
# 1부터 1000까지 숫자중, 가장많은 단계를 거처서 1로가는수는 무엇인가?, 가장많은 단계는 몇단계인가
# 규칙: n이 짝수 -> n/2
#      n이 홀수 -> 3*n+1
#  예: 5 -> 16 ->8 ->4 ->2 ->1 (5단계)



n = int(input("숫자를 입력하세요: "))
if n % 2 == 0:
    print('짝수')
else:
    print("홀수")
l = 0


while n != 1 :
    if n % 2 == 0:
        n = n / 2
        print(n)
        l = l + 1
    elif n % 2 == 1:
        n = 3 * n + 1
        print(n)
        l = l + 1
    else:
        break

print(l,'단계')




