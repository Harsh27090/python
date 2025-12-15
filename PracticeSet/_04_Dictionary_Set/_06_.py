# 4 friends -> their fav. lang.
my_dict ={}

for i in range(4):
    my_dict.update({input("your name:"): input("your fav. lang.:")})

print(my_dict)