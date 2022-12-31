#that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

#The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
'''{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
'''
import numpy as np


def calculate(num_list):
    if len(num_list) == 9:

        input_arr = np.array(num_list).reshape((3, 3))
        calculations = {}
        calculations['mean'] = [input_arr.mean(
            axis=0).tolist(), input_arr.mean(
                axis=1).tolist(), input_arr.mean()]
        calculations['variance'] = [input_arr.var(
            axis=0).tolist(), input_arr.var(
                axis=1).tolist(), input_arr.var()]
        calculations['standard deviation'] = [input_arr.std(
            axis=0).tolist(), input_arr.std(
                axis=1).tolist(), input_arr.std()]
        calculations['max'] = [input_arr.max(axis=0).tolist(), input_arr.max(
            axis=1).tolist(), input_arr.max()]
        calculations['min'] = [input_arr.min(axis=0).tolist(), input_arr.min(
            axis=1).tolist(), input_arr.min()]
        calculations['sum'] = [input_arr.sum(axis=0).tolist(), input_arr.sum(
            axis=1).tolist(), input_arr.sum()]
        return calculations
    else:
      raise ValueError('List must contain nine numbers.')
        
