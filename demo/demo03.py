def count_down(n):
    while n>=0:
        new = yield n
        print('new',new)
        if new:
            print('if')
            n = new
            print('n=',n)
        else:
            n -=1
cd = count_down(5)
print(cd)
for i in cd:
    print(i)
    if i==5:
        cd.send(3)