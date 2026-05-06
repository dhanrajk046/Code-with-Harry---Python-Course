# letter = '''Dear <|Name|>,
#         You are selected!
#         <|Date|>'''
# print(letter.replace("<|Name|>","Sonu").replace("<|Date|>","27 December 2025"))

letter = '''Dear <|Name|>,
        You are selected!
        <|Date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>", "02 September 2050"))