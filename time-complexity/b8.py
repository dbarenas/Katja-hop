
#
#Solution B a b7
# time complexity O(n)
#
#

def solution_B(N):
  result = 0
  for i in xrange(N):
    result += (i+1)
  return result

print solution_B(10)
