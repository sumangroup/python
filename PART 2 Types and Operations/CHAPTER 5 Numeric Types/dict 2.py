dict1={
    "name":"Raju Mane",
    "age":32,
    "phone":9833395327,
    'mrg':{
        'name':'Rasika',
        'phone':123456789
        },
    'skills':['c','java','c++']
    }

print('dict1',dict1,len(dict1))
name=dict1.get('name')
print('name',name)
skills=dict1.get('skills')
print('skills',skills)
address=dict1.get('address')
print('address',address)
print('-'*80)

print('items')
items=dict1.items()
print('items',items)
print()
for x in items:
    print(x)
print('-'*80)


print('keys')
keys=dict1.keys()
print('keys',keys)
for x in keys:
    print(x)
print('-'*80)

print('values')
values=dict1.values()
print('values',values)
for x in values:
    print(x)
print('-'*80)


print('pop')
pop=dict1.pop('name')
print('pop',pop)
address=dict1.pop('address','lower parel')
print('address',address)
print('dict1',dict1,len(dict1))
print('-'*80)

print('popitem')
popitem=dict1.popitem()
print('popitem',popitem)
popitem=dict1.popitem()
print('popitem',popitem)
popitem=dict1.popitem()
print('popitem',popitem)
popitem=dict1.popitem()
print('popitem',popitem)
print('dict1',dict1,len(dict1))
print('-'*80)

print('setdefault')
print('dict1',dict1,len(dict1))
dict1.setdefault('name','raju mane')
print('dict1',dict1,len(dict1))
dict2={
    "age":32,
    "phone":9833395327
    }

dict1.update(dict2)
print('dict1',dict1,len(dict1))
