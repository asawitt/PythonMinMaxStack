class StackNode:
	def __init__(self, nxt,value):
		self.next = nxt
		self.value = value
class Stack:
	def __init__(self):
		self.top = None
		self.size = 0
	def push(self,value):
		self.top = StackNode(self.top,value)
		self.size += 1
	def pop(self):
		if self.top is None:
			return None
		val = self.top.value
		self.top = self.top.next
		self.size -= 1
		return val
	def peek(self):
		if self.top is None:
			return None
		return self.top.value
	def isEmpty(self):
		return self.top is None
	def getSize(self):
		return self.size
	def display(self):
		cur=self.top
		l = []
		while not self.isEmpty():
			l.append(self.pop())
		for i in range(len(l)-1):
			print(str(l[i]),end="<--")
			self.push(l[i])
		print(str(l[len(l)-1]))
		self.push(l[len(l)-1])
		
class MinMaxStack:
	def __init__(self,min_or_max):
		self.main_stack = Stack()
		self.aux_stack = Stack()
		self.agg_func = min_or_max
	def push(self,value):
		self.main_stack.push(value)
		if self.aux_stack.isEmpty():
			self.aux_stack.push(value)
		else:
			self.aux_stack.push(self.agg_func(value,self.aux_stack.peek()))
	def pop(self):
		self.aux_stack.pop()
		return self.main_stack.pop()
	def peek(self):
		return self.main_stack.peek()
	def query(self):
		return self.aux_stack.peek()
	def getSize(self):
		return self.main_stack.getSize()
	def isEmpty(self):
		return self.main_stack.isEmpty()
	def display(self):
		print("main stack: ",end="")
		self.main_stack.display()
		print(str(self.agg_func.__name__) + " stack: ",end="")
		self.aux_stack.display()
