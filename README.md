# B-Cubed Metrics

<div style="text-align: justify">
A simple Python package to calculate B-Cubed precision, recall, and F1-score for clustering evaluation.
</div>

## What are B-Cubed Metrics
<div style="text-align: justify">
The B-Cubed algorithm was first introduced by Bagga, A. and Baldwin B. (1998) in their paper on Entity-Based Cross-Document Coreferencing Using the Vector Space Model. The algorithm compares a predicted clustering with a ground truth (or gold standard) clustering through element-wise precision and recall scores. For each element, the predicted and ground truth clusters containing the element are compared, and then the mean over all elements is taken. The B-Cubed algorithm can be useful in unsupervised techniques where the cluster labels are not available, because unlike macro-averaged metrics, it focuses on element-wise operations.
</div>

<div style="text-align: justify">
From the paper, two simple equations were devised calculating precision and recall scores for the predicted clustering:
</div>

$$
Precision = \frac{1}{\sum {elements}}\sum_{i=1}^n {\frac{(count \; of \; element)^2}{count \; of \; all \; elements \; in \; cluster}}
$$

$$
Recall = \frac{1}{\sum {elements}}\sum_{i=1}^n {\frac{(count \; of \; element)^2}{count \; of \; total \; elements \; from \; this \; category}}
$$

$$
F-score = \frac{1}{k}\sum_{i=1}^n {\frac{2\times Precision(C)_k \times Recall(C)_k}{Precision(C)_k + Recall(C)_k}}
$$

<div style="text-align: justify">

where $n$ above denotes the number of categories in the cluster and $k$ is the number of predicted clusters. $Precision(C)_k$ and $Recall(C)_k$ are the 'partial' precision and recalls for each cluster. 
</div>


## Installation and Use
<div style="text-align: justify">
Download the package from any terminal using:
</div>

```bash
pip install bcubed-metrics
```
<div style="text-align: justify">
To use the B-Cubed class you need to import it and provide 2 dictionaries - one for the predicted clustering, and one for the ground truth clustering (actual labels):
</div>

```python
from bcubed_metrics.bcubed import Bcubed

predicted_clustering = [
            {'blue': 4, 'red': 2, 'green': 1},
            {'blue': 2, 'red': 2, 'green': 3},
            {'blue': 1, 'red': 5},
            {'blue': 1, 'red': 2, 'green': 3}
        ]

ground_truth_clustering = {'blue': 8, 'red': 11, 'green': 7}

bcubed = Bcubed(predicted_clustering=predicted_clustering, ground_truth_clustering=ground_truth_clustering)

metrics = bcubed.get_metrics() # returns all metrics as dictionary

bcubed.print_metrics() # prints all metrics
```