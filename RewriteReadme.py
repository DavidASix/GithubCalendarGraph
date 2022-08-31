import os
import re
codeFindRe = "(?<=```)(.*)(?=```)"

with open('./README.md', 'r') as file:
    rm = file.read()

readMeArr = re.split(codeFindRe, rm)
currentWrites = str(int(readMeArr[1]) + 1)
newText = readMeArr[0] + currentWrites + readMeArr[2]

with open('./README.md', 'w') as file:
    file.write(newText)

os.system('cmd /c "git add ."')
os.system('cmd /k "git commit -m \"Incremented README to: ' + currentWrites + '.\""')