cpdef int factorial(int n):
    cdef int result = 1
    for i in range(2, n + 1):
        result *= i
    return result