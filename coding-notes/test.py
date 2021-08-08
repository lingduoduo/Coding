class Solution:
    def minNumber(self, nums) -> int:
        if not nums:
            return ""
        self.quickSort(nums, 0, len(nums)-1)
        return int(''.join([str(num)for num in nums]))

    def keyfunc(self, x, y):
        if int(str(x) + str(y)) <= int(str(y) + str(x)):
            return True
        else:
            return False


    # Python program for implementation of Quicksort Sort
    def partition(self, arr, low, high):
        i = (low-1)         # index of smaller element
        pivot = arr[high]     # pivot
      
        for j in range(low, high):
      
            # If current element is smaller than or
            # equal to pivot
            if self.keyfunc(arr[j],  pivot):
      
                # increment index of smaller element
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
      
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr

        if low < high:
      
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)
      
            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi-1)
            self.quickSort(arr, pi+1, high)
  
if __name__ == '__main__':
    # res = Solution().keyfunc(3, 32)
    # print(res)

    # res = Solution().quickSort([3, 32, 321], 0, 2)
    # print(res)

    res = Solution().minNumber(nums = [3, 32, 321])
    print(res)

