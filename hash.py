import random

def test():
    random_data = []
    hash_data =[]
    for i in range(0,100000):
		random_data.append(random.randint(0,10000))

    for i in random_data:
		print hash_data.append(i%100)


    result_data = set(hash_data)
    for item in result_data:
    	print("The %d has found %d" %(item,hash_data.count(item)))


if __name__ == '__main__':
	test()

