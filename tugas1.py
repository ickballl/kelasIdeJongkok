# for i in range(50):
#     i+=1
#     if i == i*3:
#         print(i,'dang')
#     elif i == 1*5:
#         print(i,'dut')
#     elif i == i*3*5:
#         print(i,'dangdut')
#     print(i)
i = 0
while i < 50:
    i += 1
    if i % 10 == 0 and i > 0:
        print('dangdut')
        continue 
    elif i % 5 == 0 and i > 0:
        print('dut')
        continue
    elif i % 3 == 0 and i > 0:
        print('dang')
        continue
    print(i)
    
