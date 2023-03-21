#형변환 실습
a = 3.
b = 6
c = .7
d = 12.7

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print()
print(float(b))
print(int(c))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))

#수치 연산 함수
print(abs(-7))
x, y = divmod(100,8)
print(x,y)
print(pow(5,3), 5**3)

#외부 모듈
import math

print(math.pi)
print(math.ceil(5.1)) # 값 이상의 수에서 가장 작은 정수
