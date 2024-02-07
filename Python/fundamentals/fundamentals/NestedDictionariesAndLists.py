x = [[5, 2, 3], [15, 8, 9]]
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first+name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Bryant', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 30}]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(some_list):
    for x in range(len(some_list)):
        for key in some_list[x]:
            print(key, " - ", some_list[x][key])

iterateDictionary(students)
print("-------------------------------------------")

def iterateDictionary2(key_name, some_list):
    for x in range(len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2('first_name', students)
print("---------------------")
iterateDictionary2('last_name', students)
print("-------------------------------------------")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key)
        for index in range(len(some_dict[key])):
            print(some_dict[key][index])
        print(" ")


printInfo(dojo)