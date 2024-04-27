num_of_js = 5
def pattern1(num_of_js):
    for i in range(num_of_js, 0, -1):
        for j in range(i):
             print(i, end = " ")
        print("\n")
pattern1(num_of_js)

