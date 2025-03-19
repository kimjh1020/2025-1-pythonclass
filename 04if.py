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
if 90 >score >=80:
    grade = 'B'
if 80 >score >=70:
    grade = 'C'
else:
    if score < 70:
        grade = 'F'
print(grade)

