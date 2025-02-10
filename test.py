# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass
# # you need to guess this number
# number = 18
# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

### anagrams
a = ["act","god", "cat", "dog", "tac"]
seen={}
for x in a:
    s = "".join(sorted(x))
    if s in seen:
        seen[s].append(x)
    else:
        seen[s]=[x]
print(seen)

### two sum
a=[2,5,4]
tar=6
se={}
for i,x in enumerate(a):
    rem = tar-x
    if rem in se:
        print(se[rem],i)
    else:
        se[x]=i


### reverse

a =123
ans=0
while a:
    ans = ans*10+a%10
    a//=10
print(ans)