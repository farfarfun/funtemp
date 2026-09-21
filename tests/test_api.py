import unittest

import funtemp


class TestPublicApi(unittest.TestCase):
    def test_version(self):
        self.assertEqual(funtemp.__version__, "0.0.2")


if __name__ == "__main__":
    unittest.main()
