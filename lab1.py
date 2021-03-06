
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError

   maxind = 0
   for i in range(1,len(int_list)):
      if int_list[i] > int_list[maxind]:
         maxind = i
   return int_list[maxind]



def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None:
      raise ValueError
   if len(int_list) == 0:
      return ([])
   else:
      return (reverse_rec(int_list[1:]) + [int_list[0]])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   

   if int_list == None:
      raise ValueError

   if len(int_list) > 0:
      if low - high <= 0:        
         mid = (low + high)//2
         if int_list[mid] == target:
            return mid
         elif int_list[mid] < target:
            return bin_search(target, mid+1, high, int_list)
         elif int_list[mid] > target:
            return bin_search(target, low, mid-1, int_list)
      return None
   #return None
      
 








    