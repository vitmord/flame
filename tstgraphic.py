import matplotlib.pyplot as plt

handle = open("output_2018-08-14_15-35-35.log", "r", encoding='UTF-8')
data = list(handle.read())
print(type(data[0]))
handle.close()
print(data)
A =[]
for i in range(0,len(data)-(len(data)%4),4):
    A.append((int(data[i],16)<<12) + (int(data[i+1],16)<<8) + (int(data[i+2],16)<<4) + (int(data[i+3],16)))

print(A)

B=A

fig = plt.figure()

T=[i for i in range(len(B))]
line=plt.plot(T, B,'b,-')

plt.axis([-5.0,len(B)+5.0,-5.0,max(B)+5.0])

grid1 = plt.grid(True)   # линии вспомогательной сетки

plt.show()