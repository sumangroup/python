print('zfill')
s1="1"
print('s1',s1,len(s1))
s2=s1.zfill(3)
print('s2',s2,len(s2))
print('-'*80)

print('strip')
s1="   Raju Mane   "
print('s1',s1,len(s1))
s2=s1.strip()
print('s2',s2,len(s2))
print('-'*80)

print('lstrip')
s1="   Raju Mane   "
print('s1',s1,len(s1))
s2=s1.lstrip()
print('s2',s2,len(s2))
print('-'*80)


print('rstrip')
s1="   Raju Mane   "
print('s1',s1,len(s1))
s2=s1.rstrip()
print('s2',s2,len(s2))
print('-'*80)

print('split')
s1="101,Raju Ramchandra Mane, 32, 25000"
print('s1',s1,len(s1))
s2=s1.split(",",2)
print('s2',s2,len(s2))
print('-'*80)


print('rsplit')
s1="101,Raju Ramchandra Mane, 32, 25000"
print('s1',s1,len(s1))
s2=s1.rsplit(",",2)
print('s2',s2,len(s2))
print('-'*80)


print('partition')
s1="Aryan Saiprasad Lakkavatri Madhavi"
print('s1',s1,len(s1))
s2=s1.partition(" ")
print('s2',s2,len(s2))
print('-'*80)

print('rpartition')
s1="Aryan Saiprasad Lakkavatri Madhavi"
print('s1',s1,len(s1))
s2=s1.rpartition(" ")
print('s2',s2,len(s2))
print('-'*80)

print('replace')
s1="hello world. These is hello world. My hello world"
print('s1',s1,len(s1))
s2=s1.replace("hello","HELLO",2)
print('s2',s2)
print('-'*80)

print('startswith')
s1="If you if Born poor if it's not your mistake"
print('s1',s1,len(s1))
s2=s1.startswith("if",7)
print('s2',s2)
print('-'*80)

print('endswith')
s1="If you if Born poor if it's not your mistake"
print('s1',s1,len(s1))
s2=s1.endswith("mistake",7,15)
print('s2',s2)
print('-'*80)

print('ljust')
s1="India, officially the Republic of India, is a country in South Asia.\n It is the seventh-largest country by area; \nthe most populous country from June 2023 onwards; \nand since its independence in 1947,\n the world's most populous democracy."
print('s1',s1,len(s1))
s2=s1.ljust(500,"$")
print('s2',s2,len(s2))
print('-'*80)


print('rjust')
s1="India, officially the Republic of India, is a country in South Asia.\n It is the seventh-largest country by area; \nthe most populous country from June 2023 onwards; \nand since its independence in 1947,\n the world's most populous democracy."
print('s1',s1,len(s1))
s2=s1.rjust(500,"$")
print('s2',s2,len(s2))
print('-'*80)

print('swapcase')
s1="Hello World"
print('s1',s1,len(s1))
s2=s1.swapcase()
print('s2',s2,len(s2))
