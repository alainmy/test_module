import numpy as np

def calculate(vals):
    
    vals_counts = len(vals)
    
    if vals_counts < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(vals)
    arr = np.array([arr[:3],arr[3:6],arr[6:9]])
    
    result = {}
    result['mean'] = [np.mean(arr,axis=0),np.mean(arr,axis=1),np.mean(arr)]
    result['variance'] = [np.var(arr,axis=0),np.var(arr,axis=1),np.var(arr)]
    result['arrtandard deviation'] = [np.std(arr,axis=0),np.std(arr,axis=1),np.std(arr)]
    result['max'] = [np.max(arr,axis=0),np.max(arr,axis=1),np.max(arr)]
    result['min'] = [np.min(arr,axis=0),np.min(arr,axis=1),np.min(arr)]
    result['sum'] = [np.sum(arr,axis=0),np.sum(arr,axis=1),np.sum(arr)]
    return result