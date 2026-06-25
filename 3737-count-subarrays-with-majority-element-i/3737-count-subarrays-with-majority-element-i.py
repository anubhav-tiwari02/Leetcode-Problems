class Solution:
    def countMajoritySubarrays(self, nums, target):
        prefix=[0]
        total=0

        for num in nums:
            if num==target:
                total+=1
            else:
                total-=1
            prefix.append(total)

        def merge_sort(left,right):
            if right-left<=1:
                return 0

            mid=(left+right)//2
            ans=merge_sort(left,mid)+merge_sort(mid,right)

            j=mid
            for i in range(left,mid):
                while j<right and prefix[j]<=prefix[i]:
                    j+=1
                ans+=right-j

            temp=[]
            i=left
            j=mid

            while i<mid and j<right:
                if prefix[i]<=prefix[j]:
                    temp.append(prefix[i])
                    i+=1
                else:
                    temp.append(prefix[j])
                    j+=1

            while i<mid:
                temp.append(prefix[i])
                i+=1

            while j<right:
                temp.append(prefix[j])
                j+=1

            prefix[left:right]=temp
            return ans

        return merge_sort(0,len(prefix))