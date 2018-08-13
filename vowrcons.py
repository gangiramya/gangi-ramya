str1=(input(""))
if str1 in ('a','e','i','o','u,'A','E','I','O','U'):
    print("vowel")
elif((str1>='a' and str1<='z') or (str1='A' and str1='Z')):
    print("consonent")
else:
print("invalid")
