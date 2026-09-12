"""Table de verite minimale pour relier preuve, invariant et decision."""
import unittest

def assess(observed, expected, fresh):
    return observed == expected and fresh

class InvariantTests(unittest.TestCase):
    def test_fresh_matching_observation_is_accepted(self):
        self.assertTrue(assess("base:8453", "base:8453", True))

    def test_stale_observation_is_rejected(self):
        self.assertFalse(assess("hyperevm:old", "hyperevm:old", False))

    def test_mismatching_observation_is_rejected(self):
        self.assertFalse(assess("zk:claim-7", "zk:claim-8", True))

if __name__ == "__main__":
    unittest.main()
