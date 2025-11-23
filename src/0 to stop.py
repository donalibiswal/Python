

nums=[]
while True:
        num=int(input("enter the number and '0' to stop:"))
        if num==0:
             break
        nums.append(num)
def calculate (nums):
        sum=0
        for num in nums:
                cube=num*num*num
                sum=sum+cube
        print("summ:",sum)
calculate(nums)
