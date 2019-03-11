import string

#xor 97-122

chars = []
with open("p059.txt") as f:
    chars = f.readlines()[0].split(",")

nums = list(int(x) for x in chars)
for x in range(97,123):
    for y in range(97,123):
        for z in range(97,123):
            # print(f"using key: {chr(x)}{chr(y)}{chr(z)}")
            new_string = []
            the_sum = 0
            for (index, val) in enumerate(nums):
                if index%3 == 0:
                    new_string.append(chr(val^x))
                    the_sum += val^x
                elif index%3 == 1:
                    new_string.append(chr(val^y))
                    the_sum += val^y
                elif index%3 == 2:
                    new_string.append(chr(val^z))
                    the_sum += val^z
            new_string = ''.join(new_string)
            if "euler" in new_string.lower():
                print(f"For key: {chr(x)}{chr(y)}{chr(z)}, we have: {new_string}\n Sum: {the_sum}")
