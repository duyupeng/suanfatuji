class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr=[0 for i in range(1001)]
        res=[]
        for i in arr1:
            arr[i]+=1
        for i in arr2:
            if arr[i]:
                res+=[i]*arr[i]
                arr[i]=0
        for i in range(len(arr)):
            res+=[i]*arr[i]
        return res