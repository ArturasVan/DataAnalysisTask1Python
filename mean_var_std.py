import numpy as np

def calculate(list):
  if len(list)!=9:
     raise ValueError("List must contain nine numbers.") 
  else:
    a = np.array(list).reshape((3, 3))
    calculations = {'mean':[np.mean(a,axis=0).tolist(),np.mean(a,axis=1).tolist(),np.mean(a.flatten()).tolist()],
         'variance':[np.var(a,axis=0).tolist(),np.var(a,axis=1).tolist(),np.var(a.flatten()).tolist()],
          'standard deviation':[np.std(a,axis=0).tolist() ,np.std(a,axis=1).tolist(),np.std(a.flatten().tolist())],
         'max': [np.max(a,axis=0).tolist(),np.max(a,axis=1).tolist(),np.max(a.flatten()).tolist()],
         'min': [np.min(a,axis=0).tolist(),np.min(a,axis=1).tolist(),np.min(a.flatten()).tolist()],
         'sum': [np.sum(a,axis=0).tolist(),np.sum(a,axis=1).tolist(),np.sum(a.flatten()).tolist()]}
    return calculations