import numpy as np

def calculate(list):
    if (len(list)) != 9:
      raise ValueError("List must contain nine numbers.")
    else:  
      Array = np.array(list)
      Array = np.reshape(Array,(3,3))
      calculations = {
                  'mean': [np.mean(Array,axis=0).tolist(), np.mean(Array,axis=1).tolist(), np.mean(Array).tolist()],
                  'variance': [np.var(Array,axis=0).tolist(), np.var(Array,axis=1).tolist(), np.var(Array).tolist()],
                  'standard deviation': [np.std(Array,axis=0).tolist(), np.std(Array,axis=1).tolist(), np.std(Array).tolist()],
                  'max': [np.max(Array,axis=0).tolist(), np.max(Array,axis=1).tolist(), np.max(Array).tolist()],
                  'min': [np.min(Array,axis=0).tolist(), np.min(Array,axis=1).tolist(), np.min(Array).tolist()],
                  'sum': [np.sum(Array,axis=0).tolist(), np.sum(Array,axis=1).tolist(), np.sum(Array).tolist()]
}
    return calculations 