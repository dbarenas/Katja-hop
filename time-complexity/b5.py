
# define quadratic time 0(N*N)
#

def quadratic(N):
  result = 0
  for i in xrange(N):
    for j in xrange(i,N):
      result += 1
    return result

print quadratic(10)
