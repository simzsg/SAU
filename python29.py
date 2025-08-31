# เขียนโปรแกรมคำนวณพื้นที่วงกลมและเส้นรอบวงกลม
# โดยรับค่ารัศมีทางแป้นพิมพ์ 
# แสดงผลพื้นที่
# แสดงเส้นรอบวงกลมที่คำนวณได้ทางหน้าจอ

def circle_area(radius):
    area = 3.1416 * radius * radius
    circumference = 2 * 3.1416 * radius
    return area, circumference


def headName():
    print('+++++++++++++++++++++++++++++++++')
    print('โปรแกรมหาพื้นที่วงกลมและเส้นรอบวงกลม')
    print('+++++++++++++++++++++++++++++++++')

headName()
radius = float(input('ป้อนรัศมี: '))
area, circumference = circle_area(radius)

print('---------------------------------')
print(f'รัศมี {radius:,.2f} ')
print(f'มีพื้นที่ {area:,.2f} ')
print(f'เส้นรอบวงกลม {circumference:,.2f}')
print('---------------------------------') 