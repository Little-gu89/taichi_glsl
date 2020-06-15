'''
GLSL-alike linear algebra helper functions / aliases.
'''

import taichi as ti


def vec(*xs):
    return ti.Vector(xs)


def mat(*xs):
    return ti.Matrix(xs)


def dot(a, b):
    '''
    Calculate the dot product of two vectors.

    `dot` returns the dot product of two vectors, i.e.,
    `x[0] * y[0] + x[1] * y[1] + ...`.

    :parameter x:
        Specifies the first of two vectors.

    :parameter y:
        Specifies the second of two vectors.

    :return:
        The return value can be calculated as `summation(a * b)`.

    :see also:
        :func:`cross`, :func:`length`, :func:`outerProduct`,
        :func:`summation`.
    '''
    return a.dot(b)


def normalize(v):
    '''
    Calculates the unit vector in the same direction as the original vector.

    `normalize` returns a vector with the same direction as its parameter,
    `v`, but with length 1.

    :parameter v:
        Specifies the vector to normalize.

    :return:
        The return value can be calculated as `v / length(v)`.

    :see also:
        :func:`dot`, :func:`length`.
    '''
    return v.normalized()


def summation(v):
    '''
    Calculate the sum of all elements in a vector.

    `summation` returns the sum of vector elements, i.e.,
    `v[0] + v[1] + ...`.

    :parameter v:
        Specifies the vector whose elements to sum up.

    :return:
        The return value is the sum of all elements in `v`.

    :see also:
        :func:`minimum`, :func:`maximum`.
    '''
    return v.sum()


def maximum(v):
    '''
    Find the maximum value in all elements of a vector.

    `maximum` returns the maximum value in vector elements, i.e.,
    `max(v[0], v[1] + ...)`.

    :parameter v:
        Specifies the vector where to find the maximum element.

    :return:
        The return value is the maximum value in vector elements.

    :see also:
        :func:`minimum`, :func:`summation`.
    '''
    return v.max()


def minimum(v):
    '''
    Find the minimum value in all elements of a vector.

    `minimum` returns the minimum value in vector elements, i.e.,
    `max(v[0], v[1] + ...)`.

    :parameter v:
        Specifies the vector where to find the minimum element.

    :return:
        The return value is the minimum value in vector elements.

    :see also:
        :func:`maximum`, :func:`summation`.
    '''
    return v.min()


def cross(a, b):
    '''
    Calculate the cross product of two vectors.
    The argument can be 2D or 3D. If 3D, the return value is 3D;
    If 2D, the return value is a scalar.
    The computation is done in a right-handed coordinate system, i.e.::

        cross(vec(1, 0, 0), vec(0, 1, 0)) == vec(0, 0, 1)
        cross(vec(1, 0), vec(0, 1)) == 1

    :parameter x:
        Specifies the first of two vectors, can be 2D or 3D.

    :parameter y:
        Specifies the second of two vectors, can be 2D or 3D.

    :return:
        The return value can be calculated as `summation(a * b)`.

    For example::

        a = vec(1, 2, 3)
        b = vec(4, 5, 6)
        c = cross(a, b)
        # c = [2*6 - 5*3, 4*3 - 1*6, 1*5 - 4*2] = [-3, 6, -3]

        p = vec(1, 2)
        q = vec(4, 5)
        r = cross(a, b)
        # r = 1*5 - 4*2 = -3
    '''
    return a.cross(b)


def outerProduct(a, b):
    return a.outer_product(b)


def length(x):
    '''
    Calculate the length of a vector.

    `length` returns the length or magnitude of the vector, i.e.,
    `sqrt(x[0] ** 2 + x[1] * 2 + ...)`.

    :parameter x:
        Specifies a vector of which to calculate the length.

    :see also:
        :func:`distance`, :func:`normalize`, :func:`dot`.
    '''
    return x.norm()


@ti.func
def distance(a, b):
    '''
    Calculate the distance between two points.

    :parameter a:
        Specifies the first of two points.

    :parameter b:
        Specifies the second of two points.

    :see also:
        :func:`length`, :func:`normalize`, :func:`dot`.
    '''
    return (a - b).norm()


def shuffle(a, *indices):
    ret = []
    for i in indices:
        t = a.subscript(i)
        ret.append(t)
    return ti.Vector(ret)
