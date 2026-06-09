from nbresult import ChallengeResultTestCase


class TestRfTuning(ChallengeResultTestCase):
    def test_best_score_is_in_expected_range(self):
        self.assertGreater(self.result.best_score, -0.2)
        self.assertLess(self.result.best_score, 0.2)