from nbresult import ChallengeResultTestCase


class TestRfPipe(ChallengeResultTestCase):
    def test_rf_pipe_is_pipeline(self):
        self.assertTrue(self.result.is_pipeline)

    def test_rf_pipe_has_two_steps(self):
        self.assertEqual(self.result.n_steps, 2)

    def test_model_is_random_forest_regressor(self):
        self.assertEqual(self.result.model_type, "RandomForestRegressor")