import re


# read in data3.txt as a string
with open('data/data3.txt', 'r') as f:
    text = f.read()
    # need to regex match for 
    # "mul(" + 1-3 digit chars + "," + 1-3 digit chars + ")
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, text)
    # print(matches)
    # print(len(matches))


running_sum = 0
for s in matches:
    # convert mul(523,283) to actually do 
    factors = re.findall(r'\d{1,3}', s)
    product = int(factors[0]) * int(factors[1])
    running_sum += product  

print(running_sum)


## PART 2:
process = True

segments = re.split(r'(do\(\)|don\'t\(\))', text)
pattern = r"mul\(\d{1,3},\d{1,3}\)"
products = []
for seg in segments:
    print(seg, "\n")
    if seg == "do()":
        process = True
    elif seg == "don't()":
        process = False
    
    elif process:
        matches = re.findall(pattern, seg)
        print(matches)

        for s in matches:
            # convert mul(523,283) to actually do 
            factors = re.findall(r'\d{1,3}', s)
            products.append(int(factors[0]) * int(factors[1]))

print(sum(products))

