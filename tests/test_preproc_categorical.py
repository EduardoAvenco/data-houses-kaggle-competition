from nbresult import ChallengeResultTestCase


class TestPreprocCategorical(ChallengeResultTestCase):
    def test_preproc_categorical_is_pipeline(self):
        self.assertTrue(self.result.is_pipeline)

    def test_preproc_categorical_has_two_steps(self):
        self.assertEqual(self.result.n_steps, 2)

    def test_first_step_is_simple_imputer(self):
        self.assertEqual(self.result.first_step_type, "SimpleImputer")

    def test_second_step_is_one_hot_encoder(self):
        self.assertEqual(self.result.second_step_type, "OneHotEncoder")