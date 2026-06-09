from nbresult import ChallengeResultTestCase


class TestPreprocPipe(ChallengeResultTestCase):
    def test_preproc_pipe_is_column_transformer(self):
        self.assertTrue(self.result.is_column_transformer)

    def test_preproc_pipe_has_two_transformers(self):
        self.assertEqual(self.result.n_transformers, 2)