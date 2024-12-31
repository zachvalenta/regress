import random
import numpy as np
from uniplot import plot

def generate_data(n_days=100, seed=42):
    """Generate synthetic tea orders based on temperature.
    >>> temps, orders = generate_data(5)
    >>> len(temps) == len(orders) == 5
    True
    """
    random.seed(seed)
    # Generate temperatures between 15-35°C
    temps = [random.uniform(15, 35) for _ in range(n_days)]
    # Generate orders with some correlation to temp + noise
    orders = [20 + 2 * temp + random.gauss(0, 10) for temp in temps]
    return temps, orders

def fit_line(x, y):
    """Simple linear regression using numpy.
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([2, 4, 6])
    >>> m, b = fit_line(x, y)
    >>> abs(m - 2) < 0.001  # Should be close to 2
    True
    """
    x, y = np.array(x), np.array(y)
    m = np.cov(x, y)[0,1] / np.var(x)
    b = np.mean(y) - m * np.mean(x)
    return m, b

def main():
    # Generate data
    temps, orders = generate_data()
    # Fit line
    m, b = fit_line(temps, orders)
    # Create points for regression line
    x_line = [min(temps), max(temps)]
    y_line = [m * x + b for x in x_line]
    # Plot scatter
    print("\nTemperature vs Tea Orders:")
    print("X-axis: Temperature (°C)")
    print("Y-axis: Tea Orders")
    plot(
        xs=temps,
        ys=orders,
    )
    # Plot regression line
    plot(
        xs=x_line,
        ys=y_line,
        lines=[(0,1)],  # Draw line between first and second point
    )
    print(f"\nRegression line: Orders = {m:.1f} * Temperature + {b:.1f}")

if __name__ == "__main__":
    main()