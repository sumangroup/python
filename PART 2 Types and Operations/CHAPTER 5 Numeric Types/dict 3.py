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
print('-'*80)
dict1['name']='Dhanshree Mane'
print('dict1',dict1,len(dict1))
dict1['phone']=5265412541
print('-'*80)
print('dict1',dict1,len(dict1))
dict1['skills'].append('python')
print('-'*80)
print('dict1',dict1,len(dict1))
dict1['phone']=[5265412541,9833395327]
print('-'*80)
print('dict1',dict1,len(dict1))

dict1['address']='virar'
print('-'*80)
print('dict1',dict1,len(dict1))
