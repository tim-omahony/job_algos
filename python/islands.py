def numIslands(chart):
  if len(chart) == 0:
      return 0

  n = len(chart)
  m = len(chart[0])
  ans = 0
  for i in range(n):
      for j in range(m):
        if chart[i][j] == 1:
            ans+=1
        # make_water(i,j,n,m,chart)
  return ans

def make_water(i,j,n,m,chart):
  if i<0 or j<0 or i>=n or j>=m:
      return
  if chart[i][j] == 0:
      return
  else:
      chart[i][j]=0

  # make_water(i+1,j,n,m,chart)
  # make_water(i,j+1,n,m,chart)
  # make_water(i-1,j,n,m,chart)
  # make_water(i,j-1,n,m,chart)
  

sea = [ 
  [0,0,1,1,1],
  [1,1,1,0,0],
  [0,0,0,0,1],
  [1,1,0,0,0],
  [1,1,1,0,1]
]
print(numIslands(sea))
