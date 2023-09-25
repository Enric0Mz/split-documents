import csv
import os

input_file = "input/filename.csv"
occurrences_per_file = 10 # Number of occurrences per file
output_directory = "output/directory"

def split_csv_file(input_file, output_directory, occurrences_per_file):
    """Splits a CSV file into multiple files, with each file containing
    occurrences_per_file rows and the same header in all of them.

    Args:
        input_file (str): The path to the input CSV file.
        output_directory (str): The path to the output directory where
            the split files will be saved.
        occurrences_per_file (int): The number of occurrences to include
            in each split file.

    Returns:
        None
    """

    os.makedirs(output_directory, exist_ok=True)

    with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
        csv_reader = csv.reader(infile)

        header = next(csv_reader)

        chunk_count = 1
        line_count = 0
        output_file = os.path.join(output_directory, f"output_{chunk_count}.csv")

        with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
            csv_writer = csv.writer(outfile)

            csv_writer.writerow(header)

            for row in csv_reader:
                csv_writer.writerow(row)
                line_count += 1
                if line_count == occurrences_per_file:
                    chunk_count += 1
                    line_count = 0
                    output_file = os.path.join(output_directory, f"output_{chunk_count}.csv")

                    outfile = open(output_file, mode="w", newline="", encoding="utf-8")
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(header)

split_csv_file(input_file, output_directory, occurrences_per_file)
