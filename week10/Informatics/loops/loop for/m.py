a = int(input())

counter_for_cycle = 0

s1 = 0

while counter_for_cycle<a:
    b = int(input())
    if b == 0:
        s1 = s1 + 1
    counter_for_cycle = counter_for_cycle+1
print(s1)