#Solution 1 : Brute Force - Use Counter
class MajorityChecker: 
    def __init__(self, nums): 
        self.nums = nums
    
    def query(left, right, threshold): 
        subarray = nums[left : right]
        ctr = Counter(subarray)
        elem, freq = ctr.most_common(1)[0]
        return elem if freq > threshold else -1 

#Solution 2 : 
#Approach : Dynamic Programming / Sliding Window / Segment Tree
#left, right - maximum element upto left, max element upto right

#TODO: See the 3 C++ Solutoins, vboioiiooioiooi