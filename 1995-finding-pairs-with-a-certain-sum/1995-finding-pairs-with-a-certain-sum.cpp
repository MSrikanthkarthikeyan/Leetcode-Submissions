class FindSumPairs {
public:
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        this->nums1 = nums1;
        this->nums2 = nums2;
        for (int num : nums2) {
            frequencyMap[num]++;
        }
    }

    void add(int index, int val) {
        int oldValue = nums2[index];
        nums2[index] += val;
        frequencyMap[oldValue]--;
        frequencyMap[nums2[index]]++;
    }

    int count(int tot) {
        int count = 0;
        for (int num : nums1) {
            int target = tot - num;
            count += frequencyMap[target];
        }
        return count;
    }

private:
    vector<int> nums1, nums2;
    unordered_map<int,int> frequencyMap;
};