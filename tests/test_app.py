import unittest
from password_analyzer.app import analyze_password, estimate_character_pool

class AnalyzerTests(unittest.TestCase):
    def test_empty_password(self):
        r = analyze_password("")
        self.assertEqual(r.length, 0)
        self.assertEqual(r.estimated_entropy_bits, 0.0)
    def test_common_password_flag(self):
        self.assertFalse(analyze_password("password").checks["not_common_password"])
    def test_mixed_long_scores_higher(self):
        self.assertGreater(analyze_password("River!Quartz7Cobalt").score, analyze_password("abc").score)
    def test_character_pool(self):
        self.assertEqual(estimate_character_pool("abc"), 26)
        self.assertEqual(estimate_character_pool("aA1!"), 26+26+10+32)

if __name__ == "__main__": unittest.main()
