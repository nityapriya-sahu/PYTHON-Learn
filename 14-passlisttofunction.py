list = [20,15,14,63,18,12,89,61,74,80]

def count(item):
    even = 0
    odd = 0
    for i in item:
        if i%2 == 0:
            even +=1
        else:
            odd+=1

    return even,odd

# print(count(list))

# OR
even, odd = count(list)
print('Even: {} and Odd: {}'.format(even, odd))


# --------------------------------------------------
# ASSIGNMENT

# Print the name which length is more than 5 from array

memberlist = ['modi', 'trump', 'zelensky', 'putin', 'xi ping', 'macron', 'stalin',]

def countstr(item):
    value = []
    for x in item:
        if len(x) >5:
            value.append(x)

    return value

result = countstr(memberlist)
print(result)