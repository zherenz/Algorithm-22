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
        

    # use last element as the pivot
    def partition(self, arr, low, high): 
        i = low
        pivot = arr[high]     
        for j in range(low, high): 
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
    
        arr[i], arr[high] = arr[high], arr[i] 
        return i
    
    def quickSort2(self, arr, low, high): 
        if low < high: 
            pi = self.partition(arr, low, high) 
            self.quickSort2(arr, low, pi - 1) 
            self.quickSort2(arr, pi + 1, high) 
                    

# merge sort O(nlogn)
class MergeSort:        
    def mergesort(self, seq):
        if len(seq) <= 1:
            return seq
        mid = len(seq) // 2
        left = self.mergesort(seq[:mid])
        right = self.mergesort(seq[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
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
    
    
if __name__ == "__main__":
    
    qsort = QuickSort()
    arr = [10, 7, 8, 9, 1, 5]
    qsort.quickSort2(arr, 0, len(arr) - 1)
    print(arr)