# tables from 2 to 20 in diff. files in folder
# import os
#
# os.makedirs('newfolder', exist_ok = True)
for i in range(2,21):
    with open(f'tables/table_{i}.txt', 'w') as f:
        for j in range(1,11):
            f.write(f'{i}x{j} = {i*j}\n')

with open(f'tables/table_2.txt') as f:
    print(f.read())