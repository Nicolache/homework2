from arguments import args
from language_parsers import choose_language
from report_kinds import choose_report_kind
from save import get_output_format
from variables import repos_local_path


def main():
    LanguageParser = choose_language(args.language)
    Report = choose_report_kind(args.report)

    language_parsing = LanguageParser(repos_local_path)

    out_data = Report(language_parsing)
    OutputFormat = get_output_format(args.format)
    OutputFormat(out_data, args.output_file)


if __name__ == "__main__":

    main()
