# A  Universal Random Number Generator

The class UnivRandGen provides a random number generator with distribution determined directly from the function definition of a given cumulative distribution function (CDF).

## Example:  Generating exponentially distributed data

    import numpy as np
    from univ_rand_gen import UnivRandGen
    from matplotlib import pyplot as plt

    NUM_POINTS = 100000
    MEAN = 1.
    cdf = lambda x: 1 - np.exp(-(1./MEAN)*x)

    gen = UnivRandGen(func=cdf, type = 'cdf', seed = 0)

    data = [gen.random() for _ in range(NUM_POINTS)]

    plt.hist(data, bins = 100)

    plt.show()

![](./images/exp_dist.png)

## Example: Generating data according to a Gaussian distribution

    import numpy as np
    from univ_rand_gen import UnivRandGen
    from matplotlib import pyplot as plt
    from math import erf

    NUM_POINTS = 100000
    MEAN = 1.
    STD = 2.
    cdf = lambda x: (.5)*(1 + erf((x - MEAN) / (STD*np.sqrt(2))))   

    gen = UnivRandGen(func=cdf, type = 'cdf')

    data = [gen.random() for _ in range(NUM_POINTS)]

    plt.hist(data, bins = 100)

    plt.show()

![](./images/normal_dist.png)

## Example: Generating radii to generate points uniformly in an annulus (without rejection sampling)

We desire the density p of the radius to be `p(r) = 2r/(rad_max**2 - rad_min**2)` so the cdf should be `F(r) = (r**2 - rad_min**2) / (rad_max**2 - rad_min**2)`

    import numpy as np
    from univ_rand_gen import UnivRandGen
    from matplotlib import pyplot as plt

    RAD_MIN = 3
    RAD_MAX = 6
    NUM_POINTS = 10000

    theta = 2*np.pi*np.random.random((NUM_POINTS,))

    radius_cdf = lambda rad: 0 if rad < RAD_MIN else 1 if rad > RAD_MAX else (rad**2 - RAD_MIN**2) / (RAD_MAX**2 - RAD_MIN**2)
    rad_gen = UnivRandGen(func = radius_cdf, type = 'cdf')
    radius = np.array([rad_gen.random() for _ in range(NUM_POINTS)])

    x = radius*np.cos(theta)
    y = radius*np.sin(theta)

    plt.plot(x,y,'.')

    plt.show()

![](./images/uniform_annulus.png)

