l1=[
    1,2,3
    ]
print('l1',l1,len(l1))
print('l1[0]',l1[0])
print('l1[1]',l1[1])
print('l1[2]',l1[2])
print("-"*80)
l2=[
    1,
    ["Raju","Rohan","Rasika","Aryan","Arya"],
    2,3
    ]
print('l2',l2,len(l2))
print('l2[0]',l2[0])
print('l2[1]',l2[1])
print('l2[2]',l2[2])
print('l2[3]',l2[3])
print('l2[1][3]',l2[1][3])
print('l2[1][1]',l2[1][1])
print("-"*80)

l3=[
    1,2,
    ["Raju","Rohan","Rasika","Aryan","Arya",["java","python",["1.23","1.27"]]],
    3.4
    ]
print('l3',l3,len(l3))
print('l3[0]',l3[0])
print('l3[1]',l3[1])
print('l3[2]',l3[2])
print('l3[3]',l3[3])
print('l3[2][3]',l3[2][3])
print('l3[2][5]',l3[2][5])
print('l3[2][5][1]',l3[2][5][1])
print('l3[2][5][2][1]',l3[2][5][2][1],"l3[2][3]",l3[2][3])
print("-"*80)

l4=[
    101,
    {
        "name":"Raju Ramchandra Mane",
        "age":32,
        "phone":9833395327,
        "skills":["java","c","c++",
                  {
                    "version":["1.23","1.27",(1,2,3,{
                            "years":[1995,2000,{1,5,6}]
                        })]
            }]
        },
    25000.500,
    ["Raju","Rohan","Rasika","Aryan","Arya"]
     ]
print('l4',l4,len(l4))
print('l4[0]',l4[0])
print()
print('l4[1]',l4[1])
print()
print('l4[2]',l4[2])
print()
print('l4[3]',l4[3])
print()
print('l4[1][name]',l4[1]["name"])
print('l4[1][age]',l4[1]["age"])
print('l4[1][phone]',l4[1]["phone"])
print('l4[1][skills]',l4[1]["skills"])
print('l4[1][skills][2]',l4[1]["skills"][2])
print('l4[1][skills][3]',l4[1]["skills"][3])
print('l4[1][skills][3][version]',l4[1]["skills"][3]["version"])
print('l4[1][skills][3][version][1]',l4[1]["skills"][3]["version"][1])
print('l4[1][skills][3][version]',l4[1]["skills"][3]["version"])
print('l4[1][skills][3][version][2]',l4[1]["skills"][3]["version"][2])
print('l4[1][skills][3][version][2][2]',l4[1]["skills"][3]["version"][2][2])
print('l4[1][skills][3][version][2][3][years][1]',l4[1]["skills"][3]["version"][2][3]["years"][1])
print('l4[1][skills][3][version][2][3][years][2][0]',l4[1]["skills"][3]["version"][2][3]["years"][2][0])





