print(bin(-1))
print((bin(-1))[2:].count('1'))


tmp=1
count=0
for i in range(32):

    count+=tmp&1
    tmp>>1
print(count)