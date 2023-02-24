"""
Use the k-nearest neighbors algorithm to return the k nearest neighbors of the provided features.

These features are the result of a dimensionality reduction by PCA on some operating-system data related to processes and their intrusivity in some network. You'll have access to an EXAMPLES dictionary, mapping each process identifier "pid_i" to a respective dictionary containing its associated features as well as a label representing whether the relevant process was intrusive to the network. A label of 0 means that it wasn't intrusive, while a label of 1 means that it was intrusive.

Below is an example portion of the EXAMPLES:

{
  "pid_0": {
    "features": [3.968642003034218, 3.9553899901567955, 3.8067717105202794, # ... more words],
    "is_intrusive": 0,
  }, 
  "pid_1": {
    "features": [3.905930716908446, 3.9843869514613046, 3.999386668299634, # ... more words],
    "is_intrusive": 0,
  }, 
  # ...
  # More of the same kind of data.
  "pid_500": {
    "features": [4.309361217767318, 4.287392829732823, 4.296809382863873, # ... more words],
    "is_intrusive": 1,
  },
  "pid_501": {
    "features": [4.310938448487633, 4.298506635010131, 4.256964230013101, # ... more words],
    "is_intrusive": 1,
  },
  # ...
  # More of the same kind of data.
}
"""

def predict_label(examples, features, k, label_key="is_intrusive"):
    dist_dict = find_k_nearest_neighbors(examples,features,k)
    labels = [examples[pid][label_key] for pid in dist_dict]

    return round(sum(labels)/k)

def find_k_nearest_neighbors(examples, features, k):
    d = {} 
    for pid,feat in examples.items():
        dist = calculateEuclidean(features,feat)
        d[pid]=dist

    knn = sorted(d,key = d.get)[:k]
    return knn

def calculateEuclidean(features, feat):
    exp_features = feat["features"]
    dist = 0

    for i in range(len(features)):
        dist += ((exp_features[i]-features[i])**2)

    return dist**0.5
