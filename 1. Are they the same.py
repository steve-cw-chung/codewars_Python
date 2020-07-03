""" Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure) that checks whether the two arrays have the "same" elements, with the same multiplicities. "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

Examples
Valid arrays
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements in terms of squares:

a = [121, 144, 19, 161, 19, 144, 19, 11] 
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
Invalid arrays
If we change the first number to something else, comp may not return true anymore:

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 132 is not the square of any number of a.

a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
comp(a,b) returns false because in b 36100 is not the square of any number of a.

Remarks
a or b might be [] (all languages except R, Shell).
a or b might be nil or null or None or nothing (except in Haskell, Elixir, C++, Rust, R, Shell, PureScript).
If a or b are nil (or null or None), the problem doesn't make sense so return false.

Note for C
The two arrays have the same size (> 0) given as parameter in function comp. """

# My Solution
def comp(array1, array2):
  if(array1 is None and array2 is None):
      return True
  elif(array1 is None and array2 is not None):
      return False
  elif(array1 is not None and array2 is None):
      return False
  elif(len(array1)==0 and len(array2)==0):
      return True
  else:
      while len(array1) >0 and len(array2) >0:
        arr2 = array2.copy()
        valid = False
        for j in arr2:
          if(pow(array1[0],2)==j):
            valid = True
            array1.pop(0)
            array2.remove(j)
        if(valid==True and len(array1)==0 and len(array2)==0):
          return True
        elif(valid==True):
          valid = False
        else:
          return False
      return False
# Solution 1
def comp(array1, array2)
  array1.nil? || array2.nil? ? false : array1.sort.map {|v| v ** 2} == array2.sort
end

# Solution 2 
def comp(array1, array2)
  return false if array1.nil? || array2.nil?
  array1.map {|num| num ** 2}.sort == array2.sort 
end
# Solution 3 
def comp(a, b)
  a && b ? a.sort.map {|x| x ** 2} == b.sort : false
end
# Solution 4 
def comp(array1, array2)

array1.sort.map {|num| num ** 2} == array2.sort
rescue 
false

end
