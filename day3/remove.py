test_list = [5, 6, 4, [], 2, [], [], [], 9]

print ("The Oringinal list is:" + str(test_list))

res = [ele for ele in test_list if ele != []]

print ("list after empty list removal :" + str(res))

