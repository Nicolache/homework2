import collections
import csv
import json


def save_to_pdf():
    """An empty function, as an example of future formats.
    """
    pass


def save_to_csv(data, write_file):
    """Saves data to csv format to a file with a certain filename.

    Keyword arguments:
    data -- input data
    """
    list_for_csv = []
    for word, occurence in collections.Counter(data).most_common():
        list_for_csv.append([word[0], word[1], occurence])
    with open(write_file, "w") as write_file:
        writer = csv.writer(write_file, delimiter=',')
        for line in list_for_csv:
            writer.writerow(line)


def save_to_json(data, write_file):
    dict_for_json = {}
    for word, occurence in collections.Counter(data).most_common():
        dict_for_json.update({word[0]: (word[1], occurence)})
    with open(write_file, "w") as write_file:
        json.dump(dict_for_json, write_file)


def to_stdout(data, write_file):
    print(data)


def get_output_format(format):
    return _output_formats.get(format)


_output_formats = {
    'stdout': to_stdout,
    'json': save_to_json,
    'csv': save_to_csv,
    'pdf': save_to_pdf,
}
