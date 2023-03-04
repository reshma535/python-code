arr=[]
n=int(input("enter the size"))
for i in range(n):
          value=int(input("enter the value"))
          arr.append(value)
print("the given unsorted array")
print(arr)
small=min(arr)
large=max(arr)
print("the smallest element:")
print(small)
print("the largest element:")
print(large)
