# Day 4: python fundamental

#operators
#membership operator


def is_banned(comment): 
    comment_lower = comment.lower()  # lower is used because python is case sensitive the word 'Free' is different from 'free' so we convert the comment to lower case to avoid this issue
                                    # issue :a spammer use different case and bypass the filter
    if ('free' in comment_lower or              
        'click here' in comment_lower or 
        'prizes' in comment_lower or 
        'win' in comment_lower):
        return 'comment is banned'
        
    return 'comment approved'

print(is_banned('click here to win a free prize'))
print(is_banned('this is a normal comment'))

#bitwise operator

print(5 & 2) # bitwise AND

write_permission=3
player_permission=6
if write_permission & player_permission:
    print('you can write to the file')
else:
    print('you cannot write to the file')

#bitwise shift operator
print(5 << 2)   # left shift
print(5 >> 2)   # right shift

#notes
"""
   exponent ** and BITWISE NOT,AND,OR,XOR are higher procedance to DMAS also BITWISE NOT .
   but bitwise shift << and >> are lower procedance to DMAS.
   comparison is lower procedance to DMAS but higher procedance to logical operator.
   AND operator is higher than OR.
   OR is lower than DMAS.
"""
print(4 or 15 or 8)
#Since the first value is True, the or operator doesn't care what comes next. Even if the next numbers are 15, 8, or a million, a single True makes the whole statement true.
print(4 & 15 & 8)
#and check all if all one that give true if one become 0 that give false
