import random

def selection_sort(list_items):
	for i in range(len(list_items)):
		min = i
		for j in range(i+1, len(list_items)):
			if list_items[min] > list_items[j]:
				min  = j
		if i != min:
			list_items[i], list_items[min] = list_items[min],list_items[i]

if __name__ == '__main__':
	list_items = [random.randint(-50, 100) for c in range(10)]
	print 'List before sorting  -> ', list_items
	selection_sort(list_items)
	print 'List after soritng -> ', list_items