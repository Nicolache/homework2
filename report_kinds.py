import collections
import nltk
from nltk import pos_tag
from typing import Generator


if not nltk.data.find('taggers/averaged_perceptron_tagger'):
    nltk.download('averaged_perceptron_tagger')


def get_top(words):
    """Function makes chart out of plenty of words.

    Keyword arguments:
    words -- list of words.

    Returns list
    """
    return collections.Counter(words).most_common()


def is_noun(word):
    """Function checks if a given word is a noun.

    Keyword arguments:
    word -- a string with a word.

    Returns bool
    """
    if not word:
        return False
    pos_info = pos_tag([word])

    return pos_info[0][1] in ('NN', 'NNS', 'NNP', 'NNPS')


def is_verb(word):
    """Function checks if a given word is a verb.

    Keyword arguments:
    word -- a string with a word.

    Returns bool
    """
    if not word:
        return False
    pos_info = pos_tag([word])

    return pos_info[0][1] in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')


def select_verbs_from_name(name: str) -> Generator[str, None, None]:
    """Forms a generator of verbs that are selected from a name.

    Keyword arguments:
    name -- name of a unit in a computer code, such as variable,
    or function.

    Returns a generator
    """
    words_of_name = name.lower().split('_')
    for word in words_of_name:
        if is_verb(word):
            yield word


def select_nouns_from_name(name: str) -> Generator[str, None, None]:
    """Forms a generator of nouns that are selected from a name.

    Keyword arguments:
    name -- name of a unit in a computer code, such as variable,
    or function.

    Returns a generator
    """
    words_of_name = name.lower().split('_')
    for word in words_of_name:
        if is_noun(word):
            yield word


def verbs_in_functions(applied_language_parser):
    """Uses selected language class
    to return verbs out of functions names of code.

    Keyword arguments:
    applied_language_parser -- A class that is selected to apply
    to a certain kind of a computer language code.

    Returns list
    """
    verbs = []
    for name in applied_language_parser.select_function_names_from_nodes():
        for verb in select_verbs_from_name(name):
            verbs.append(verb)
    return get_top(verbs)


def verbs_in_variables(applied_language_parser):
    """Uses selected language class
    to return verbs out of variables names of code.

    Keyword arguments:
    applied_language_parser -- A class that is selected to apply
    to a certain kind of a computer language code.

    Returns list
    """
    verbs = []
    for name in applied_language_parser.select_variable_names_from_nodes():
        for verb in select_verbs_from_name(name):
            verbs.append(verb)
    return get_top(verbs)


def nouns_in_functions(applied_language_parser):
    """Uses selected language class
    to return nouns out of functions names of code.

    Keyword arguments:
    applied_language_parser -- A class that is selected to apply
    to a certain kind of a computer language code.

    Returns list
    """
    nouns = []
    for name in applied_language_parser.select_function_names_from_nodes():
        for noun in select_nouns_from_name(name):
            nouns.append(noun)
    return get_top(nouns)


def nouns_in_variables(applied_language_parser):
    """Uses selected language class
    to return nouns out of variables names of code.

    Keyword arguments:
    applied_language_parser -- A class that is selected to apply
    to a certain kind of a computer language code.

    Returns list
    """
    nouns = []
    for name in applied_language_parser.select_variable_names_from_nodes():
        for noun in select_nouns_from_name(name):
            nouns.append(noun)
    return get_top(nouns)


_reports_dictionary = {
    'nouns_in_functions': nouns_in_functions,
    'verbs_in_functions': verbs_in_functions,
    'nouns_in_variables': nouns_in_variables,
    'verbs_in_variables': verbs_in_variables,
}


def choose_report_kind(report_kind):
    return _reports_dictionary.get(report_kind)
