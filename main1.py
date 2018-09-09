# 输入
# 输入第一行包含若干个整数，最少一个，最多100000个，中间用逗号隔开。

# 输出
# 输出包含若干个形如li-ri形式的页码段，中间用逗号隔开。


# 样例输入
# 1,2,3,1,1,2,6,6,2
# 样例输出
# 1-3,6

# Hint
# 输入样例2
# 3,2,1
# 输出样例2
# 1-3
# 输入样例3
# 30,20,10
# 输出样例3
# 10,20,30
input=raw_input()
arr=input.split(',')
temp=[]
for i in arr:
	temp.append(int(i))
temp.sort()
is_first=0
is_=0
for i in range(0,len(temp)):
    if i==0:
        print temp[i]
        is_first=1
    elif temp[i]==temp[i-1]:
        continue

    elif temp[i]==temp[i-1]+1 :
        if is_!=1:
            print "-"
            is_=1
        elif i==len(temp)-1:
        	print temp[i]
    elif is_==1 :
        print temp[i-1]
        print ','
        print temp[i]
        is_=0
        is_first=1
    else :
        print ','
        print temp[i]
