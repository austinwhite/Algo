// Time: O(n) where n is the length of n
// Space: O(n) where n is the length of n
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hm = HashMap::new();
        for (i, &val) in nums.iter().enumerate() {
            let look = target - val;
            if let Some(&j) = hm.get(&look) {
                return vec![i as i32, j];
            }
            hm.insert(val, i as i32);
        }
        return vec![];
    }
}
