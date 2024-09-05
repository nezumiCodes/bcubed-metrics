class Bcubed():
    """
    Class to calculate Bcubed precision, recall, and F1-score for clustering evaluation.
    
    Attributes:
        predicted_clustering (list): A list of dictionaries representing the predicted clustering.
        ground_truth_clustering (dict): A dictionary representing the ground truth clustering.
        decimals (int): Number of decimal places to round the results.
    """
    
    def __init__(self, predicted_clustering=None, ground_truth_clustering=None, decimals=5):
        """
        Initialises the Bcubed object with predicted clustering and ground truth data.
        
        Args:
            predicted_clustering (list): A list of dictionaries representing the predicted clustering.
            ground_truth_clustering (dict): A dictionary representing the ground truth clustering.
            decimals (int): Number of decimal places to round the results (default is 5).
        """
        self.predicted_clustering = predicted_clustering
        self.ground_truth_clustering = ground_truth_clustering
        self.decimals = decimals
        
        self.total_precision = 0
        self.total_recall = 0
        self.total_f1 = 0
        self.total_items = sum(sum(cluster.values()) for cluster in self.predicted_clustering) # count of all cluster items
        
        self.bcubed_precision = 0
        self.bcubed_recall = 0
        self.bcubed_f1 = 0
        self.bcubed_f1_micro = 0
        
        self.calculate_metrics()
        # self.print_metrics()
            
    def calculate_metrics(self):
        """
        Calculate Bcubed precision, recall, and F1-score based on the predicted clustering 
        and ground truth data.
        """
        for cluster in self.predicted_clustering:
            cluster_total = sum(cluster.values())
            for item, count in cluster.items():
                true_total = self.ground_truth_clustering[item]
                
                precision = count / cluster_total
                recall = count / true_total
                f1 = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0
                            
                self.bcubed_precision += precision * count
                self.bcubed_recall += recall * count
                self.bcubed_f1 += f1 * count

        self.bcubed_precision = self.bcubed_precision / self.total_items
        self.bcubed_recall = self.bcubed_recall / self.total_items
        self.bcubed_f1 = self.bcubed_f1 / self.total_items
        self.bcubed_f1_micro = 2*self.bcubed_precision*self.bcubed_recall / (self.bcubed_precision + self.bcubed_recall)
    
    def get_metrics(self):
        """
        Returns the calculated Bcubed metrics as a dictionary.
        
        Returns:
            dict: A dictionary containing the precision, recall, F1-score, and micro F1-score.
        """
        return {
            'precision': round(self.bcubed_precision, self.decimals),
            'recall': round(self.bcubed_recall, self.decimals),
            'f1_score': round(self.bcubed_f1, self.decimals),
            'micro_f1_score': round(self.bcubed_f1_micro, self.decimals),
        }
    
    
    def print_metrics(self):
        """
        Print the calculated Bcubed metrics: precision, recall, F1-score, and micro F1-score.
        """
        print('BCubed Metrics\n--------------------------------')
        print(f'Precision: {round(self.bcubed_precision, self.decimals)}')
        print(f'Recall: {round(self.bcubed_recall, self.decimals)}')
        print(f'F1-score: {round(self.bcubed_f1, self.decimals)}')
        print(f'Micro F1-score: {round(self.bcubed_f1_micro, self.decimals)}')

def main():
    Bcubed(predicted_clustering={}, ground_truth_clustering={})

if __name__ == '__main__':
    main()