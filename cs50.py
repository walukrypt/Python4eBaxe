#capitalize the user name and remove whitespaces
name = input("whats your name").strip().title()
# split name to first and last 
first, last = name.split("")
#say hello to the user
print(f"Hello, {name}")