
def logarithmic(N):
  result = 0
  while(N > 1):
    N=N//2
    result +=1
  return result

print logarithmic(10)

