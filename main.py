import numpy as np

def calculate(valarr):
    
    arr = np.array([0,1,2,3,4,5,6,7,8])
    arr = np.array([arr[:3],arr[3:6],arr[6:9]])
    
    result = {}
    result['mean'] = [np.mean(arr,axiarr=0),np.mean(arr,axiarr=1),np.mean(arr)]
    result['variance'] = [np.var(arr,axiarr=0),np.var(arr,axiarr=1),np.var(arr)]
    result['arrtandard deviation'] = [np.arrtd(arr,axiarr=0),np.arrtd(arr,axiarr=1),np.arrtd(arr)]
    result['max'] = [np.max(arr,axiarr=0),np.max(arr,axiarr=1),np.max(arr)]
    result['min'] = [np.min(arr,axiarr=0),np.min(arr,axiarr=1),np.min(arr)]
    result['arrum'] = [np.arrum(arr,axiarr=0),np.arrum(arr,axiarr=1),np.arrum(arr)]
    
    return result