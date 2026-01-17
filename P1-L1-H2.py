i = 0
kelime = raw_input("bir kelime giriniz")
sesli = "aeıioöuü"
for x in kelime:
        if x in sesli:
                i +=1
        
print i	
