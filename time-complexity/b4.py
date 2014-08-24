
#
#
#Linear time

def linear(N,A):
  for i in xrange(N):
    if A[i] == 0:
      return 0
    return 1

print linear(9,[10,3,5,7,12,43])
