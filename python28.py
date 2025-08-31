# ค่าที่ return มีค่าได้มากกว่าหนึ่งค่า

def sumdit(a, b, c):
    print(f"a = {a}, b = {b}, c = {c}")
    return a * 10 , b * 20 ,c * 30


sum1 , sum2 , sum3 = sumdit(1,2,3)
print(sum1)
print(sum2)
print(sum3)


