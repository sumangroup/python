print('capitalize')
s1="if You Born Poor it's not your mistake"
print("s1",s1,len(s1))
s2=s1.capitalize()
print('s2',s2,len(s2))
print("s1",s1,len(s1))
print('-'*80)

print('casefold')
s1='HELLO, wOrld! ß İ'
print('s1',s1,len(s1))
s2=s1.casefold()
print('s2',s2,len(s2))
print('-'*80)

print('lower')
s1='HELLO, WORLD! ß İ'
print('s1',s1,len(s1))
s2=s1.lower()
print('s2',s2,len(s2))
print('-'*80)

print('upper')
s1="hello, world!"
print('s1',s1,len(s1))
s2=s1.upper()
print('s2',s2,len(s2))
print('-'*80)

print('title')
s1='if You Born Poor it"s not your mistake'
print('s1',s1,len(s1))
s2=s1.title()
print('s2',s2,len(s2))
print('-'*80)

print('center')
s1='HELLO, WORLD!'
print('s1',s1,len(s1))
s2=s1.center(22,'#')
print('s2',s2,len(s2))
print('-'*80)

print('count')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.count('You',15,30)
print('s2',s2)
print('-'*80)

print('find - found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.find('You',15,30)
print('s2',s2)
print('-'*80)

print('find - Not found return -1')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.find('Raju')
print('s2',s2)
print('-'*80)


print('rfind - found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rfind('You')
print('s2',s2)
print('-'*80)

print('rfind - not found return -1')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rfind('Raju')
print('s2',s2)
print('-'*80)

print('index - found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.index('You',15,30)
print('s2',s2)
print('-'*80)

'''
print('index - not found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.index('Raju')
print('s2',s2)
print('-'*80)
'''
print('rindex - found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rindex('You')
print('s2',s2)
print('-'*80)

'''
print('rindex - not found return value error')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rindex('Raju')
print('s2',s2)
print('-'*80)
'''

print('isalnum')
s1='Python3'
print('s1',s1,len(s1))
s2=s1.isalnum()
print('s2',s2)
print('Python 3'.isalnum())
print('123'.isalnum())
print('?'.isalnum())
print('-'*80)

print('isalpha')
print('HelloWorld'.isalpha())
print('Hello World'.isalpha())
print('123'.isalpha())
print(''.isalpha())
print('-'*80)

print('isdecimal')
print('12345'.isdecimal())
print('123.45'.isdecimal())
print('12,345'.isdecimal())
print('Roman numeral: V'.isdecimal())










      
