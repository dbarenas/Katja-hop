
# example liear time 2
#
def linear2(N,M):
  result = 0
  for i in xrange(N):
    result += i
  for j in xrange(M):
    result += j
  return result

print linear2(2,2)
print "* "*20
print linear2(1,2)
