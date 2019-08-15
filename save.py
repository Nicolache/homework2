def save_to_pdf():
    pass


def save_to_csv():
    pass


def save_to_json():
    pass


def to_stdout():
    pass


def get_output_format(format):
    return output_formats.get(format)

output_formats = {
    'stdout': to_stdout,
    'json': save_to_json,
    'csv': save_to_csv,
    'pdf': save_to_pdf,
}
