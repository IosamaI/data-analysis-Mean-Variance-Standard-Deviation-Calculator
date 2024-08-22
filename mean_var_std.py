import numpy as np 

def calculate(list_name):
    if len(list_name) != 9:
        raise ValueError("List must contain nine numbers")
    
    
    matrix = np.array(list_name).reshape(3,3)
    
    mean = [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(),matrix.mean()]
    variance= [matrix.var(axis=0).tolist(),matrix.var(axis=0),matrix.var()]
    std_dev = [matrix.std(axis=0).tolist(),matrix.std(axis=1),matrix.std()]
    max =[matrix.max(axis=0),matrix.max(axis=1),matrix.max()]
    min = [matrix.min(axis=0),matrix.min(axis=1),matrix.min()]
    sum = [matrix.sum(axis=0),matrix.sum(axis=1),matrix.sum()]
    
    
       # Prepare the result dictionary
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max,
        'min': min,
        'sum': sum
    }
    
    return result
    
    
    