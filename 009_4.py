# Leetcode numero 4: Median of Two Sorted Arrays
def medianSortedArrays(nums1, nums2):
        nums = [nums1, nums2]
        nums_final = []

        for num in nums:
            for n in num:
                nums_final.append(n)
        nums_final.sort()
        
        if len(nums_final) % 2 == 0:
            posicion = int(len(nums_final)/2)
            p1 = nums_final[posicion]
            p2 = nums_final[posicion - 1]
            mediana = float((p1 + p2) / 2)
            return mediana
        else:
            posicion = int(len(nums_final)/2)
            mediana = float(nums_final[posicion])
            return mediana


nums1 = [1,2]
nums2 = [3,4]

call = medianSortedArrays(nums1, nums2)

print(call)
