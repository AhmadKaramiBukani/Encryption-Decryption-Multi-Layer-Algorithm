
#/////////////////////////////////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////////////////////////////////
#/////      CopyRight: Ahmad Karmi Bukani     احمد کرمی بوکانی    //////
#/////          Rojhalat Kurdistan  2025          روژهلات کوردستان     ///////
#//////////////////////////////////////////////////////////////////////////////////

import random
import colorama
import time


MyData="I Live in Kurdistan , my+name+is Ahmad.Karami.Bukani , I+am a Programmer , this+is my algorithm ..."
MyDataList = []
MyDataList2 = []

MyDictionaryPosition1_1=[]
MyDictionaryPosition2_1=[]


MyDictionaryPosition1_2=[]
MyDictionaryPosition2_2=[]

MyDictionaryPosition1_3=[]
MyDictionaryPosition2_3=[]

MyDictionaryPosition1_4=[]
MyDictionaryPosition2_4=[]

MyDictionaryPosition1_5=[]
MyDictionaryPosition2_5=[]

MyDictionaryPosition1_6=[]
MyDictionaryPosition2_6=[]

MyDictionaryPosition1_7=[]
MyDictionaryPosition2_7=[]

MyDictionaryPosition1_8=[]
MyDictionaryPosition2_8=[]

MyDictionaryPosition1_9=[]
MyDictionaryPosition2_9=[]

MyDictionaryPosition1_10=[]
MyDictionaryPosition2_10=[]

ElementCounter=0
MyDictionaryCounter=0
MyDictionary1 = [ "I+am","I+am+not","she+is" , "she+is+not","he+is", "he+is+not"]
MyDictionary2 = ["this+is","this+is+not","those+are","those+are+not","there+is", "there+is+not"]
MyDictionary3 = ["my+name+is","my+name+is+not"]
MyDictionary4 = ["Live","Love","Enable","Wish","Active","Write","Teaching","Going"]
MyDictionary5 = ["Programmer","Reporter","Worker","Teacher","Driver"]
MyDictionary6 = ["We","I","You","They"]
MyDictionary7 = ["car","cars","airplane","bus","earth","moon","ship","book","books","note","mobile","notes","notebook","night","day","algorithm"]
MyDictionary8 = ["in","to","from"]
MyDictionary9 = ["Kurdistan","USA","France","UK","Germany","Italy","Norway"]
MyDictionary10 = ["Ahmad.Karami.Bukani","David","Shaho","Eleya","Mary","Ako","Nishteman","Nechirvan"]


key_random_list = []
key_random_list2 = []

encrypt=""
decrypt=""

encrypt_gap=""
decrypt_gap=""
encrypt_gap_send_message=""
decrypt_correct_receive_message=""
max_len=20
source=""
index=0
duration = 0

print()
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"##################      Start Algorithm      ###################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)
print()
print(MyData)
print()

print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"##############   INSERT GAP TEXT LAYER  ########################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)

print()

GapText= ", "+ random.choice(MyDictionary6)+" "+random.choice(MyDictionary4)+" "+random.choice(MyDictionary8)+" "+random.choice(MyDictionary9)+" ..."
print(colorama.Fore.RED+colorama.Back.YELLOW+colorama.Style.BRIGHT+" Gap Text : "+GapText)
print(colorama.Fore.WHITE+colorama.Back.BLACK+colorama.Style.NORMAL+" ")
MyData=MyData.replace("...",GapText)
print(MyData)

MyDataList=MyData.split(" ")

time.sleep(duration)



print()
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"##################       HIDE TEXT LAYER     ###################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary1)):
     if element == MyDictionary1[i]:
         choice = random.choice(MyDictionary1)
         MyDictionaryPosition1_1.append(element)
         MyDictionaryPosition2_1.append(choice)
         MyDataList[ElementCounter] = choice






ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary2)):
     if element == MyDictionary2[i]:
         choice = random.choice(MyDictionary2)
         MyDictionaryPosition1_2.append(element)
         MyDictionaryPosition2_2.append(choice)
         MyDataList[ElementCounter] = choice








ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary3)):
     if element == MyDictionary3[i]:
         choice = random.choice(MyDictionary3)
         MyDictionaryPosition1_3.append(element)
         MyDictionaryPosition2_3.append(choice)
         MyDataList[ElementCounter] = choice






ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary4)):
     if element == MyDictionary4[i]:
         choice = random.choice(MyDictionary4)
         MyDictionaryPosition1_4.append(element)
         MyDictionaryPosition2_4.append(choice)
         MyDataList[ElementCounter] = choice




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary5)):
     if element == MyDictionary5[i]:
         choice = random.choice(MyDictionary5)
         MyDictionaryPosition1_5.append(element)
         MyDictionaryPosition2_5.append(choice)
         MyDataList[ElementCounter] = choice






ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary6)):
     if element == MyDictionary6[i]:
         choice = random.choice(MyDictionary6)
         MyDictionaryPosition1_6.append(element)
         MyDictionaryPosition2_6.append(choice)
         MyDataList[ElementCounter] = choice





ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary7)):
     if element == MyDictionary7[i]:
         choice = random.choice(MyDictionary7)
         MyDictionaryPosition1_7.append(element)
         MyDictionaryPosition2_7.append(choice)
         MyDataList[ElementCounter] = choice






ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary8)):
     if element == MyDictionary8[i]:
         choice = random.choice(MyDictionary8)
         MyDictionaryPosition1_8.append(element)
         MyDictionaryPosition2_8.append(choice)
         MyDataList[ElementCounter] = choice







ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary9)):
     if element == MyDictionary9[i]:
         choice = random.choice(MyDictionary9)
         MyDictionaryPosition1_9.append(element)
         MyDictionaryPosition2_9.append(choice)
         MyDataList[ElementCounter] = choice






ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionary10)):
     if element == MyDictionary10[i]:
         choice = random.choice(MyDictionary10)
         MyDictionaryPosition1_10.append(element)
         MyDictionaryPosition2_10.append(choice)
         MyDataList[ElementCounter] = choice


