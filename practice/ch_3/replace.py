letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

ltr = letter.replace("<|Name|>", "Tusharkanta Palo")
ltr = ltr.replace("<|Date|>", "14 October 2026")

print(f"{ltr}")
