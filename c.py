import re
pattern=r'[\w\.]+@\w+\.\w+'
sequence='asdjsakjdhas tea@lemon.cup tea.lemon@cup.here hi@tea.lemon@cup.here'
print(re.findall(pattern,sequence))