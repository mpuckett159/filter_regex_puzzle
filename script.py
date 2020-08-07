import re
import itertools

with open('words_alpha.txt','r') as file:
    words = file.readlines()

words = [x.strip() for x in words]

reg_1 = r'.*[hack]+[the]*.*[planet]*.*'
reg_2 = r'.*[hack]*[the]*.*[planet]+.*'
reg_3 = r'^.?.?.?.?.?.?.?.?$'
reg_4 = r'^...........*$'
reg_5 = r'.*(.)...\1.*'
reg_6 = r'.*[exfedbadge].*'

# 8 or less letter words
reg_list_8 = [reg_1,reg_2,reg_3,reg_5,reg_6]
# 10+ letter words
reg_list_10 = [reg_1,reg_2,reg_4,reg_5,reg_6]

# All permutations for the 8 letter ones
perms_8 = list(itertools.permutations(reg_list_8,5))
# All permutations for the 10 letter ones
perms_10 = list(itertools.permutations(reg_list_10,5))

# Run through for 8 letter words
interesting_lists_8 = []
for perm in perms_8:
    filter_words = words
    for reg in perm:
        filter_words = list(filter(lambda x: re.search(reg,x),filter_words))
    if len(filter_words) < 1000:
        interesting_lists_8.append(filter_words)

interesting_lists_10 = []
for perm in perms_10:
    filter_words = words
    for reg in perm:
        filter_words = list(filter(lambda x: re.search(reg,x),filter_words))
    if len(filter_words) < 1000:
        interesting_lists_10.append(filter_words)
