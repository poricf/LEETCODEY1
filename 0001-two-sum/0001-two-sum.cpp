class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> seen;

        for(int i = 0 ; i<nums.size() ; i++){
            int r = target - nums[i];
            if(seen.find(r) != seen.end()){
                return{seen[r] , i };
            }
            seen[nums[i]] = i; 
            }
            
        return {};

    }
};