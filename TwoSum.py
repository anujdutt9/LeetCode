# Two Sum
# Find the index of two numbers such that they add to a target value without using any number twice.


# In this approach, we traverse the list/array twice.
# One traversal using the for loop and the other using a[i+1:].
# So, Time Complexity:
# For Loop: O(N)
# a[i+1:] : N-1 elements => O(N)
# Total Time Complexity: O(N^2)
def twoSum(a,t):
    # O(N)
    for i in range(len(a)):
        # O(N)
        if (t - a[i]) in a[i+1:]:
            return [i,a.index(t - a[i])]



# In this approach, we use dictionary instead of an inner loop a[i+1:]
# Hash Table/Dictionary Time Complexity: O(1)
# For Loop: O(N) Time Complexity
# Total Time Complexity: O(N)
def TwoSum(a,t):
    d = {}
    # O(N)
    for i in range(len(a)):
        # O(1)
        if a[i] in d:
            return [d[a[i]],i]
        else:
            d[t - a[i]] = i



a = [1,2,5,7,9,10]
target = 6
print(twoSum(a,target))
print('\n')
print(TwoSum(a,target))