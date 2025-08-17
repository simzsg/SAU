# break and continue ใน loop
# break ใน loop ทำงานเมื่อเจอเงื่อนไข แล้วหยุดการทำงานทันที
# continue ใน loop ทำงานเมื่อเจอเงื่อนไข แล้วไม่ทำงานต่อ


for a in range(1,11):
    if a == 5:
        break
    print(a)

print('------------------------')

for b in range(1,11):
    if b == 5:
        continue
    print(b)