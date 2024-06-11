# def hillvalley(l):
#     asc, desc = False, False
#     slope = 0
#     if len(l) < 3:
#         return False
#     for i in range(len(l) - 1):  # loop stops at 2nd last index
#         if slope > 1:
#             return False
#         current = l[i]
#         next_element = l[i + 1]
#         diff = next_element - current
#         if diff > 0:
#             if desc:
#                 slope += 1
#             asc = True
#             desc = False
#         elif diff < 0:
#             if asc:
#                 slope += 1
#             desc = True
#             asc = False
#     if slope == 1:
#         return True
#     return False
#
#
# print(hillvalley([1, 2, 3, 5, 4]))
#
# print(hillvalley([1, 2, 3, 4, 5]))
#
# print(hillvalley([5, 4, 1, 2, 3]))
#
# print(hillvalley([5, 4, 3, 2, 1]))
#
# print(hillvalley([1, 2, 3, 5, 4, 3, 2, 1]))
#
# print(hillvalley([1, 2, 3, 4, 5, 3, 2, 4, 5, 3, 2, 1]))
#
# print(hillvalley([9, 5, 4, -1, -2, 3, 7]))
#
# print(hillvalley([5, 4, 3, 2, 1, 0, -1, -2, -3]))

def ascending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] < l[1] and ascending(l[1:]))

def descending(l):
    if len(l) <= 1:
        return(True)
    else:
        return(l[0] > l[1] and descending(l[1:]))

def hill(l):
    for i in range(1,len(l)-1):
        if ascending(l[:i+1]) and descending(l[i:]):
            return(True)
    return(False)

def valley(l):
    for i in range(1,len(l)-1):
        if descending(l[:i+1]) and ascending(l[i:]):
            return(True)
    return(False)

def hillvalley(l):
    return(hill(l) or valley(l))