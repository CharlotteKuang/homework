from RegularExpression import ReParser

rp4 = ReParser('(c|d)')
rp4.buildTree()
print rp4.pattern 
rp4.printTree()

rp4 = ReParser('(a)*(c|d)')
rp4.buildTree()
print rp4.pattern 
rp4.printTree()

rp4 = ReParser('(a)*cd')
rp4.buildTree()
print rp4.pattern 
rp4.printTree()

rp5 = ReParser('a(b*)cd')
rp5.buildTree()
print rp5.pattern
rp5.printTree()

rp0 = ReParser('a(b*(c|e))d')
rp0.buildTree()
print rp0.pattern
rp0.printTree()

rp0 = ReParser('a(b|c)d')
rp0.buildTree()
print rp0.pattern 
rp0.printTree()

rp = ReParser('a|b')
rp.buildTree()
print rp.pattern
rp.printTree()

rp = ReParser('a**b')
rp.buildTree()
print rp.pattern
rp.printTree()

rp1 = ReParser('ab')
rp1.buildTree()
print rp1.pattern
rp1.printTree()

rp2 = ReParser('abcd')
rp2.buildTree()
print rp2.pattern
rp2.printTree() 

rp3 = ReParser('a(bc)d')
rp3.buildTree()
print rp3.pattern 
rp2.printTree() 

rp4 = ReParser('ab*cd')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('a*cd')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('(ab|dc)*cd')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('(ab|dc)*c|d')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('c|dccccccccccc')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('c|(dccccc*cccccc)')
rp4.buildTree()
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('c|d((c))*')
tree = rp4.buildTree() 
print rp4.pattern 
rp4.printTree() 

rp4 = ReParser('c|d(c|bc)')
tree = rp4.buildTree() 
print rp4.pattern 
rp4.printTree() 
