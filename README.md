# Homework2
This is a homework to check.
This is executable in Python3 .
Tested in Python 3.5.2, 3.6.8, 3.6.9 .
This script makes some function names, or variable names statistics in given projects. It uses "ast" module to walk the code tree, and "nltk" module to distinguish between parts of speech. The essential variables (such as repos_local_path) is located in file variables.py . You can add, or clone with this script some projects to the location in variable repos_local_path, and launch it the way below:
## Usage. ##
    start.py [-h] [--clear] [-c]
             [-r {nouns_in_functions,verbs_in_functions,nouns_in_variables,verbs_in_variables}]
             [-l {python,ruby}] [-f {stdout,json,csv,pdf}] [-o OUTPUT_FILE]

    optional arguments:
      -h, --help            show this help message and exit
      --clear, --clear-local-repos-directory
                            It removes all the directories inside repos_local_path
                            on start.
      -c, --clone           It clones all from repos_to_clone_urls variable.
      -r {nouns_in_functions,verbs_in_functions,nouns_in_variables,verbs_in_variables}, --report {nouns_in_functions,verbs_in_functions,nouns_in_variables,verbs_in_variables}
                            A kind of statistics. Default is verbs_in_functions.
      -l {python,ruby}, --language {python,ruby}
                            Parsing language choice.
      -f {stdout,json,csv,pdf}, --format {stdout,json,csv,pdf}
                            Output to stdout, or to a file with a chosen format.
      -o OUTPUT_FILE, --output_file OUTPUT_FILE
                            The name of file to save in.
## Example of using the script. ##
    python3 start.py
    python3 start.py -r verbs_in_functions
    python3 start.py -r verbs_in_functions -f json -o data.json

    python3 start.py -r verbs_in_functions
## Python files meaning. ##
 * **arguments.py** -- Arguments key names are defined in this file. Each key has its help line. You can watch help with the **python3 start.py -h** command as well.
 * **language_parsers.py** -- Classes to parse different languages.
 * **report_kinds.py** -- Kinds of the statistics.
 * **save.py** -- Output formats.
 * **start.py** -- The main file.
 * **variables.py** -- All variables definitions including logging.
