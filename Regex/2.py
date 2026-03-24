import re

email = "test_23@gmail.com"

pattern = r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$' 
 # Matches a valid email address

if re.match(pattern, email):
     print("Valid email address")
else:  
     print("Invalid email address")