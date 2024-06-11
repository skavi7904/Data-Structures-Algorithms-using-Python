# def repfree(s):
#     x = True
#     list1 = []
#     for i in s:
#         if i not in list1:
#             list1.append(i)
#         else:
#             x = False
#     return x

# def repfree(s):
#     seen_characters = set()
#     for char in s:
#         if char in seen_characters:
#             return False  # If the character is already seen, there's a repetition
#         seen_characters.add(char)  # Add the character to the set
#     return True  # If no repetitions are found, return True

# def repfree(s):
#     set1 = set()
#     for i in s:
#         if i in set1:
#             return False
#         set1.add(i)
#     return True
#
# print(repfree('kj'))

def repfree(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return(False)
    return(True)