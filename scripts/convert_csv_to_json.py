#!/usr/bin/env python3

import os
import csv
import json


def generate_json_files():

    source_directory = './source-data/gb'
    output_directory = './data/gb'

    for source_file_name in os.listdir(source_directory):

        source_file_location = os.path.join(source_directory, source_file_name)

        if os.path.isfile(source_file_location):

            source_file = open(source_file_location, 'r')

            output_file_name = source_file_name.replace('.csv', '.json')
            output_file_location = os.path.join(output_directory, output_file_name)

            json_data = []

            with open(source_file_location, newline='') as csv_file:
                for row in csv.DictReader(csv_file):
                    # Append the data item as a json key-value if not an empty string
                    json_data.append({k: v for k, v in row.items() if v})
            try:
                with open(output_file_location, 'w', encoding='utf8') as f:
                    json.dump(json_data, f, indent=3, ensure_ascii=False)
            except FileNotFoundError:
                print(
                    f"Output could not be written to {output_file_name}\nDoes the output folder {output_directory} exist?"
                )
                return

            print(f"{source_file.name} >> {output_file_location}")

            source_file.close()
        else:
            print(f"{source_file_location} is not a regular file")


if __name__ == "__main__":
        generate_json_files()
