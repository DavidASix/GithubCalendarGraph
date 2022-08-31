import os
import re
# Regex to find any generic code blocks in a README
codeFindRe = "(?<=```)(.*)(?=```)"

# Rewrite the README to show some work is done
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
