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

# Push new README to Gitub
os.system('cmd /c "git add ."')
os.system('cmd /c "git commit -m \"Incremented README to: ' + currentWrites + '.\""')
os.system('cmd /k "git push"')
