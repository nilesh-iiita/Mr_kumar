#!/usr/bin/python
import random
N=5
mat =[[random.random() for x in xrange(N)] for y in xrange(N)] ## random matrix genration of N X N
print '\n###### original Matrix ########\n'
def prt_mat(M): ## function to print matrix
	for i in M:
		for j in i:
			print j,
		print 
prt_mat(mat)
print '\n############## croped matrix #############\n'
def crop(mat,m,n,i,j): # cropping function
	if m+i > len(mat) or n+j > len(mat[0]):exit('Error !!\nIndex out of range')
	t1,t2 = [],[]
	for x in xrange(i,m+i):
		for y in xrange(j,n+j):
			t1.append(mat[x][y])
			#print mat[x][y],
		t2.append([t1])
		t1 = []
		#print
	#print t2
	c_mat = t2
	prt_mat(c_mat)

crop(mat,3,3,0,0)

print '''

####################################################
function "crop(mat,3,3,0,0)" takes input as
crop(mat,m,n,i,j) where :
		mat = matrix (input original)
		m X n = diminsition of new croped matrix
		i,j = reference orgin for corping.
'''
