integer1 = input()
integer2 = input()
integer1 = int(integer1)
integer2 = int(integer2)
result = 0
if integer1 > 0:
    result = (integer1*integer2)
else:
    result = (-integer1*integer2%109)
    result = 109 - result

print(result % 109)