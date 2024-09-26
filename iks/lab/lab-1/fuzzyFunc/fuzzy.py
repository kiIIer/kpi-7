import numpy as np
import matplotlib.pyplot as plt


# Define the updated function for y
def y_function(x):
    return np.sin(x) * np.cos(x / 2 + np.sin(x))


# Define the updated function for z
def z_function(x, y):
    return x * np.cos(x + y)


x_high_res = np.linspace(0, 10, 1000)
y_high_res = y_function(x_high_res)
z_high_res = z_function(x_high_res, y_high_res)


def plot_xyz():
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

    # Plot x vs y
    ax1.plot(x_high_res, y_high_res, label="y(x)")
    ax1.set_title("y vs x")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.grid(True)

    # Plot x vs z
    ax2.plot(x_high_res, z_high_res, label="z(x)")
    ax2.set_title("z vs x")
    ax2.set_xlabel("x")
    ax2.set_ylabel("z")
    ax2.grid(True)

    # Plot x
    ax3.plot(x_high_res, label="x")
    ax3.set_title("x vs Index")
    ax3.set_xlabel("Index")
    ax3.set_ylabel("x")
    ax3.grid(True)

    # Show the plots in a single window
    plt.tight_layout()
    plt.show()


plot_xyz()


# Triangular membership function
def triangular_mf(a, b, c):
    epsilon = 1e-6  # Small value to prevent division by zero
    return lambda x: np.maximum(np.minimum((x - a) / (b - a + epsilon), (c - x) / (c - b + epsilon)), 0)


# Trapezoidal membership function
def trapezoidal_mf(a, b, c, d):
    return lambda x: np.maximum(np.minimum(np.minimum((x - a) / (b - a), 1), (d - x) / (d - c)), 0)


# Gaussian membership function
def gaussian_mf(mean, sigma):
    return lambda x: np.exp(-((x - mean) ** 2) / (2 * sigma ** 2))


def plot_mem():
    triangular = triangular_mf(2, 5, 8)
    trapezoidal = trapezoidal_mf(2, 4, 6, 8)
    gaussian = gaussian_mf(5, 1)

    plt.figure(figsize=(10, 6))

    # Plot triangular membership function
    plt.plot(x_high_res, triangular(x_high_res), label='Triangular MF', linestyle='--')

    # Plot trapezoidal membership function
    plt.plot(x_high_res, trapezoidal(x_high_res), label='Trapezoidal MF', linestyle='-.')

    # Plot gaussian membership function
    plt.plot(x_high_res, gaussian(x_high_res), label='Gaussian MF', linestyle='-')

    # Add labels and title
    plt.title("Membership Functions (High Resolution)")
    plt.xlabel("x")
    plt.ylabel("Membership Degree")
    plt.legend()
    plt.grid(True)

    plt.show()


plot_mem()


def generate_membership_functions(lower_bound, upper_bound, count, mf_type):
    x = np.linspace(lower_bound, upper_bound, 1000)
    membership_functions = []
    step = (upper_bound - lower_bound) / (count - 1)

    for i in range(count):
        center = lower_bound + i * step

        if mf_type == 'triangular':
            # Make triangles wider by increasing the overlap between functions
            a = center - step if i > 0 else lower_bound
            c = center + step if i < count - 1 else upper_bound
            mf = triangular_mf(a, center, c)

        elif mf_type == 'trapezoidal':
            # Make trapezoids narrower by reducing the width of the top part
            a = center - (step / 1.5)
            b = center - (step / 3)  # Narrow the top
            c = center + (step / 3)  # Narrow the top
            d = center + (step / 1.5)
            mf = trapezoidal_mf(a, b, c, d)

        elif mf_type == 'gaussian':
            sigma = step / 2
            mf = gaussian_mf(center, sigma)

        else:
            raise ValueError(
                "Invalid membership function type. Choose from 'triangular', 'trapezoidal', or 'gaussian'.")

        membership_functions.append(mf)

    return x, membership_functions


# Plot the generated membership functions
def plot_membership_functions(x, membership_functions, title):
    plt.figure(figsize=(10, 6))

    for i, mf in enumerate(membership_functions):
        plt.plot(x, mf(x), label=f'mx{i + 1}')

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("Membership Degree")
    plt.legend()
    plt.grid(True)
    plt.show()


def pick_f(membership_functions, value_index):
    scores = np.array([mf(value_index) for mf in membership_functions])
    max_index = np.argmax(scores)
    return max_index


def print_funcs():
    lower_bound = 0
    upper_bound = 10
    function_count = 10

    x, membership_functions_tr = generate_membership_functions(lower_bound, upper_bound, function_count, 'triangular')
    x, membership_functions_pz = generate_membership_functions(lower_bound, upper_bound, function_count, 'trapezoidal')
    x, membership_functions_gu = generate_membership_functions(lower_bound, upper_bound, function_count, 'gaussian')
    plot_membership_functions(x, membership_functions_tr,
                              f"Generated Triangular Membership Functions ({function_count})")

    plot_membership_functions(x, membership_functions_pz,
                              f"Generated Trapezoidal Membership Functions ({function_count})")
    plot_membership_functions(x, membership_functions_gu,
                              f"Generated Gaussian Membership Functions ({function_count})")


print_funcs()

x_min = 0
x_max = 10
y_min, y_max = np.min(y_high_res), np.max(y_high_res)
z_min, z_max = np.min(z_high_res), np.max(z_high_res)

