#using the hastable
def hasha(a,b):
    n=set(a)
    for nums in b:
        if nums not in n:
            return False
    return True

if __name__=="__main__":
  a = [11, 1, 13, 21, 3, 7]
  b = [11, 3, 7, 1,2]

  if hasha(a, b):
      print("true")
  else:
      print("false")