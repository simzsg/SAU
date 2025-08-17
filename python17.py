# คำสั่ง  if-elif


score = int(input('กรุณากรอกคะแนนของคุณ : '))
print('------------------------')

if score >= 80 :
    print('A')
elif score >= 70 :
    print('B')
elif score >= 60 :
    print('C')
elif score >= 50 :
    print('D')
else :
    print('F')

print('จบโปรแกรม')