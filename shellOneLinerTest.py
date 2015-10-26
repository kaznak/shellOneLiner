
import shellOneLiner,csv

def head(iter, n):
	x = iter.__iter__()
	i = 0
	while i < n :
		print x.next()
		i = i + 1

class list2iter:
	
	def __init__(self, list):
		self.list = list
	
	def __iter__(self):
		return self
	
	def next(self):
		if   len(self.list) > 1:
			head = self.list[0]
			self.list = self.list[1:]
			return head
		elif len(self.list) == 1:
			head = self.list[0]
			self.list = []
			return head
		elif len(self.list) < 1:
			raise StopIteration('end of list')

li = list2iter(range(1,10))
[ v for v in li ]



# Test 1-1: count
ol = shellOneLiner.ShellOneLiner('self 1.1.6 sample-data | count 1 1')
print [v for v in ol]


# Test 1-2: count
reader = csv.reader(open('sample-data', 'rb'), delimiter=' ')
ol = shellOneLiner.ShellOneLiner('self 1.1.6 | count 1 1',input=reader)
print [v for v in ol]


# Test 1-3: count
reader = csv.reader(open('sample-data', 'rb'), delimiter=' ')
ol = shellOneLiner.ShellOneLiner('self 1.1.6 | count 1 1',input=reader, outfile='tmp')
print list(ol)
of = csv.reader(open('tmp', 'rb'), delimiter=' ')
print [v for v in of]


# Test 2-1: getlast
reader = csv.reader(open('sample-data', 'rb'), delimiter=' ')
ol = shellOneLiner.ShellOneLiner('self 1.1.6 1 2 | LANG=C sort -k1,3 -n | getlast key=1 | delf 1',input=reader)
print [v for v in ol]

# Test 2-2: getlast
reader = csv.reader(open('sample-data', 'rb'), delimiter=' ')
ol = shellOneLiner.ShellOneLiner('self 1.1.6 1 2 | LANG=C sort -k1,3 -n | getlast key=1 | delf 1',input=reader, outfile='tmp')
print [v for v in ol]
of = csv.reader(open('tmp', 'rb'), delimiter=' ')
print [v for v in of]



# Test 1-1: count
ol = shellOneLiner.ShellOneLiner('dmerge key=1 set_A set_B set_C')
print [v for v in ol]



