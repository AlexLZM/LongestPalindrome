def longestPalindrome(s):
     
    # 'aba' -> '~#a#b#a#$' to make sure expansion will not pass the end of s + 1 
    # and we can map back index of T to index of s with //2 operation
    T = '#'.join('~'+s+'$')
    
    N = len(T) # N = 2 * len(s) + 3
    radius = [0] * N
    center = rightBound = 0 # current right most palindrome center and its rightbound
    
    for i in range(1, N - 1): # i is current processing index, which is at right of the current center
        iMirror = 2*center - i # left mirror of i as per current center
        diff = rightBound - i
        if diff > 0: # i is within the current right bound, so we can know its radius is at least same as its left mirror but it can not exceed the right bound
            radius[i] = min(diff, radius[iMirror])
        else:
            radius[i] = 0
        
        # try to expend the palindrome at i
        while T[i - 1 - radius[i]] == T[i + 1 + radius[i]]:
            radius[i] += 1
            
        if i + radius[i] > rightBound: # i is the most right palindrome, update center and rightBound
            center, rightBound = i, i + radius[i]
        
        
    max_i = max(range(N), key=lambda x: radius[x])
    max_r = radius[max_i]
    
    return s[(max_i - max_r) // 2: (max_i + max_r) // 2] # extract the corrosponding substring from s
        
    
