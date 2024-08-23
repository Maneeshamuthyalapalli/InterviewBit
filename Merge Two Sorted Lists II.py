class Solution:
	# @param A : list of integers
	# @param B : list of integers
	def merge(self, A, B):
        A.extend(B)
        A.sort()
   
