import csv
from collections import Counter

def read_csv_file(file_path):
    cityes = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cityes.append(row[0])  # Assuming city is the first column (index 0)
    return cityes

def get_unique_cityes_with_count(data):
    city_count = Counter(data)
    unique_cityes = list(city_count.keys())
    city_counts = list(city_count.values())
    return unique_cityes, city_counts

def save_to_csv(unique_cityes, city_counts, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['city', 'Count'])  # Write header row
        for city, count in zip(unique_cityes, city_counts):
            writer.writerow([city, count])

def main():
    input_file = 'latlong.csv'
    output_file = 'unique_cityes.csv'
    cityes = read_csv_file(input_file)
    unique_cityes, city_counts = get_unique_cityes_with_count(cityes)
    save_to_csv(unique_cityes, city_counts, output_file)
    print(f"Unique cityes with counts saved to {output_file}.")

if __name__ == "__main__":
    main()
