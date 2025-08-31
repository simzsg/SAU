# สร้างโปรแกรมเครื่องคำนวณของตัวเลข 2 จำนวน
# ที่รับทางแป้นพิมพ์ ได้แก่ บวก ลบ คูณ หาร โดยทำเป็นเมนูให้ผู้ใช้เลือก
#  ผู้ใช้เลือกเมนูไหนให้คำนวณตามเมนูนั้นๆ แล้วเสดงผลลัพธ์

def Headname():
    print('+++++++++++++++++++++++++++++++++')
    print('           เครื่องคิดเลข            ')
    print('+++++++++++++++++++++++++++++++++')

def showMenu():
    print('1. บวก')
    print('2. ลบ')
    print('3. คูณ')
    print('4. หาร')
    menu = int(input('กรุณาเลือกเมนู : '))
    return menu

def inputNumber():
    num1 = int(input('ป้อนตัวเลขที่ 1 : '))
    num2 = int(input('ป้อนตัวเลขที่ 2 : '))
    return num1, num2

def sumdit(num1, num2):
    return num1 + num2

def subdit(num1, num2):
    return num1 - num2

def muldit(num1, num2):
    return num1 * num2

def divdit(num1, num2):
    if num2 == 0:
        return "ไม่สามารถหารด้วยศูนย์ได้"
    return num1 / num2

def showResult(menu, num1, num2):
    if menu == 1:
        print(f'ผลบวกของ {num1} และ {num2} คือ {sumdit(num1, num2)}')
    elif menu == 2:
        print(f'ผลลบของ {num1} และ {num2} คือ {subdit(num1, num2)}')
    elif menu == 3:
        print(f'ผลคูณของ {num1} และ {num2} คือ {muldit(num1, num2)}')
    elif menu == 4:
        print(f'ผลหารของ {num1} และ {num2} คือ {divdit(num1, num2)}')
    else:
        print("เมนูไม่ถูกต้อง")


Headname()
menu = showMenu()
num1, num2 = inputNumber()
showResult(menu, num1, num2)
