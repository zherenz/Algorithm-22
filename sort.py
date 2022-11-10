# bubble sort O(N^2)
class BubbleSort:
    def bubbleSort(lst):
        n = len(lst)
        if n <= 1:
            return lst
        for i in range (0,n):
            for j in range(0, n - i - 1):
                if lst[j]>lst[j + 1]:
                    (lst[j], lst[j + 1])=(lst[j + 1], lst[j])
        return lst


# quick sort Time: O(nlogn) -> average   O(n^2) -> worst [1|2 3 4 5]
class QuickSort: 
    def sortIntegers(self, A): 
        if A == None or len(A) == 0: 
            return 
        self.quickSort(A, 0, len(A) - 1) 
         
    def quickSort(self, A, start, end): 
        if start >= end: 
            return 
         
        left, right = start, end 
        pivot = A[(start + end) // 2] 
         
        while left <= right: 
            while left <= right and A[left] < pivot: 
                left += 1 
            while left <= right and A[right] > pivot: 
                right -= 1 
                 
            if left <= right: 
                A[left], A[right] = A[right], A[left] 
                left += 1 
                right -= 1 
                 
        self.quickSort(A, start, right) 
        self.quickSort(A, left, end)
        

# merge sort O(nlogn)
class MergeSort:        
    def mergesort(self, seq):
        """归并排序"""
        if len(seq) <= 1:
            return seq
        mid = len(seq) / 2  # 将列表分成更小的两个列表
        # 分别对左右两个列表进行处理，分别返回两个排序好的列表
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        # 对排序好的两个列表合并，产生一个新的排序好的列表
        return self.merge(left, right)

    def merge(self, left, right):
        """合并两个已排序好的列表，产生一个新的已排序好的列表"""
        result = []  # 新的已排序好的列表
        i = 0  # 下标
        j = 0
        # 对两个列表中的元素 两两对比。
        # 将最小的元素，放到result中，并对当前列表下标加1
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result