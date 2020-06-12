import unittest

hours = input("enter number of hours :")
capacity = int(input("enter number of units :"))
dict = {"Large":10 , "XLarge":20, "2XLarge":40, "4XLarge":80, "8XLarge":160, "10XLarge":320}


NewYork = [120, 230, 450, 774, 1400, 2820]
India = [140, 0, 413, 890, 1300, 2970]
China = [110, 200, 0, 670, 1180, 0]



count6 = 0
def tenX(x, y):
    
    
    if capacity > dict["10XLarge"]:
        
        
        
        res = dict["10XLarge"]
        
        for i in range(1,100):
            
            global count6
            count6 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
        
    return count6 - 1

UtenX = (dict["10XLarge"] * (count6 -1))
NtenX = NewYork[len(NewYork)-1] * (count6 -1)
#print("overall units {}".format(dict["10XLarge"] * (count61 -1) ))
ItenX = India[len(India)-1] * (count6 -1)
CtenX = China[len(China)-1] * (count6 -1)
print("tenunit", UtenX)


print("10X *", tenX(hours, capacity))  
#print("num of units:", sol)
print("overall units  {}".format(dict["10XLarge"] * (count6 -1)))
print("cost in NewYork:", NewYork[len(NewYork)-1] * (count6 -1))
#print("overall units {}".format(dict["10XLarge"] * (count61 -1) ))
print("cost in India:", India[len(India)-1] * (count6 -1))
print("cost in China:", China[len(China)-1] * (count6 -1))

#ten = 0
#if UtenX == capacity:
#    ten = NtenX, ItenX, CtenX
#else:
#    ten= capacity - UtenX
    
#print("unit difference:", ten)

#tN = 0
#print("tennewyork:", tN)
"""
print("10X *", tenX(hours, capacity))
#print("num of units:", sol)
print("overall units  {}".format(dict["10XLarge"] * (count6 -1) * hours ))
print("cost in NewYork:", NewYork[len(NewYork)-1] * (count6 -1))
#print("overall units {}".format(dict["10XLarge"] * (count61 -1) ))
print("cost in India:", India[len(India)-1] * (count6 -1))
print("cost in China:", China[len(China)-1] * (count6 -1))
#print("unit difference 10X {}".format((capacity) - (dict["10XLarge"] * (count6 -1)))
"""



count5 = 0
def eightX(x1, y1):
    
    
    if capacity > dict["8XLarge"]:
        
        
        
        res = dict["8XLarge"]
        
        for i in range(1,100):
            
            global count5
            count5 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
        
    return count5 - 1
    
UeightX = int(dict["8XLarge"] * (count5 -1))
NeightX = ((NewYork[len(NewYork)-2]) * (count5 -1))
#print("overall units {}".format(dict["10XLarge"] * (count51 -1) ))
IeightX = ((India[len(India)-2]) * (count5 -1))
CeightX = ((China[len(China)-2]) * (count5 -1))
#print("ueight:", UeightX)
 
print("8X *", eightX(hours, capacity))
#print("num of units:", sol)
print("overall units  {}".format(dict["8XLarge"] * (count5 -1)))
print("cost in NewYork:", NewYork[len(NewYork)-2] * (count5 -1))
#print("overall units {}".format(dict["10XLarge"] * (count51 -1) ))
print("cost in India:", India[len(India)-2] * (count5 -1))
print("cost in China:", China[len(China)-2] * (count5 -1))

count4 = 0
def fourX(x2, y2):
    
    
    if capacity > dict["4XLarge"]:
        
        
        
        res = dict["4XLarge"]
        
        for i in range(1,100):
            
            global count4
            count4 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
        
    return count4 - 1

UfourX = dict["4XLarge"] * (count4 -1) 
NfourX = NewYork[len(NewYork)-3] * (count4 -1)
#print("overall units {}".format(dict["10XLarge"] * (count4 -1) ))
IfourX = India[len(India)-3] * (count4 -1)
CfourX = China[len(China)-3] * (count4 -1)
 
