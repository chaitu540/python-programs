def check(s, t):
     
    # the sorted strings are checked
    if(sorted(s)== sorted(t)):
        print("The strings of anagrams is true.")
    else:
        print("The strings of anagrams is false.")        
         
# driver code 
s ="chaitu"
t ="chaitu"
check(s, t)
