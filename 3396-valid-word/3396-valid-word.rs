impl Solution {
    pub fn is_valid(word: String) -> bool {
        // Rule 1: Check if the length is at least 3
        if word.len() < 3 {
            return false;
        }

        // Define sets for vowels and valid characters
        let vowels = "aeiouAEIOU";
        let mut has_vowel = false;
        let mut has_consonant = false;

        for ch in word.chars() {
            // Rule 2: Must be only digits and letters
            if !ch.is_ascii_alphanumeric() {
                return false;
            }

            // Check if it's a letter
            if ch.is_ascii_alphabetic() {
                if vowels.contains(ch) {
                    has_vowel = true;
                } else {
                    has_consonant = true;
                }
            }
        }

        // Rule 3 and 4: Must have at least one vowel and one consonant
        has_vowel && has_consonant
    }
}
