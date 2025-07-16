import random
import csv
import os

def generateCSV(num_rows, fileName):
    header = ["REMOTE_PORT", "LATENCY", "THROUGHPUT", "ANOMALY"]
    rows = []

    # This is the parameters for the testData.csv file
    # trainData used an anomaly_probability of .01
    # validData used an anomaly_probability of .05
    ports = [20, 21, 22, 23, 53, 67, 68, 80, 443]
    latency_min, latency_max = 10.0, 20.0
    throughput_min, throughput_max = 10.0, 20.0
    anomaly_probability = random.uniform(.01, .1)

    for _ in range(num_rows):
        remote_port = random.choice(ports)
        latency = round(random.uniform(latency_min, latency_max), 8)
        throughput = round(random.uniform(throughput_min, throughput_max), 8)
        anomaly = 1 if random.random() < anomaly_probability else 0
        rows.append([remote_port, latency, throughput, anomaly])

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fileName)

    with open(file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

            # Write the header
        csv_writer.writerow(header)

            # Write the data rows
        csv_writer.writerows(rows)

# --- Example Usage ---
num_rows_to_generate = 3000 
output_filename = "testData.csv"
generateCSV(num_rows_to_generate, output_filename)