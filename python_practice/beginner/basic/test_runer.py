# write a funciton to take in a given string and a substring
# calciulate the number of occurances in the string
# ex ABCDCDC ->CDC = 2 occurances

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count
print(count_substring('abcdcdc','cdc'))