# rename a file

# with open('old.txt') as f:
#     content = f.read()
#
# with open('old_rename.txt', 'w') as f:
#     f.write(content)

import os
os.rename('old.txt', 'old_renamed.txt')