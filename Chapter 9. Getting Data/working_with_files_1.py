import re
starts_with_hash = 0

with open('the_bible.txt', 'r') as file:
    for line in file:  # look at each line in the file
        if re.match("^#", line):  # use a regex to see if it starts w
            starts_with_hash += 1  # if it does, add 1 to the count

print(starts_with_hash)