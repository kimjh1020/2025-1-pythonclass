  # 2025.3.12
  # 파이썬 수업 - 변수,타입,출력
  # 타입 (형) 정수 : int (integer)
  #          실수 : float (floating point)
  #          문자열 : str (string)
  #          논리값: bool (boolean)

title = "시간 계산"
sec = 3700
min = sec/60
bigger = min > sec
print(sec,min,bigger)
print(type(title), type(sec), type(min), type(bigger))

a = int(10.9) #floor 버림 ceiling 올림 round 반올림
b= float(10.3)
c= str(10.3)
print(type(a), type(b), type(c))
print(a)

sec1 = 3100; sec2 = 120
seca = sec1 + sec2
secs = sec1 - sec2
secm = sec1 * sec2
secd = sec1 / sec2
secq = sec1 // sec2
secr = sec1 % sec2
print(f'{seca=},{secs=},{secm=},{secd=},{secq=},{secr=}') #f string

# 화씨를 섭씨로 바꿈
# tc = (tf - 32) * 5/9
# tf = (tc * 9/5) +32
tf = 100

tc = (tf -32) * 5/9
print(f'{tf=} ===> {tc=}')
tc = 37.77777777777778
tf = (tc * 9/5) +32

print(f'{tc=} ===> {tf=}')

print(2 ** 3,2 ** (1/2))
# 사칙 연산 중에서 0으로 나누는 것은 허용 하지 않음
# print(3/0)
a = True
print(type(a))

a='3'
b=float(a)
print(b**int(a))

a = '3.5 '
b = 4
print(a * b)