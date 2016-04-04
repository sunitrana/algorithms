def selection_sort(list):
	for i in range(len(list)):
		min = i
		for j in range(i+1, len(list)):
			if list[min] > list[j]:
				min  = j
		if i != min:
			list[i], list[min]	= list[min],list[i]

if __name__ == '__main__':
	list = [12,45,23,98,78,12,566,-1,-2,0,-99,45,3,6]
	print list
	selection_sort(list)
	print list