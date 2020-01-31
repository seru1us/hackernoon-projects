# THIS SHOULDN'T RUN. Here is why my original was bad.
# I had a ton of different if/else statements that returned booleans... 
# one of the tests was screwing up, so after making a lot of my own tests (below) I 
# discovered this guy's post:
# https://www.hackerrank.com/challenges/write-a-function/forum/comments/215243
# I like the simplicity of this solution.

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

leapYearList = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
notLeapYearList = [1905, 1906, 1907, 1909, 1910, 1911, 1913, 1914, 1915, 1917, 1918, 1919, 1921, 1922]

for year in leapYearList:
    result = str(is_leap(year)) + " " + str(year)
    print(result)

def find_missing(lst): 
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst] 

print("lol")