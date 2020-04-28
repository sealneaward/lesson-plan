def toaster(bread):
  toast = None
  if toast == 'white':
    print('You are not allowed to eat this Neil')
  elif toast == 'brown':
    print('Good decision Neil')
  else:
    print('What are you putting in the toaster? What is wrong with you?')
  return toast

bread = 'white'
toast = toaster(bread)
print('Toast type: %s' % (toast))