import numpy as np
import matplotlib.pyplot as plt


def get_random(length):
    return np.random.random(length)


def get_baker(length):
    a = np.zeros(length)
    x = np.random.random()
    for i in range(length):
        x = x * 3.0
        x = x - int(x)
        a[i] = x
    return a


def get_xy(data):
    n = len(data) - 1
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = data[i]
        y[i] = data[i+1]
    return x,y


if __name__=='__main__':

    # generate instance
    random_instance = get_random(1000)
    baker_instance = get_baker(1000)

    normal_fig = plt.figure()

    normal_ax1 = normal_fig.add_subplot(211)
    normal_ax1.plot(random_instance, marker='.', linestyle = 'None', label='random')
    normal_ax1.set_title('Random')

    normal_ax2 = normal_fig.add_subplot(212)
    normal_ax2.plot(baker_instance, marker='.', linestyle='None', label='baker')
    normal_ax2.set_title('Baker')

    plt.show()

    # cannot tell random from baker in picture
    # even in statistical metrics
    print(f"average = {np.average(random_instance)}")
    print(f"variance = {np.var(random_instance)}")

    print(f"average = {np.average(baker_instance)}")
    print(f"variance = {np.var(baker_instance)}")


    # however, using certain transformation, we can see the difference clearly
    stepped_fig = plt.figure()

    r_x, r_y = get_xy(random_instance)
    stepped_ax1 = stepped_fig.add_subplot(211)
    stepped_ax1.plot(r_x, r_y, linestyle='None', marker='.')
    stepped_ax1.set_title("Random")
    
    b_x, b_y = get_xy(baker_instance)
    stepped_ax2 = stepped_fig.add_subplot(212)
    stepped_ax2.plot(b_x, b_y, linestyle='None', marker='.')
    stepped_ax2.set_title("Baker")

    plt.show()


