# 2025.3.19
# 파이썬 수업, 조건문

grade= "아직모름"
score = int(input("점수를 입력하세요:"))
if 100 >= score > 60:
    grade = "합격"
else:
    if 60>= score >= 50:
        grade="임시합격"
    if score < 50:
        grade = "불합격"

print(grade)

if score >=90:
    grade = 'A'
elif score >=80:
    grade = 'B'
elif score >=70:
    grade = 'C'
elif score >=60:
    grade = 'D'
else:
    if score < 60:
        grade = 'F'
print(grade)



