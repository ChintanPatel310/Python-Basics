# dictionary is nothing but key value Pair

d1 = {}      #dictionary type
print(type(d1)) 

d2 ={
      "introduction":"yourself", 
      "trip":"mountain", 
      "see":"sea"
    }
print(d2)    #print dictionary
print(d2["see"])   #print waht you see? :'sea'

d2 = {
    "introduction":"yourself", 
    "trip":
        {
            "a":"mountain", 
            "b":"river", 
            "c":"one-day"
        }, 
    "see":"sea"
    }      #dictionary into dictionary
d2["school"] = "morning"  #new string add to dictionary
d2[55] = 25 
del d2[55]  #remove into dictionary
print(d2["trip"]["b"])  #print dic trip option b
print(d2)



#functions of dic
d3 = d2         
#print(d2.copy())          #use  dot-copy function
# del d3 ["trip"]
# print(d2)
print(d3.get("trip"))  #we can write d3 or d2
d2.update({"season":"monsoon"})   #update function
print(d2.keys())
print(d2.items())
a = d2.get("trip")
# print(d2)
print(a)



#users choice


d5 ={
        "joorfood":"burgger",
        "panjabi":"paneer",
        "rice":"hydrabadi-biryani",
        "drinks":"coffe",
        "ice-cream":"amaul",
    }
d = input("choice:")
print(d5[d])







