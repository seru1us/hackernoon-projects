# The thing that got me on this was was the instruction mentioned NOT using str methods
# Since the easy thing here would be to use my already-made "find_missing" function 
# and just join it together, I realized quickly that you can only really join an array
# of strings. sneaky bastards

# without wanting to reinvent the wheel and also keep my find_missing function, I found 
# that I could just print out each number individually instead of joining them first. 
# Credit goes to:
# https://www.geeksforgeeks.org/python-convert-a-list-of-multiple-integers-into-a-single-integer/


def find_missing(lst): 
    return [str(x) for x in range(lst[0], lst[-1]+1) if x not in lst] 

if __name__ == '__main__':
    n = int(input())
    narray = find_missing([0,n+1])
    for i in narray:
        print(i, end="")


