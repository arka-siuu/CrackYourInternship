class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = nums.size();
        int freq[n];
        memset(freq,0,sizeof(freq));
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
        }
        for(int i=0;i<n;i++){
            if(freq[i]>1)
            return i;
        }
        return 0;
    }
};