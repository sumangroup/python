'''
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


print('index - not found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.index('Raju')
print('s2',s2)
print('-'*80)

print('rindex - found')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rindex('You')
print('s2',s2)
print('-'*80)


print('rindex - not found return value error')
s1="If You Born Poor it's Not Your Mistake. But, If You Die Poor it's Your Mistake"
print('s1',s1,len(s1))
s2=s1.rindex('Raju')
print('s2',s2)
print('-'*80)


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
'''
print('isdecimal')
print('12345','12345'.isdecimal())
print('123.45','123.45'.isdecimal())
print('12,345','12,345'.isdecimal())
print('Roman numeral: V','Roman numeral: V'.isdecimal())
print('-'*80)

print('isdigit')
print('12345','12345'.isdigit())
print('1/4','1/4'.isdigit())
print('123.45','123.45'.isdigit())
print('1,234','1,234'.isdigit())
print('Roman numeral: V','Roman numeral: V'.isdigit())
print('⁰¹²','⁰¹²'.isdigit())
print('-'*80)

print('isnumeric')
print('123','123'.isnumeric())
print('123.45','123.45'.isnumeric())
print('¼','¼'.isnumeric())
print('IX','IX'.isnumeric())
print('-'*80)

print('isidentifier')
print('s1','s1'.isidentifier())
print('RAJU123','RAJU123'.isidentifier())
print('_RAJU123','_RAJU123'.isidentifier())
print('0RAJU123','0RAJU123'.isidentifier())
print('RAJU1.23','RAJU12.3'.isidentifier())
print('if','if'.isidentifier())
print('-'*80)

print('islower')
print('Hello','Hello'.islower())
print('hello','hello'.islower())
print('hello world','hello world'.islower())    
print('123 hello','123 hello'.islower())
print('123 Hello','123 Hello'.islower())
print('',''.islower())
print('123 Hello','123 Hello'.islower())
print('123456','123456'.islower())
print('-'*80)

print('isupper')
print('HELLO','HELLO'.isupper())
print('HELLo','HELLo'.isupper())
print('123','123'.isupper())
print('123 HELLO','123 HELLO'.isupper())
print('123 HELLo','123 HELLo'.isupper())
print('',''.isupper())
print(' ',' '.isupper())
print(' #',' #'.isupper())
print(' HELLO',' HELLO'.isupper())
print('-'*80)

print('Istitle')
print('This Is A Title Case String','This Is A Title Case String'.istitle())
print('this is a title case string','this is a title case string'.istitle())
print('This is a Title Case String','This is a Title Case String'.istitle())
print("it's","it's".title())
print("It'S","It'S".istitle())
print("It's","It's".istitle())
print('-'*80)





















