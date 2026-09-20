class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        index=0
        l=len(s)
        while index<l and s[index]==" ":
            index+=1
        sign=1
        if index<l:
            if s[index]=="-":
                index+=1
                sign=-1
            elif s[index-1]=="+":
                sign=1
                index+=1
        s=s[index:]
        def parse(i,num):
            if i==len(s) or not s[i].isdigit():
                return num
            digit=int(s[i])
            new_num=num*10+digit
            return parse(i+1,new_num)
        num=parse(0,0)
        if sign==-1:
            num=num*sign
        if num>2**31-1:
            return 2**31-1
        if num<-2**31:
            return -2**31
        return num
S=Solution()
print(S.myAtoi("123-"))
