
 #
 #
 #https://codility.com/c/run/demoYUAKSY-UCS
#
# A small frog wants to get to the other side of the road. The frog is currently located at i
# position X and wants to get to a position greater than or equal to Y. 
# The small frog always jumps a fixed distance, D.
# Count the minimal number of jumps that the small frog must perform to reach its target.
#
#


def solution(X, Y, D):
  res=0
  cont=0
  for i in range(D,Y+D,D):
      res+=X+i
      cont += 1
  return cont

print solution(11,18,13)
