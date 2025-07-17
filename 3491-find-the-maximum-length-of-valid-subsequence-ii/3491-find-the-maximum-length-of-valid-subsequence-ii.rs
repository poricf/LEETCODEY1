impl Solution {
fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
    let mut max_length = 2;

    for target_mod in 0..k {
        let mut remainder_dp = vec![0; k as usize];

        for &num in &nums {
            let num_mod = num % k;
            let required_mod = (target_mod - num_mod + k) % k;
            remainder_dp[num_mod as usize] = remainder_dp[required_mod as usize] + 1;
        }

        for &length in &remainder_dp {
            max_length = max_length.max(length);
        }
    }

    max_length
}

}