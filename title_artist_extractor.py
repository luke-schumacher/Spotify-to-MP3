import csv

def simplify_data(input_csv, output_csv):
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        simplified_data = []
        for row in reader:
            # Extract track name and artist from the row
            track_name = row[1].strip('"')
            artist_names = row[3].strip('"').replace('spotify:artist:', '').replace(',', ', ')
            simplified_data.append([track_name, artist_names])

    # Write the simplified data to the output CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Track Name', 'Artist'])
        writer.writerows(simplified_data)

if __name__ == "__main__":
    input_csv = 'YOUR_CSV_NAME.csv'
    output_csv = 'simplified_wYOUR_CSV_NAME.csv'
    simplify_data(input_csv, output_csv)