for element in MyDataList:
 print(element, end=" ")

print()
print()
time.sleep(duration)





print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"#############   INSERT ENCRYPTION RANDOM LAYER   ###############")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)



for element in MyDataList:
 source= source + element + " "

for i in range(0,max_len):
    key_random_list.append(random.randint(0,50))


print()
print(" Text : " + source)
print()

index=0
for char in source:
   if(index==max_len):
        index=0
   encrypt+=chr(ord(char)+key_random_list[index])
   if(index==len(source)):
       break
   index+=1

print()
print(" Encrypt : " + encrypt)
print()



time.sleep(duration)




print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"#############   INSERT ENCRYPTION GAP LAYER   ##################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)




print(" encrypt : ")
print(encrypt)
print()

#encrypt_gap=" 1234567890 "
encrypt_gap=""

for i in range(0,max_len):
    key_random_list2.append(random.randint(0,50))


index=0
for char in encrypt:
   if(index==max_len):
        index=0
   encrypt_gap+=chr(ord(char)+key_random_list2[index])
   if(index==len(encrypt_gap)):
       break
   index+=1

print()
print(" encrypt_gap : ")
print(encrypt_gap)
print()

"""
encrypt_gap = encrypt_gap + encrypt


print()
print("encrypt_gap = encrypt_gap + encrypt : ")
print(encrypt_gap)
print()
"""
print()
encrypt_gap_send_message=encrypt_gap
print(colorama.Fore.RED+ " Send Message : ")
print(encrypt_gap_send_message)

print()



time.sleep(duration)





print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"############   DELETE DECRYPTION GAP LAYER     #################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)



decrypt=""
index=0
for char in encrypt_gap:
    if index==max_len:
        index=0
    decrypt+=chr(ord(char)-key_random_list2[index])
    if index==len(encrypt_gap):
        break
    index+=1





#encrypt_gap_send_message=decrypt

print(colorama.Fore.WHITE)



#encrypt_gap=encrypt_gap.replace(encrypt_gap,encrypt)
print()
print(" decrypt : " + decrypt)
print()


time.sleep(duration)







print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"############   DELETE DECRYPTION RANDOM LAYER  #################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)


decrypt_gap=""
index=0
for char in decrypt:
    if index==max_len:
        index=0
    decrypt_gap+=chr(ord(char)-key_random_list[index])
    if index==len(decrypt):
        break
    index+=1



print()
print(" decrypt : " + decrypt_gap)
print()



decrypt = decrypt_gap


print()



time.sleep(duration)






print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"#################    SHOW TEXT LAYER   #########################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)




MyData=decrypt

