import os
from vcstools import get_vcs_client

from arguments import args
from language_parsers import choose_language
from report_kinds import choose_report_kind
from save import get_output_format
from variables import repos_local_path, repos_to_clone_urls


def delete_repos_directories():
    """Deletes all the folders and their contents in `repos_local_path`
    location.
    """
    for directory in os.listdir(repos_local_path):
        os.system('rm -rf ' + repos_local_path + '/' + directory)


def repo_clone(https_url, vcs_type):
    """Cloning a specified repository url, with a specified repo type
    into a `repos_local_path directory`, creating subdirectory by a repo name.

    Keyword arguments:
    https_url -- a string of repository url.
    vcs_type -- a string of a type of a repository, such as: git, svn, hg.
    """
    reponame = https_url.rsplit('/', 1)[1]
    client = get_vcs_client(vcs_type, repos_local_path + reponame)
    client.checkout(https_url)


def clone_all():
    """Executes cloning of each repository by `repos_to_clone_urls` plenty.
    """
    print('working')
    for url_and_vcstype in repos_to_clone_urls:
        repo_clone(url_and_vcstype[0], url_and_vcstype[1])


def main():
    if args.clear:
        delete_repos_directories()

    if args.clone:
        clone_all()

    LanguageParser = choose_language(args.language)
    Report = choose_report_kind(args.report)

    language_parsing = LanguageParser(repos_local_path)

    out_data = Report(language_parsing)
    OutputFormat = get_output_format(args.format)
    OutputFormat(out_data, args.output_file)


if __name__ == "__main__":

    main()
