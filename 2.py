i = result = 0
a, b = 1, 2
while i < 27:
    # if b > 4000000:
    #     break

    # print a

    if (i % 2) == 0:
        # print "yang genap", a
        result += b

    a, b = b, a+b
    i += 1

print result