from nbresult import ChallengeResultTestCase


class TestBaselinePipe(ChallengeResultTestCase):
    def test_baseline_pipe_is_pipeline(self):
        self.assertTrue(self.result.is_pipeline)

    def test_baseline_pipe_has_two_steps(self):
        self.assertEqual(self.result.n_steps, 2)

    def test_model_is_linear_regression(self):
        self.assertEqual(self.result.model_type, "LinearRegression")