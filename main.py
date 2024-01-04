import simulate_pi
import plot_simulated_points
import plot_relative_error

###### INPUT ######
number_of_simulated_points = 10**4
###################

# Simulate Pi #
pi, x_inside, y_inside, x_outside, y_outside = simulate_pi.main(number_of_simulated_points)
print(pi[-1])

# Plot Simulated Points #
plot_simulated_points.main(x_inside, y_inside, x_outside, y_outside)

# Plot Relative Error
plot_relative_error.main(pi,number_of_simulated_points)