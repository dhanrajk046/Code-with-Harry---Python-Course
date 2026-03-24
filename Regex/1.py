import re

text = "hello123"

pattern = r"\d+"  # Matches one or more digits

result = re.search(pattern, text)

print(result.group())