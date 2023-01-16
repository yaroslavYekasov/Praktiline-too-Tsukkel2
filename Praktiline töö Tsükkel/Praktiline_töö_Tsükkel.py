from random import *

print("Ülesanne 0 for i")

print()

n = int(input("Enter the number "))  
for i in range(1,11):  
    c = n*i  
    print(n,"*",i,"=",c) 

print()

print("Ülesanne 0 while")

print()

i=0
number = int(input("Enter the number:")) 
while i <=10: 
    c = n*i  
    print(number,"*",i,"=",c)
    i +=1 
    
print()

print("Ülesanne 12 for i")

print()                         

try:
    aasta =1
    skol = (int(input("kui palju te tahate panna raha pangasse => ")))
    skol1 = skol
    print("Aasta   Algsumma    Intress     Aasta lõpuks")
    for x in range (5):
        procent=int(skol/100*5)
        proc_skol=int((skol/100*5)+skol)
        print(aasta,"      ",skol,"      ",procent,"      ",proc_skol)
        aasta +=1
        skol +=procent
    print("Summa kokku:", proc_skol)
    kasum = proc_skol - skol1
    print("Kasum:", kasum)
except:
    print("errror")
print()

print("Ülesanne 12 while")
  
print()
try:
   aasta =1
   skol = (int(input("kui palju te tahate panna raha pangasse  => ")))
   skol1 = skol
   print("Aasta   Algsumma    Intress     Aasta lõpuks")
   while aasta != 6:
       procent=int(skol/100*5)
       proc_skol=int((skol/100*5)+skol)
       print(aasta,"      ",skol,"      ",procent,"      ",proc_skol)
       aasta +=1
       skol +=procent
   print("Summa kokku:", proc_skol)
   kasum = proc_skol - skol1
   print("Kasum:", kasum)
except:
   print("errror")

#10
#x=1
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#    x+=1

#16
#ans = random.randint(1,10)
#while True:
#    g=input("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp* ) ")
#    if g.lower() == "lõpp":
#        print("mäng on läbi")
#        break
#    if not g.isnumeric():
#        print("Vale  andmetüüp!")
#        continue
#    g = int(g)
#    if g == ans:
#        print("õige! sa arvasid ära!")
#        break
#    if g>10 or g<1:

#        print("Vahemisik on vale!")
#        continue
#    elif g !=ans:
#        print(f"vale! proovi veel korra!")
#        continue

#3
#try:
#    f=int(input("mitu ülesandeid sa tahad?"))
#    for d in range (0,f,1):
#        print(f"ülesanne {g}: ")
#        a = randint(1,50)
#        b = randint(1,50)
#        c=a+b
#        for i in range (0,5,1):
#            answer=int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print("see on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        g=g+1
#        print(f"õige on {c}")
#except:
#    print("see ei ole õige")

#13
#print("arv", "  ruut  ","  kuup")
#for i in range(1,11):
#    print(f" {1}    {1 ** 2}    {1 ** 3}")
#    print("teine variant")
#    print("arv", "  ruut ", "  kuup")
#    i=1
#while i<11:
#    print(f"  {1}    {1 ** 2}    {1 ** 3}")
#    i +=1

#6
#print()
#print("Ülessanne 6 1")
#print()
#for i in range (0,5):
#    print("* "*5)
#print()
#for i in range (0,10):
#    print("* "*1)
#print()
#for i in range (0,10):
#    print("* "*(10-i))
#print()