MyDataList=MyData.split(" ")




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_1)):
      if element == MyDictionaryPosition2_1[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_1[i]
         MyDataList[ElementCounter] = choice
         break



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_2)):
      if element == MyDictionaryPosition2_2[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_2[i]
         MyDataList[ElementCounter] = choice
         break



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_3)):
      if element == MyDictionaryPosition2_3[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_3[i]
         MyDataList[ElementCounter] = choice
         break    



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_4)):
      if element == MyDictionaryPosition2_4[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_4[i]
         MyDataList[ElementCounter] = choice
         break



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_5)):
      if element == MyDictionaryPosition2_5[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_5[i]
         MyDataList[ElementCounter] = choice
         break




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_6)):
      if element == MyDictionaryPosition2_6[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_6[i]
         MyDataList[ElementCounter] = choice
         break




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_7)):
      if element == MyDictionaryPosition2_7[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_7[i]
         MyDataList[ElementCounter] = choice
         break



ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_8)):
      if element == MyDictionaryPosition2_8[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_8[i]
         MyDataList[ElementCounter] = choice
         break




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_9)):
      if element == MyDictionaryPosition2_9[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_9[i]
         MyDataList[ElementCounter] = choice
         break




ElementCounter=-1
for element in MyDataList:
    ElementCounter=ElementCounter+1
    for i in range(0,len(MyDictionaryPosition2_10)):
      if element == MyDictionaryPosition2_10[i] and ElementCounter<len(MyDataList):
         choice = MyDictionaryPosition1_10[i]
         MyDataList[ElementCounter] = choice
         break








source=""
for element in MyDataList:
 source = source + element + " "

print()
print(" Text : " + source)
print()








time.sleep(duration)

print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"##############   DELETE GAP TEXT LAYER  ########################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)


print()

MyDataList2=source.split(",")

source=""

for i in range(0,len(MyDataList2)-1):
 source = source + MyDataList2[i] + ","

source = source +"\b"
source = source +"..."
decrypt_correct_receive_message=source
print(colorama.Fore.RED+" Receive Message : "+ decrypt_correct_receive_message)

print(colorama.Fore.WHITE)

print()
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"##################       End Algorithm       ###################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)


"""
###############################################################################################

MyData=decrypt_correct_receive_message

print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################    PROCESS RESULT     #########################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)

print(10*"*")
print(colorama.Back.CYAN+colorama.Fore.BLACK+colorama.Style.NORMAL +" Main Text : ",end= " ")
print(MyData)
print(colorama.Back.BLACK+colorama.Fore.WHITE)
print()
print(10*"*")
print(colorama.Back.CYAN+colorama.Fore.BLACK+colorama.Style.NORMAL +" Gap Text : ",end= " ")
print(GapText)
print(colorama.Back.BLACK+colorama.Fore.WHITE)
print(10*"*")
print()
print(colorama.Back.GREEN+colorama.Fore.BLACK + colorama.Style.BRIGHT+ " Hide Text Layer : ",end= " ")
print(decrypt)
print()
print(" encrypt_gap : "+encrypt_gap)
print()
print(" encrypt_gap_send_message : " +encrypt_gap_send_message)
print()
print(colorama.Back.BLACK+colorama.Fore.WHITE)
print(10*"*")
print(colorama.Back.CYAN+colorama.Fore.BLACK+colorama.Style.NORMAL + " (Main Text) Show Text Layer & Decryption Random Layer : ",end= " ")
print()
print(MyData)
print(colorama.Back.BLACK+colorama.Fore.WHITE+colorama.Style.BRIGHT)
print(10*"*")





time.sleep(duration)





"""


print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################     INFORMATION    ############################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.YELLOW+"################################################################")
print(colorama.Fore.WHITE)



print()
print("List 1 , Key Max {0} = {1}".format(max_len,key_random_list))



print()
print("List 2 , Key Max {0} = {1}".format(max_len,key_random_list2))





print()
print(10*"*")

print()
for element in MyDictionaryPosition1_1:
    print("MyDictionaryPosition 1 - pos 1 = ",element)

for element in MyDictionaryPosition2_1:
    print("MyDictionaryPosition 1 - pos 2 = ",element)








print()
print(10*"*")

print()
for element in MyDictionaryPosition1_2:
    print("MyDictionaryPosition 2 - pos 1 = ",element)

for element in MyDictionaryPosition2_2:
    print("MyDictionaryPosition 2 - pos 2 = ",element)








print()
print(10*"*")

print()
for element in MyDictionaryPosition1_3:
    print("MyDictionaryPosition 3 - pos 1 = ",element)

for element in MyDictionaryPosition2_3:
    print("MyDictionaryPosition 3 - pos 2 = ",element)









print()
print(10*"*")

print()
for element in MyDictionaryPosition1_4:
    print("MyDictionaryPosition 4 - pos 1 = ",element)

for element in MyDictionaryPosition2_4:
    print("MyDictionaryPosition 4 - pos 2 = ",element)







print()
print(10*"*")

print()
for element in MyDictionaryPosition1_5:
    print("MyDictionaryPosition 5 - pos 1 = ",element)

for element in MyDictionaryPosition2_5:
    print("MyDictionaryPosition 5 - pos 2 = ",element)







print()
print(10*"*")

print()
for element in MyDictionaryPosition1_6:
    print("MyDictionaryPosition 6 - pos 1 = ",element)

for element in MyDictionaryPosition2_6:
    print("MyDictionaryPosition 6 - pos 2 = ",element)






print()
print(10*"*")


print()
for element in MyDictionaryPosition1_7:
    print("MyDictionaryPosition 7 - pos 1 = ",element)

for element in MyDictionaryPosition2_7:
    print("MyDictionaryPosition 7 - pos 2 = ",element)








print()
print(10*"*")



print()
for element in MyDictionaryPosition1_8:
    print("MyDictionaryPosition 8 - pos 1 = ",element)

for element in MyDictionaryPosition2_8:
    print("MyDictionaryPosition 8 - pos 2 = ",element)









print()
print(10*"*")




print()
for element in MyDictionaryPosition1_9:
    print("MyDictionaryPosition 9 - pos 1 = ",element)

for element in MyDictionaryPosition2_9:
    print("MyDictionaryPosition 9 - pos 2 = ",element)









print()
print(10*"*")


print()
for element in MyDictionaryPosition1_10:
    print("MyDictionaryPosition 10 - pos 1 = ",element)

for element in MyDictionaryPosition2_10:
    print("MyDictionaryPosition 10 - pos 2 = ",element)

print()
print()
print()
