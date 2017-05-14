import random
import numpy as np

class UnivRandGen(object):
    
    def __init__(self, func, type = 'icdf', seed = 0):

        if type == 'icdf':
            self._icdf = func
        elif type == 'cdf':
            self._icdf = invert_cdf(func)
        elif type == 'pdf':
            raise NotImplementedError("pdf support not yet implemented")
        else:
            raise ValueError("Function type {} not understood.".format(type))

            #self._icdf = invert_cdf(pdf_to_cdf(func))

        self._rand_gen = random.Random(seed)

    
    def random(self):
        return self._icdf(self._rand_gen.random())


def invert_cdf(cdf, init_step = 1., granularity = .000001):

    #Returns an approximation to the inverse of a continuous monotonic non-decreasing function

    def inverse_cdf(p, granularity = granularity):

        assert 0 <= p <= 1, "p is not a probability"

        x = 0
        step = init_step

        if cdf(x) < p:
            while cdf(x) < p:
                minim = x
                x += step
                step *= 2
            maxim = x
        else:
            while cdf(x) >= p:
                maxim = x
                x -= step
                step *= 2
            minim = x

        return bin_search_func(p, cdf, minim, maxim, granularity)

    return inverse_cdf

def bin_search_func(p, cdf, minim, maxim, granularity):
    #assumes cdf(minim) < p <= cdf(maxim)
    assert minim < maxim, "Minimum must be less than maximum."
    assert cdf(minim) < p <= cdf(maxim), "Must have cdf(minim) < p <= cdf(maxim)."
    while True:

        if maxim <  minim + granularity:
            return maxim
        else:
            cut = (maxim + minim)/2.
            if p <= cdf(cut):
                maxim = cut
            else:
                minim = cut
