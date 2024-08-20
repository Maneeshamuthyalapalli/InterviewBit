class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        sides = [A, B, C, D]
        sides.sort()
        if sides[0]  == sides[1] and sides[2] == sides[3]:
            return 1
        else:
            return 0
