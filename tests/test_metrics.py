import unittest
from bcubed_metrics.bcubed import Bcubed

class TestBCubed(unittest.TestCase):
    def test_bcubed_metrics(self):
        predicted_clustering = [
            {'blue': 4, 'red': 2, 'green': 1},
            {'blue': 2, 'red': 2, 'green': 3},
            {'blue': 1, 'red': 5},
            {'blue': 1, 'red': 2, 'green': 3}
        ]

        ground_truth_clustering = {'blue': 8, 'red': 11, 'green': 7}

        bcubed = Bcubed(predicted_clustering=predicted_clustering, ground_truth_clustering=ground_truth_clustering)
        metrics = bcubed.get_metrics()
        bcubed.print_metrics()
        
        self.assertAlmostEqual(metrics['precision'], 0.4652, places=4)
        self.assertAlmostEqual(metrics['recall'], 0.33954, places=4)
        self.assertAlmostEqual(metrics['f1_score'], 0.38716, places=4)
        self.assertAlmostEqual(metrics['micro_f1_score'], 0.39256, places=4)

if __name__ == "__main__":
    unittest.main()