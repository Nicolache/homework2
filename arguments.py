import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '-r',
    '--report',
    choices=[
        'nouns_in_functions',
        'verbs_in_functions',
        'nouns_in_variables',
        'verbs_in_variables'
    ],
    default='verbs_in_functions',
    help="A kind of statistics",
)
parser.add_argument(
    '-l',
    '--language',
    choices=['python', 'ruby'],
    default='python',
    help="Parsing language choice.",
)
parser.add_argument(
    '-f',
    '--format',
    choices=['stdout', 'json', 'csv', 'pdf'],
    default='stdout',
    help="Output to stdout, or to a file with a chosen format.",
)
parser.add_argument(
    '-o',
    '--output_file',
    action='store',
    type=str,
    help="The name of file to save in.",
)
args = parser.parse_args()
