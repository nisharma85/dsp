################################################################
#Part 3: Dictionaries

data["las1"] = data["name"].str.split().str[-1]
data["firs1"] = data["name"].str.split().str[0]
faculty_dict= dict([(i,[a,b,c ]) for i, a,b,c in zip(data.las1,data.degree,data.title,data.email)])

print('The first three key and value pairs in first dictionary:')
print faculty_dict.items()[:3]
 
##########################
 data["name_new"] = data["firs1"].map(str) + ","+ data["las1"]
professor_dict= dict([(i,[a,b,c ]) for i, a,b,c in zip(data.name_new,data.degree,data.title,data.email)])

print('The first three key and value pairs in second dictionary:')
print professor_dict.items()[:3]
 
##########################
 
professor_dict_sorted = dict(sorted(professor_dict.items(), key=operator.itemgetter(1)))

print('The first three key and value pairs in second dictionary sorted by last name:')
print professor_dict_sorted.items() [:3]
 
################################################################ 
