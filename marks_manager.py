marks=[]
n=int(input("how many marks"))
for i in range(n):
  m=int(input(f"enter mark {i+1}:"))
  marks.append(m)
  print("marks list:",marks)
  print("total:",sum(marks))
  print("average:",sum(marks)/len(marks))
  print("highest:",max(marks))
  print("lowest:",min(marks))
