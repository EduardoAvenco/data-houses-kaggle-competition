from nbresult import ChallengeResultTestCase


class TestBaselineScore(ChallengeResultTestCase):
    def test_baseline_score_is_in_expected_range(self):
        self.assertGreater(self.result.baseline_score, -0.25)
        self.assertLess(self.result.baseline_score, 0.25)