# assignment 1

import re
with open('baby2008.html', 'r') as f:
    contents = f.read()
    
pattern = re.compile(r'Baby Names')
    
matches = pattern.finditer(contents)

    
for i in matches:
    print(i)


# assignment 2
with open('names.txt', 'r') as p:
    content = p.read()
    
    print(content)
    
    
 #assignment 3   
import os

cwd = os.getcwd()

print(cwd)




#assignment 4
def search(arr, low, high, x):
    
    # check for the base case
    if high >= low:
        mid = (high + low) // 2
        
        #if elt is present at the middle
        if arr[mid] == x:
            return mid
        
        #check if elt is smaller than mid
        elif arr[mid] > x:
            return search(arr, low, mid - 1, x)
    
        else:
            return search(arr, mid+1, high, x)
    else:
        #elt is not present in the array
        return -1
    
    
arr = [2,3,4,10,40]
x = 2

result = search(arr, 0, len(arr)-1, x)    
    
if result != -1:
    print('element is at index', str(result))

else:
    print('element is not in the array')         