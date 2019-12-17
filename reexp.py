import re

#pattern=r'\d'
#pattern=r'\d\d+'
#pattern=r'\d*'
pattern=r'\d{3}'
sequence='sdasdkjashdksjahfjsafkhsakd0askfj0098asdfjjsaf'

#print(re.match(pattern,sequence))
#print(re.search(pattern,sequence))
print(re.findall(pattern,sequence))