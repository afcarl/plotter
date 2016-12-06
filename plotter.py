import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time

class Plotter:
    def __init__(self, x, y, getter):
        self._fig = plt.figure()
        self._ax1 = self._fig.add_subplot(1, 1, 1)

        self._data_y = y
        self._data_x = x

        self._data_getter = getter

    def animate(self):
        ani = animation.FuncAnimation(self._fig, self._draw, interval=500)
        plt.show()

    def _update_data(self):
        new_val = self._data_getter.get()
        self._data_y.append(new_val)

    def _draw(self, frame):
        new_x = len(self._data_x)
        self._data_x.append(new_x)

        self._update_data()

        self._ax1.clear()
        self._ax1.plot(self._data_x, self._data_y)



if __name__ == "__main__":
    class Getter:
        def __init__(self):
            pass

        def get(self):
            return random.randint(0, 200)

    g = Getter()
    plotter = Plotter([], [], g)
    plotter.animate()

    
