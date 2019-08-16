import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    '--clear',
    '--clear-local-repos-directory',
    action='store_true',
    help='It removes all the directories \
        inside repos_local_path\
        on start.',
)
parser.add_argument(
    '-c',
    '--clone',
    action='store_true',
    help='It clones all from repos_to_clone_urls variable.',
)
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
    help="A kind of statistics. Default is verbs_in_functions.",
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
