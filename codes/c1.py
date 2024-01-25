import matplotlib.pyplot as plt

# Define the specific values of n
n_values = [20, 19, 18, 16]
x_values = [21 - n for n in n_values]

# Create a stem plot for the specified values
plt.stem(n_values, x_values, linefmt='-', markerfmt='o', basefmt=' ')

# Add labels and title
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Plot for x(n) = 21 - n at n=20, 19, 18, 16')
plt.savefig('f1.png')
# Display the plot
plt.show()