print("4X *",fourX(hours, capacity))
#print("num of units:", sol)
print("overall units  {}".format(dict["4XLarge"] * (count4 -1) ))
print("cost in NewYork:", NewYork[len(NewYork)-3] * (count4 -1))
#print("overall units {}".format(dict["10XLarge"] * (count4 -1) ))
print("cost in India:", India[len(India)-3] * (count4 -1))
print("cost in China:", China[len(China)-3] * (count4 -1))

count3 = 0
def twoX(x3, y3):
    
    
    if capacity > dict["2XLarge"]:
        
        
        
        res = dict["2XLarge"]
        
        for i in range(1,100):
            
            global count3
            count3 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
                
    UtwoX = dict["2XLarge"] * (count3 -1) 
    NtwoX = NewYork[len(NewYork)-4] * (count3 -1)
    #print("overall units {}".format(dict["10XLarge"] * (count3 -1) ))
    ItwoX = India[len(India)-4] * (count3 -1)
    CtwoX = China[len(China)-4] * (count3 -1)
    utwo = int(UtwoX)
    Ntwo = int(NtwoX)
    Itwo = int(ItwoX)
    Ctwo = int(CtwoX)
        
    return count3 - 1

UtwoX = dict["2XLarge"] * (count3 -1) 
NtwoX = NewYork[len(NewYork)-4] * (count3 -1)
#print("overall units {}".format(dict["10XLarge"] * (count3 -1) ))
ItwoX = India[len(India)-4] * (count3 -1)
CtwoX = China[len(China)-4] * (count3 -1)
        

 
print("2X *", twoX(hours, capacity))
#print("num of units:", sol)
print("overall units  {}".format(dict["2XLarge"] * (count3 -1) ))
print("cost in NewYork:", NewYork[len(NewYork)-4] * (count3 -1))
#print("overall units {}".format(dict["10XLarge"] * (count3 -1) ))
print("cost in India:", India[len(India)-4] * (count3 -1))
print("cost in China:", China[len(China)-4] * (count3 -1))


count2 = 0
def XLarge(x4, y4):
    
    
    if capacity > dict["XLarge"]:
        
        
        
        res = dict["XLarge"]
        
        for i in range(1,100):
            
            global count2
            count2 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
        
    return count2 - 1
    
UnitsX = dict["XLarge"] * (count2 -1) 
NcostX = NewYork[len(NewYork)-5] * (count2 -1)
#print("overall units {}".format(dict["10XLarge"] * (count2 -1) ))
IcostX = India[len(India)-5] * (count2 -1)
CcostX = China[len(China)-5] * (count2 -1)
 
print("XL *",XLarge(hours, capacity))
#print("num of units:", sol)
print("overall units  {}".format(dict["XLarge"] * (count2 -1) ))
print("cost in NewYork:", NewYork[len(NewYork)-5] * (count2 -1))
#print("overall units {}".format(dict["10XLarge"] * (count2 -1) ))
print("cost in India:", India[len(India)-5] * (count2 -1))
print("cost in China:", China[len(China)-5] * (count2 -1))


count1 = 0
def Large(x5, y5):
    
    
    if capacity > dict["Large"]:
        
        
        
        res = dict["Large"]
        
        for i in range(1,100):
            
            global count1
            count1 +=1
            sol = res * i
            if sol < capacity:
                continue
                
            else:
                
                break
    
        
    return count1 - 1
    
UnitsL = dict["Large"] * (count1 -1) 
NcostL = NewYork[len(NewYork)-6] * (count1 -1)
#print("overall units {}".format(dict["10XLarge"] * (count1 -1) ))
IcostL = India[len(India)-6] * (count1 -1)
CcostL = China[len(China)-6] * (count1 -1)
 
print("L *", Large(hours, capacity))  
#print("num of units:", sol)
print("overall units  {}".format(dict["Large"] * (count1 -1)))
print("cost in NewYork:", NewYork[len(NewYork)-6] * (count1 -1))
#print("overall units {}".format(dict["10XLarge"] * (count1 -1) ))
print("cost in India:", India[len(India)-6] * (count1 -1))
print("cost in China:", China[len(China)-6] * (count1 -1))


#print("result after")
#print(NcostL)

#city = ["New York", "India", "China"]


  
class test(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertTrue(True) 
  
if __name__ == '__main__': 
    unittest.main() 
    
    
    

#print(dict.zip("region": city[0], "total_cost": 