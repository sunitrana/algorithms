import random

def bubble_sort(items):
	for i in range(len(items)):
		for j in range(len(items)-1-i):
			if items[j] > items[j+1]:
				items[j], items[j+1] = items[j+1], items[j]

if __name__ == '__main__':
	list_items = [random.randint(-50, 100) for c in range(10)]
	print 'List before sorting -> ', list_items
	bubble_sort(list_items)
	print 'List after soritng -> ', list_items