print(f"y(x) minimum: {y_min}, y(x) maximum: {y_max}")
print(f"z(x) minimum: {z_min}, z(x) maximum: {z_max}")


def generate_rule_set(x_values, x_mf, y_mf, z_mf):
    rule_set = {}
    for i, x in enumerate(x_values):
        y_value = y_function(x)
        z_value = z_function(x, y_value)

        x_index = pick_f(x_mf, x)
        y_index = pick_f(y_mf, y_value)
        z_index = pick_f(z_mf, z_value)

        rule_set[(x_index, y_index)] = z_index

    return rule_set


def pretty_print_rule_set(rule_set):
    for key, value in rule_set.items():
        x_index, y_index = key
        print(f"Rule: x index {x_index}, y index {y_index} -> z index {value}")


def evaluate_rule_set_simple(rule_set, x_value, x_mf, y_mf, z_min, z_max, f_count):
    # Step 1: Calculate y(x)
    y_value = y_function(x_value)

    # Step 2: Find the index of the membership function for x and y
    x_index = int(pick_f(x_mf, x_value))  # Find index of best x membership function
    y_index = int(pick_f(y_mf, y_value))  # Find index of best y membership function

    # Step 3: Look up the rule set for the corresponding x and y indices
    if (x_index, y_index) in rule_set:
        z_index = rule_set[(x_index, y_index)]  # Get the z membership function index
    else:
        raise ValueError(f"No rule found for x index {x_index} and y index {y_index}")

    # Step 4: Return the middle value of the z membership function
    step = (z_max - z_min) / (f_count - 1)
    z_value = z_min + z_index * step + step / 2  # Middle value of the z membership function
    return z_value


def plot_fuzzy_vs_normal_z(x_values, rule_set, x_mf, y_mf, z_min, z_max, f_count):
    # Step 1: Calculate normal z values using the z_function
    normal_z_values = z_function(x_values, y_function(x_values))

    # Step 2: Calculate fuzzy z values using the rule set
    fuzzy_z_values = []
    absolute_errors = []

    for x_value in x_values:
        try:
            fuzzy_z = evaluate_rule_set_simple(rule_set, x_value, x_mf, y_mf, z_min, z_max, f_count)
        except ValueError:
            fuzzy_z = np.nan  # In case there's no rule, return NaN

        # Append fuzzy z value
        fuzzy_z_values.append(fuzzy_z)

        # Calculate the absolute error between fuzzy and normal z values
        normal_z = z_function(x_value, y_function(x_value))
        absolute_errors.append(abs(fuzzy_z - normal_z))

    # Step 3: Plot the fuzzy z and normal z values
    plt.figure(figsize=(10, 6))

    # Plot normal z values
    plt.plot(x_values, normal_z_values, label='Normal z(x)', linestyle='-', color='blue')

    # Plot fuzzy z values
    plt.plot(x_values, fuzzy_z_values, label='Fuzzy z(x)', linestyle='--', color='red')

    # Add labels and title
    plt.title("Fuzzy z(x) vs Normal z(x)")
    plt.xlabel("x")
    plt.ylabel("z")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

    # Step 4: Plot the error between fuzzy and normal z values
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, absolute_errors, label="Error |Fuzzy z - Normal z|", linestyle='-', color='green')
    plt.title("Absolute Error between Fuzzy z(x) and Normal z(x)")
    plt.xlabel("x")
    plt.ylabel("Absolute Error")
    plt.grid(True)
    plt.show()

    # Step 5: Calculate the integral of the error (area under the curve)
    total_error_integral = np.trapezoid(absolute_errors, x_values)
    print(f"Integral of absolute error: {total_error_integral:.4f}")


f_count = 15
_, membership_functions_x = generate_membership_functions(x_min, x_max, f_count, 'triangular')
_, membership_functions_y = generate_membership_functions(y_min, y_max, f_count,
                                                          'triangular')
_, membership_functions_z = generate_membership_functions(z_min, z_max, f_count,
                                                          'triangular')

rule_set = generate_rule_set(x_high_res, membership_functions_x, membership_functions_y, membership_functions_z)
pretty_print_rule_set(rule_set)
plot_fuzzy_vs_normal_z(x_high_res, rule_set, membership_functions_x, membership_functions_y, z_min, z_max, f_count)

_, membership_functions_x = generate_membership_functions(x_min, x_max, f_count, 'trapezoidal')
_, membership_functions_y = generate_membership_functions(y_min, y_max, f_count,
                                                          'trapezoidal')
_, membership_functions_z = generate_membership_functions(z_min, z_max, f_count,
                                                          'trapezoidal')

rule_set = generate_rule_set(x_high_res, membership_functions_x, membership_functions_y, membership_functions_z)
plot_fuzzy_vs_normal_z(x_high_res, rule_set, membership_functions_x, membership_functions_y, z_min, z_max, f_count)

_, membership_functions_x = generate_membership_functions(x_min, x_max, f_count, 'gaussian')
_, membership_functions_y = generate_membership_functions(y_min, y_max, f_count,
                                                          'gaussian')
_, membership_functions_z = generate_membership_functions(z_min, z_max, f_count,
                                                          'gaussian')

rule_set = generate_rule_set(x_high_res, membership_functions_x, membership_functions_y, membership_functions_z)
plot_fuzzy_vs_normal_z(x_high_res, rule_set, membership_functions_x, membership_functions_y, z_min, z_max, f_count)

