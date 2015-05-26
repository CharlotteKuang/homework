import pdb

class _Const():
	def TYPE_OP(self):
		return 0
	def TYPE_CHAR(self):
		return 1
	def TYPE_RE(self):
		return 2

CONST = _Const()

class ReTreeNode:
	def __init__(self, type, op=''):
		self.childrens = [] # 'exp o exp' or 'r o' 
		self.type = type
		self.op = op 

class ReParser:
	def __init__(self, p):
		self.pattern = p
		self.tree = None

	def __fixPattern(self):
		symbols = ['*', '|', '(', ')']
		addDotRules = [
			lambda s, i: not s[i] in symbols and (not s[i+1] in symbols or s[i+1] == '('),
			lambda s, i: s[i] == ')' and (s[i+1] == '(' or not s[i+1] in symbols),
			lambda s, i: s[i] == '*' and s[i+1] != ')',
		]
		duplicateResules = [
			lambda s, i: s[i] == '*' and s[i+1] == '*'
		] 
		tmp = self.pattern
		#add a pair of parethese make no need to pop
		#the operands left in the stack.
		result = ['('] 
		for i in range(len(tmp)-1):
			flag = False
			for f in duplicateResules:
				if f(tmp, i):
					flag = True
					break
			if flag: continue
			result.append(tmp[i])
			for f in addDotRules:
				if f(tmp, i):
					result.append('.')
					break
		result.append(tmp[-1])
		result.append(')')
		self.pattern = ''.join(result)
	
	def __makeBinaryRe(self, re1, op, re2):		
		node = ReTreeNode(CONST.TYPE_RE())
		node.childrens.insert(0, re1)
		node.childrens.insert(0, ReTreeNode(CONST.TYPE_OP(), op))
		node.childrens.insert(0, re2)
		return node 

	def __makeSingleRe(self, re, op):
		node = ReTreeNode(CONST.TYPE_RE()) 
		node.childrens.insert(0, ReTreeNode(CONST.TYPE_OP(), op))
		node.childrens.insert(0, re)
		return node 

	def __makeCharRe(self, char):
		node = ReTreeNode(CONST.TYPE_CHAR())
		node.childrens = char
		return node 

	def buildTree(self):
		opStack = []
		treeStack = []
		opPriority = {'*': 2, '.': 1, '|': 0}
		binaryOp = ['|', '.']
		singleOp = ['*']
		self.__fixPattern() 
		for char in self.pattern:
			#pdb.set_trace()
			if 'a' <= char <= 'z' or 'A' <= char <= 'Z': 
				node = self.__makeCharRe(char)
				treeStack.append(node)
			if char == '(':
				opStack.append(char)
			if char == ')':
				while opStack[-1] != '(':
					if opStack[-1] in binaryOp:
						node = self.__makeBinaryRe(treeStack.pop(-1), opStack[-1], treeStack.pop(-1))
					if opStack[-1] in singleOp:
						node = self.__makeSingleRe(treeStack.pop(-1), opStack[-1])
					treeStack.append(node)
					opStack.pop(-1) 
				opStack.pop(-1)
			if char in opPriority:
				if len(opStack) > 0:
					topOp = opStack[-1]
					if topOp != '(' and opPriority[char] <= opPriority[topOp]: 
						if topOp in binaryOp:
							node = self.__makeBinaryRe(treeStack.pop(-1), topOp, treeStack.pop(-1))
						if topOp in singleOp:
							node = self.__makeSingleRe(treeStack.pop(-1), topOp)
						treeStack.append(node)
						opStack.pop(-1)
				opStack.append(char)
		self.tree = treeStack.pop() 

	def __recursivePrintTree(self, father):
		if father is None:
			return self.__recursivePrintTree(self.tree)
		for child in father.childrens:
			if child.type == CONST.TYPE_CHAR():
				print (father, child.childrens)
			if child.type == CONST.TYPE_OP():
				print (father, child.op)
			if child.type == CONST.TYPE_RE():
				print (father, child)
				self.__recursivePrintTree(child)

	def printTree(self):
		self.__recursivePrintTree(None)
