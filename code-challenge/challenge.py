""" Print out all of the numbers in the following array that are divisible by 3:
[85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]
The expected output for the above input is:
27
81
9
27
99
63
42
You may use whatever programming language you wish.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""


# Step 1 - Write a loop
def check_if_div_by_3(var):
    for x in var:
# Step 2 - Check to see if it's divisible by 3
        if x % 3 == 0:
# Step 3 - Print if true, skip if false
            print(x)

check_if_div_by_3([85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14])