s = set()
# print(type(s))
l = [1, 2, 3, 4]    #list
s_from_list = set (l)
print(s_from_list)
# print(type(s_from_list))
s.add (11)        #add number in set
#s.add (11)     #set written unique values
s.add(2)
s.union({2, 11, 3})   
s1 = s.union({2, 11, 3})            #union of sets
s2 = s.intersection({2, 11, 3})  #intrection sets
print(s, s2)                    #print two sets
print(max(s2))                  #maximum number of set
print(min(s))                   #minimum number of set
s3 = {13, 14}
print(s.isdisjoint(s3))       #disjoint function
s3.remove(13)                  #remove number from set
print(s3)


