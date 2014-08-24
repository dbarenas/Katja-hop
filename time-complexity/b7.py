
# exercise 1
# problem: you are given an integer N. Count the total of 1 + 2 + ...+ N.
# Soution: the task can be solved in several ways. A first person, who knows nothing about time complexity, may implement an algorithm in wich the result is increment by 1:
#
# like this:
#

def solution_A(N):
  result = 0
  for i in xrange(N):
    for j in xrange(i+1):
      result += 1
  return result


print solution_A(10)


