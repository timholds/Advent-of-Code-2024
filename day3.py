import re


# read in data3.txt as a string
with open('data/data3.txt', 'r') as f:

    text = f.read()
# need to regex match for 
# "mul(" + 1-3 digit chars + "," + 1-3 digit chars + ")
# 

    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    print(matches)
    print(len(matches))


running_sum = 0
for s in matches:
    # convert mul(523,283) to actually do 
    print(s)
    factors = re.findall(r'\d{1,3}', s)
    product = int(factors[0]) * int(factors[1])
    running_sum += product  

print(running_sum)
test = 'mul(168,87)}*:mul(911,800)(%,)where()#&&$mul(734,19)'

# want to get this to do
test1 = 'mul(819<%/{how(675,621)where()@(>from()mul(722,49)'
# 168*87, splitting on the comma
# 911*800 splitting on the comma
# 734*19, """"

# 675*621
# 722*49
# do we want 819* something? or does that get filtered out 
