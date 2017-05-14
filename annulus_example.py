import numpy as np
from univ_rand_gen import UnivRandGen


def uniform_annulus(rad_min, rad_max, num_points):
    # generates num_points uniformly distributed throughout an annulus

    #density of rad is 2r/(rad_max**2 - rad_min**2) so 
    #cdf is F(r) = (r**2 - rad_min**2) / (rad_max**2 - rad_min**2)

    theta = 2*np.pi*np.random.random((num_points,))

    def cdf(r):

        if r < rad_min:
            return 0

        elif r > rad_max:
            return 1

        else:
            return (r**2 - rad_min**2) / (rad_max**2 - rad_min**2)


    rad_gen = UnivRandGen(func = cdf, type = 'cdf')

    radius = np.array([rad_gen.random() for _ in range(num_points)])

    x = radius*np.cos(theta)
    y = radius*np.sin(theta)

    return x,y
