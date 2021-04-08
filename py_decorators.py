def deco(func):
  def new_func(val1, val2):
    return func(int(val1) + int(val2))
  return new_func

@deco
def concat(val1, val2):
  return val1+val2
