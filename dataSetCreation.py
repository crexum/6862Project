import random
import csv
import os

def generate_random_and_save_csv(num_rows, filename="tData.csv"):
    header = ["REMOTE_PORT", "LATENCY", "THROUGHPUT", "ANOMALY"]
    rows = []

    # Define reasonable ranges for random data
    common_ports = [20, 21, 22, 23, 53, 67, 68, 80, 443]
    latency_min, latency_max = 10.0, 20.0
    throughput_min, throughput_max = 10.0, 20.0
    anomaly_probability = random.uniform(.01, .1)

    for _ in range(num_rows):
        remote_port = random.choice(common_ports) # Or random.randint(1, 65535) for a wider range
        latency = round(random.uniform(latency_min, latency_max), 8) # 8 decimal places like in the example
        throughput = round(random.uniform(throughput_min, throughput_max), 8) # 8 decimal places
        anomaly = 1 if random.random() < anomaly_probability else 0
        rows.append([remote_port, latency, throughput, anomaly]) # Store as actual types, csv writer handles conversion

    try:
        # Get the directory of the script and construct the full path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the header
            csv_writer.writerow(header)

            # Write the data rows
            csv_writer.writerows(rows)
        print(f"Successfully generated '{filename}' at '{file_path}' with {num_rows} rows of data.")
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

# --- Example Usage ---
num_rows_to_generate = 3000 # Let's generate a larger dataset for training
output_filename = "validData.csv"
generate_random_and_save_csv(num_rows_to_generate, output_filename)
