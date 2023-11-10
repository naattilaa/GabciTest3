szotar = {"name":[],"house":[]};

szotar["name"].append("Gipsz Jakab")
szotar["house"].append("gipsz_jakab_haza")

szotar["name"].append("John Doe")
szotar["house"].append("john_doe_haza")


ujszotar = {"fname":[], "lname":[], "house":[]}

for i in range(0,len(szotar)):
     splittedname = szotar["name"][i].split()
     print(splittedname)
     print(i)
     ujszotar["fname"].append(splittedname[0])
     ujszotar["lname"].append(splittedname[1])
     ujszotar["house"].append(szotar["house"][i])

print(ujszotar)
