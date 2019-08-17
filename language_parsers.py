import ast
import os
from typing import Generator, Any
from variables import logging, MAXFILENAMES


class AllLanguagesParser(object):

    def __init__(self, path):
        self.path = path

    def get_filenames(self) -> Generator[str, None, None]:
        """Get all *.py files locations inside `self.path` location.
        This is a common method for all the programming language parsers.

        Returns a generator.
        """
        filenames_counter = 0
        for dirname, dirs, files in os.walk(self.path, topdown=True):
            for file in files:
                if file.endswith('.py') and filenames_counter < MAXFILENAMES:
                    filenames_counter += 1
                    yield os.path.join(dirname, file)


class PythonParser(AllLanguagesParser):

    def __init__(self, path):
        super().__init__(path)

    def get_trees(
        self,
        with_filenames: bool = False,
        with_file_content: bool = False
    ) -> Generator[Any, None, None]:
        """Generates ast objects, or ast objects in tuple
        with filenames, and file contents.

        Keyword arguments:
        self.path -- A path string.
        with_filenames -- `bool`:
            A flag that switches "with filenames" return mode on:
            ((filename, tree), ...)
        with_file_content -- `bool`:
            A flag that switches "with file content" return mode on:
            ((filename, main_file_content, tree), ...)

        Returns a generator.
        """
        filenames_counter = 0
        for filename in self.get_filenames():
            with open(filename, 'r', encoding='utf-8') as attempt_handler:
                main_file_content = attempt_handler.read()
            try:
                tree = ast.parse(main_file_content)
                filenames_counter += 1
            except SyntaxError as e:
                logging.warning(e)
                tree = None
            if not with_filenames:
                yield tree
            if with_filenames and not with_filenames:
                yield (filename, tree)
            if with_filenames and with_file_content:
                yield (filename, main_file_content, tree)
        logging.debug('Total {} files'.format(filenames_counter))
        logging.debug('trees generated')

    def generate_nodes_out_of_trees(self) -> Generator[Any, None, None]:
        """Returns all nodes of code, as ast tree objects like:
        <_ast.Index object at 0x7f1fbc30>
        <_ast.Attribute object at 0x7f1fa1d0>
        <_ast.Subscript object at 0x7f1f0870>
        <_ast.Call object at 0x7f1f8a70>
        <_ast.Num object at 0x7f1f8bb0>
        <_ast.BinOp object at 0x7f1f8d50>
        <_ast.Add object at 0x7f98eb50>
        <_ast.Str object at 0x7f1f8fd0>
        <_ast.Load object at 0x7f98e2d0>,
        but i do not know how to annotate it more precisely.

        Returns a generator.
        """
        for tree in self.get_trees():
            for node in ast.walk(tree):
                yield node

    def select_function_names_from_nodes(self) -> Generator[str, None, None]:
        """Extracts from nodes all the function names in lowercase.

        Returns a generator.
        """
        for node in self.generate_nodes_out_of_trees():
            if isinstance(node, ast.FunctionDef) and\
                not (node.name.lower().startswith('__') and
                node.name.lower().endswith('__')):
                yield node.name.lower()

    def select_variable_names_from_nodes(self) -> Generator[str, None, None]:
        """Extracts from nodes all the variables names in lowercase.

        Returns a generator.
        """
        for node in self.generate_nodes_out_of_trees():
            if isinstance(node, ast.Name):
                yield node.id.lower()


def choose_language(language):
    """A function that helps to choose the desired programming language class
    to parse.

    Returns a class.
    """
    return _language_classes_dictionary.get(language)


_language_classes_dictionary = {
    'python': PythonParser
}
