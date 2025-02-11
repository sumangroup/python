#dict
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
print('dict1[name]',dict1['name'])
print('dict1[age]',dict1['age'])
print('dict1[phone]',dict1['phone'])
print('dict1[mrg]',dict1['mrg'])
print('dict1[mrg][name]',dict1['mrg']['name'])
print('dict1[mrg][phone]',dict1['mrg']['phone'])
print('dict1[skills]',dict1['skills'])
print('dict1[skills][0]',dict1['skills'][0])
print('dict1[skills][1]',dict1['skills'][1])
print('dict1[skills][2]',dict1['skills'][2])
print('-'*80)

dict2=dict(name='Raju Mane',age=32,phone=9833395327,)
print('dict2',dict2,len(dict2))


list1=[('name','Raju Mane'),('age',32),('phone',9833395327)]
dict3=dict(list1)
print('dict3',dict3,len(dict3))









