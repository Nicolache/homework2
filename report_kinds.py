import collections
import nltk
from nltk import pos_tag


if not nltk.data.find('taggers/averaged_perceptron_tagger'):
    nltk.download('averaged_perceptron_tagger')


#def lower_case_split(name):
#	lower_name = name.lower()
#	return lower_name.split('_')


def get_top(words):
    return collections.Counter(words).most_common()


def is_noun(word):

    if not word:
        return False
    pos_info = pos_tag([word])

    return pos_info[0][1] in ('NN', 'NNS', 'NNP', 'NNPS')


def is_verb(word):

    if not word:
        return False
    pos_info = pos_tag([word])

    return pos_info[0][1] in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')


def select_verbs_from_name(name):
    """Forms a generator of verbs that are selected from a name.
    """
    words_of_name = name.lower().split('_')
    for word in words_of_name:
        if is_verb(word):
            yield word


def verbs_in_functions(applied_language_parser):
    """Uses selected language class to return verbs out of functions names of code.
    """
	verbs = []
	for name in applied_language_parser.select_function_names_from_nodes():
		for verb in select_verbs_from_name(name):
			verbs.append(verb)
	return get_top(verbs)


def verbs_in_variables(applied_language_parser):
    """Uses selected language class to return verbs out of variables names of code.
    """
    for name in applied_language_parser.select_variable_names_from_nodes():
        for verb in select_verbs_from_name(name):
            verbs.append(verb)
    return get_top(verbs)
    pass


def nouns_in_functions(applied_language_parser):
    pass


def nouns_in_variables(applied_language_parser):
    pass


reports_dictionary = {
    'nouns_in_functions': nouns_in_functions,
    'verbs_in_functions': verbs_in_functions,
    'nouns_in_variables': nouns_in_variables,
    'verbs_in_variables': verbs_in_variables,
}


def choose_report_kind(report_kind):
    return reports_dictionary.get(report_kind)
