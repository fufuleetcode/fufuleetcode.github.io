---
layout: post
title: Leetcode 973. k closest points to origin 的三种解法
categories: [难度 Middle, 主题 Divide & Conquer, 主题 Heap, 主题 Sort]
description: 
keywords: leetcode， 973
---

### Youtube 视频链接
- 本题链接: [Youtube视频本题](https://www.youtube.com/watch?v=G9VcMTSZ1Lo&feature=youtu.be)
- 我的LeetCode刷题频道是：[Youtube小小福LeetCode讲解频道](https://www.youtube.com/watch?v=XObufhWMQ1o&list=PL6i_0cc-sEeKV6TM-RJMN5H87CvzQhYJx)

### Github 代码链接
- Guihub代码链接: [Github本题解析链接](https://github.com/fufuleetcode/FufuLeetCode/blob/master/lc_973_k_closest_points_to_origin.py)

### 知识点: 
- [分治(Divide and Conquer)][]
- [堆(Heap)][]
- [排序(Sort)][]


### 本题思路分析PPT
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide1.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide2.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide3.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide4.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide5.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide6.jpeg)
* ![](/images/posts/lc-973-k-closest-points-to-origin/Slide7.jpeg)


### 本题解答代码

- Solution-1: BF Solution

```python
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        Solution-1: BF Recursion
        """
        def helper(s, curr_idx) -> bool:
                        
            if curr_idx == len(s) :
                return True
            
            N = len(s)
            
            for word in wordDict:
                                
                if len(word) <= N - curr_idx  and s[curr_idx:curr_idx+len(word)] in wordDict and helper(s,curr_idx+len(word)):
                    return True
            
            return False
        
        return helper(s, 0)
        
```


- Solution-2: Recursion with memory

```python
class Solution:


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        Solution-1: Recursion with memory
        """

        mem  = {}
        def helper(s, curr_idx) -> bool:
                        
            if curr_idx in mem:
                return mem[curr_idx]
            
            if curr_idx == len(s) :
                mem[curr_idx] = True
                return True
            
            N = len(s)
            
            for word in wordDict:
                                
                if len(word) <= N - curr_idx  and s[curr_idx:curr_idx+len(word)] in wordDict and helper(s,curr_idx+len(word)):
                    mem[curr_idx] = True
                    return True
            
            mem[curr_idx] = False
            return False
        
            
        return helper(s, 0)    

```

- Solution-3: BFS( time out limit error)

```python
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        Solution-2: BFS( time out limit error)
        """
        
        queue = collections.deque([0])
        
        while queue:
            
            idx = queue.popleft()
            
            # print(idx)
            
            if idx == len(s):
                return True
            
            for end in range(idx, len(s) ):
                
                if s[idx:end+1] in wordDict:
                    
                    queue.append(end+1)
                
        return False

```

- Solution-4: Dynamic Programming

```python
class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        """
        Solution-3: Dynamic Programming
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            if dp[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
        return dp[-1]

```


### 面试高频考点Youtube链接
- [数组(Array)][]
- [哈希表(Hash Table][]
- [链表(Linked List)][]
- [数学(Math)][]
- [链表(Linked List)][]
- [双指针(Two Pointers)][]
- [字符串(String)][]
- [二分查找(Binary Search)][]
- [分治(Divide and Conquer)][]
- [动态规划(Dynamic Programming)][]
- [回溯(Backtracking)][]
- [栈(Stack)][]
- [堆(Heap)][]
- [Greedy][]
- [排序(Sort)][]
- [Tree][]
- [Depth-first Search][]
- [Breadth-first Search][]
- [Binary Search Tree][]
- [Recursion][]
- [Queue][]
- [Sliding Window][]

### 面试低频考点Youtube链接
- [Bit Manipulation](https://www.youtube.com/playlist?list=PL6i_0cc-sEeKCSV72ZUjBBP7dY92beorD)
- [Union Find](https://www.youtube.com/playlist?list=PL6i_0cc-sEeIgu-2oOxEn_QaauIou6Bmx)
- [Graph](https://www.youtube.com/playlist?list=PL6i_0cc-sEeIjHRwoXNMihdf-_TeYXu4r)
- [Design](https://www.youtube.com/playlist?list=PL6i_0cc-sEeJbKTgIKfLqXEZ5oydICtmd)
- [Topological Sort](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLyFc8aRnPQvauzluf_jsbd)
- [Trie](https://www.youtube.com/playlist?list=PL6i_0cc-sEeIx4f8kYCd8jykTKZ72Nvbp)
- [Binary Indexed Tree](https://www.youtube.com/playlist?list=PL6i_0cc-sEeL2m5h6CVMPMARgAOP6mq3w)
- [Segment Tree](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLS1alwWhHzZOP-8vDuxLnu)
- [Brainteaser](https://www.youtube.com/playlist?list=PL6i_0cc-sEeIcZrGKD8oTEQxhOSS8SwEV)
- [Memoization](https://www.youtube.com/playlist?list=PL6i_0cc-sEeJ6AHiCA7h_YxhQ2gmh0fBq)
- [Minimax](https://www.youtube.com/playlist?list=PL6i_0cc-sEeK0r0LD4K9y8EWNYjvfb0ru)
- [Reservoir Sampling](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLribSIjAlgKgK69Blc5Erj)
- [Ordered Map](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLVGuImYCM8-ngauFxY-uAE)
- [Geometry](https://www.youtube.com/playlist?list=PL6i_0cc-sEeKXQUN0HRkRvTRHRQijFpF-)
- [Random](https://www.youtube.com/playlist?list=PL6i_0cc-sEeIx7gt5j9l9Ab0iPXIVnCO5)
- [Rejection Sampling](https://www.youtube.com/playlist?list=PL6i_0cc-sEeJpI51nLhgvNxlXXMG0uvZ2)
- [Line Sweep](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLCf-yZvoViY-2mGLE2Pn4o)
- [Rolling Hash](https://www.youtube.com/playlist?list=PL6i_0cc-sEeJnANBdS-HxDWljnMa-_NE1)
- [Suffix Array](https://www.youtube.com/playlist?list=PL6i_0cc-sEeLiBNJvqCqlRCelM80qOMUx)






[数组(Array)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLy4CiDaPWIikuIqpEk9OFD
[哈希表(Hash Table]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKeNWNT8rhYou264_pKtHov
[链表(Linked List)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeI9YS7CcAG4YqCH3eInxT8t
[数学(Math)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJYXF6Z69ommaw1YelF9BXM
[链表(Linked List)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeI9YS7CcAG4YqCH3eInxT8t
[双指针(Two Pointers)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJz13nHm-Um8kzSYOvxi9Aq
[字符串(String)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJQT3nRiniO4Iw0C574QicD
[二分查找(Binary Search)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeITbHxpAP1MbTM-YuvyNO1W
[分治(Divide and Conquer)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKUfDm-qjLzM1v5GtJ4fm_b
[动态规划(Dynamic Programming)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeL6HkIg8KfofcsMfnLmey94
[回溯(Backtracking)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJ3O8PUrlGUnw32J9pPavnm
[栈(Stack)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeI1h0DendVsj5-t7P3V_AK0
[堆(Heap)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLR3TqRiInw5kAr1S3IidtD
[Greedy]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIWZxARM194QDuiXvp6CqZI
[排序(Sort)]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKcFACiLPger-8AVkcVw3z9
[Tree]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJFh6AFYT2g5jHViPKL9Da_
[Depth-first Search]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJ_V0sMsrEKkdUOM567oeNM
[Breadth-first Search]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLerHCt2Vnb1TUVpjVu-9kB
[Binary Search Tree]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIHwobNSz9z39MmtN03OHJq
[Recursion]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKuA5YbeSeEmGQ6Sz-zhzRD
[Queue]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJkCqfdOlK59EUqtPvXSf6A
[Sliding Window]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLwGC1TVEbFK3Zr0gAEGvTG
[Bit Manipulation]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKCSV72ZUjBBP7dY92beorD
[Union Find]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIgu-2oOxEn_QaauIou6Bmx
[Graph]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIjHRwoXNMihdf-_TeYXu4r
[Design]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJbKTgIKfLqXEZ5oydICtmd
[Topological Sort]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLyFc8aRnPQvauzluf_jsbd
[Trie]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIx4f8kYCd8jykTKZ72Nvbp
[Binary Indexed Tree]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeL2m5h6CVMPMARgAOP6mq3w
[Segment Tree]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLS1alwWhHzZOP-8vDuxLnu
[Brainteaser]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIcZrGKD8oTEQxhOSS8SwEV
[Memoization]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJ6AHiCA7h_YxhQ2gmh0fBq
[Minimax]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeK0r0LD4K9y8EWNYjvfb0ru
[Reservoir Sampling]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLribSIjAlgKgK69Blc5Erj
[Ordered Map]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLVGuImYCM8-ngauFxY-uAE
[Geometry]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeKXQUN0HRkRvTRHRQijFpF-
[Random]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeIx7gt5j9l9Ab0iPXIVnCO5
[Rejection Sampling]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJpI51nLhgvNxlXXMG0uvZ2
[Line Sweep]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLCf-yZvoViY-2mGLE2Pn4o
[Rolling Hash]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeJnANBdS-HxDWljnMa-_NE1
[Suffix Array]:https://www.youtube.com/playlist?list=PL6i_0cc-sEeLiBNJvqCqlRCelM80qOMUx