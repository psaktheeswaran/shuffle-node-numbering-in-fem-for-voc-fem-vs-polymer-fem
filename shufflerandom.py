import csv
import random

# Input CSV file and output CSV file
input_file = '/home/josva/Music/node numbering example/Dogbone_Tension.input'
output_file = 'shuffled_output.csv'

# Read the CSV file into a list
data = []
with open(input_file, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

# Define the range you want to shuffle (B1431:E2728)
start_row = 1430  # Adjust for 0-based indexing
end_row = 2727  # Adjust for 0-based indexing
start_col = 1  # Column B

# Shuffle the values within the specified range
shuffled_data = data.copy()
for row in range(start_row, end_row + 1):
    for col in range(start_col, start_col + 4):  # 4 columns (B to E)
        # Generate a random row and column within the range
        random_row = random.randint(start_row, end_row)
        random_col = random.randint(start_col, start_col + 3)  # 3 columns (B to E)

        # Swap the values between the current cell and the randomly selected cell
        shuffled_data[row][col], shuffled_data[random_row][random_col] = shuffled_data[random_row][random_col], shuffled_data[row][col]

# Write the shuffled data to a new CSV file
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(shuffled_data)

print(f"Shuffled data saved to {output_file}")

