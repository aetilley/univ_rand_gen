from univ_rand_gen import UnivRandGen


def gen_lin_separable(N, m, b):
    #Generates 2 sets of N points separable by y = mx + b

    x_pos = np.random.uniform(-10, 10, N)
    x_neg = np.random.uniform(-10, 10, N)

    delta_pos = np.random.uniform(low = 0.0, high = 20.0, size = N)
    delta_neg = np.random.uniform(low = 0.0, high = 20.0, size = N)

    y_pos = (m*x_pos + b) + delta_pos
    y_neg = (m*x_neg + b) - delta_neg
    
    return x_pos, y_pos, x_neg, y_neg



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
