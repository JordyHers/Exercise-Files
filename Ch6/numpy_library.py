import numpy as np


def main():
    # Print the version
    print("numpy version: {}".format(np.__version__))
    np_array = a = np.array([1, 2, 3, 4, 5])

    print("create array from a list:")
    print(np_array)

    np_array = a = np.array((6, 7, 8, 9, 10))
    print("create array from a tuple:")
    print(np_array)
    np_shape = np_array.shape
    print("one-dimension array shape, 5 elements:")
    print(np_shape)
    np_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("two-dimensions array:")
    print(np_array)
    np_shape = np_array.shape
    print("two-dimensions array shape, 2 rows and 5 columns:")
    print(np_shape)
    np_array = a = np.array((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    np_reshape = np_array.reshape(5, 2)
    print("returns the array with a modified shape, 5 rows and 2 columns:")
    print(np_reshape)
    np_dim = np_array.ndim
    print("array dimensions:")
    print(np_dim)
    np_size = np_array.size
    print("array size: column number x row number:")
    print(np_size)
    np_dtype = np_array.dtype
    print("data type of the elements in the array:")
    print(np_dtype)
    np_itemsize = np_array.itemsize
    print("the size in bytes of each element of the array:")
    print(np_itemsize)
    np_data = np_array.data
    print("the buffer containing the actual elements of the array.don't need it for calculations")
    print(np_data)
    array_1 = np.array([1, 2, 3, 4, 5])
    array_2 = np.array([6, 7, 8, 9, 10])
    array_result = array_1 + array_2
    print("addition operation:")
    print(array_result)
    array_result = array_1 - array_2
    print("subtraction operation:")
    print(array_result)
    array_result = array_2 - array_1
    print("subtraction operation:")
    print(array_result)
    array_result = array_1 * array_2
    print("multiplication operation:")
    print(array_result)
    array_result = array_1 / array_2
    print("division operation:")
    print(array_result)
    np_corrcoef = np.corrcoef(array_1, array_2)
    print("pearson product-moment correlation coefficients")
    print(np_corrcoef)
    np_mean = np.mean(array_1)
    print("arithmetic mean:")
    print(np_mean)
    np_average = np.average(array_1)
    print("weighted average:")
    print(np_average)
    np_std = np.std(array_1)
    print("standard deviation:")
    print(np_std)
    np_median = np.median(array_1)
    print("median:")
    print(np_median)
    np_variance = np.var(array_1)
    print("variance:")
    print(np_variance)
    np_min = np.min(array_1)
    print("minimum:")
    print(np_min)
    np_max = np.max(array_1)
    print("maximum:")
    print(np_max)
    np_summa = np.sum(array_1)
    print("summa:")
    print(np_summa)


if __name__ == '__main__':

    main()
