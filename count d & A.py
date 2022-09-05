alpha,string=0,"chaitu1234"
for i in string:
    if (i.isalpha()):
        alpha+=1
print("Number of Digits is", len(string)-alpha)
print("Number of Alphabets is", alpha)
