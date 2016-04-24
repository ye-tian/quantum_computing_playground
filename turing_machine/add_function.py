__author__ = "Ye Tian"
__email__ = "ye.tian@avira.com"
__license__ = "GPL"

# m + n using Turing Automata

'''
 rules
 5 status    : s1, s2, s3, s4, s5 => s = {1,2,3,4,0}, where 0 = H (halt)
 2 values    : 1, b => 1, 0
 3 directions: stop, l, r => 0, 1, 2

 convert decimal to unary and use unary system to work with Turing Automata

 +-----------------------------------+
 | s    a | s_new   a_new   direction|
 +-----------------------------------+
 | s1   b | s2      b       l        |
 | s2   b | s3      b       l        |
 | s2   1 | s2      1       l        |
 | s3   b | H       b       0        |
 | s3   1 | s4      b       r        |
 | s4   b | s2      1       l        |
 +-----------------------------------+

 Initial state:

 bb11...1b11...1bb
 ---------------^-
                s1
'''
def f(s, a):
    if (s == 1 and a == 0):
        return (2, 0, 1)
    elif (s == 2 and a == 0):
        return (3, 0, 1)
    elif (s == 2 and a == 1):
        return (2, 1, 1)
    elif (s == 3 and a == 0):
        return (0, 0, 0)
    elif (s == 3 and a == 1):
        return (4, 0, 2)
    elif (s == 4 and a == 0):
        return (2, 1, 1)
    else:
        return (-1, -1, -1) # error

# convert decimal to unary
# assume d is integer ONLY, thus no more check
def convert(d):
    if type(d) == int:
        return list(map(int, "1" * d))
    return [0]

# create tap
def map_to_tap(a, b):
    r = [0, 0]
    r.extend(convert(a))
    r.extend([0])
    r.extend(convert(b))
    r.extend([0, 0])
    return r

# do add
def add(a, b):
    tap = map_to_tap(a, b)

    # initialize state
    # including state and position (starts from 0)
    s = 1
    p = len(tap) - 2
    a = tap[p]

    finished = False

    while not finished:
        r = f(s, a)

        (s_new, a_new, d) = r

        # update state and value at p on the tap
        s = s_new
        tap[p] = a_new

        # print out how it works
        print (tap)

        # move
        if d == 1: # to left
            p -= 1
        elif d == 2: # to right
            p += 1
        else:
            finished = True # stops when halt, d == 0

        # read new value from the tap
        a = tap[p]

    # generate result | verify the result
    # verify by calculating 1 from the first 1 and stopping when meets a 0
    # if Automata goes wrong, the sum will be wrong of the script will get an error
    # use the "Dumm" way of doing counting

    # get position of the left boundary
    left_boundary = -1
    for i in range(0, len(tap)):
        v = tap[i]
        if v == 1:
            left_boundary = i
            break

    # get position of the right boundary
    right_boundary = - 1
    for i in range(left_boundary, len(tap)):
        v = tap[i]
        if v == 0:
            right_boundary = i
            break

    # generate the result
    final_result = 0
    sub_tap = tap[left_boundary:right_boundary]

    for i in sub_tap:
        final_result += i

    return final_result


if __name__ == "__main__":
    print (add(47, 8))