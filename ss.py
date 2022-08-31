#string and slicing

str =  "chintan patel instrumentation and control engineer"


print(len(str))
print(str[0:])   #print all the character
print(str[:6])   #consider 0 automatically means print only 0 to 6 characters
print(str[:])    #(consider full length)print all the characters


print(str[5])       #index start on 0
print(str[0:50])    #slicing rule excluding last num
print(str[60])     #show the error
print(str[0:60])   #do not show the error
print(str[0:7:2])   #skip the character


#positive index

print(str[::])          #consider skip 1 num
print(str[1:50:1])     #both are same
print(str[::555])      #extend slicing or advance python slicing



#negative index

print(str[-1:])     #negative index starts on a last character or letter
print(str[49])      #both are same
print(str[::-1])    #printing in reverse order



#function of strings
print(str.isalnum())                    #alpha-numeric function (true/false) 
print(str.isalpha())                    #there is no alpha funtion
print(str.endswith("engineer"))         #end charachter
print(str.count("e"))                   #count function
print(str.capitalize())                 #capitalize first charater of the string
print(str.find("and"))                  #give the index num when 'and' starts
print(str.lower())                      #all character in small letter
print(str.upper())                      #all character in upper letter
print(str.replace("and", "&"))          #replace with 'and' to '&'
print(str.casefold())   #lower case
print(str.center())
print(str.encode()) 
print(str.expandtabs())
print(str.format())



#lists and functions



a = [10, 25, 30, 55, 45]

print(a[:4])    #print index o to 4 
print(a[3])   #only print index num 3 digit
a.sort()   #sequence form
a.reverse()  #reverse form
print(a[3:4])
print(a[0:5:2])    #extended slice
print(a[::-1])    #nagetive slicing do not metion -2 or -3 etc. only metion -1 others not work in slicing


#funtion in list

a.append(50)    #add num in last
a.append(50)   #you can add same num in multiple time
print(a)
a.insert(1, 20)     #index, add num
print(a)
a.remove(50)
print(a)
a.pop()    #remove the last digit
print(a)



a[1] = 20
print(a)
mutable = can change (list)
immutable = cannot change (tuple)


#tupels

tp = (1, 11, 22)  
b = (1)     #do not write one digit tuple like this
b = (1,)     #write this
print(b)
print(tp)

#swape num
c = 11
d = 41
c, d = d, c

print("the new c is ",c)
print("the new d is ",d)


temp = c    #traditional way (DSA method)
c = d 
d = temp
print(c,d)


a = 33
b =44
a = a^b
b = b^a
a = a^b


a = 33
b =44
a = a+b
b = a-b
a = a-b

print("The new a is ",a)
print("The new b is ",b)


