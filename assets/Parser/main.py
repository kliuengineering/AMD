from NaiveParser import NaiveParser

def main() -> None:
    # Update with your actual directory path for the repo
    GENOA_POC_PATH = "C:/AmdWorkspace/Parser/test_directory"
    OUTPUT_JSON = "parsed_functions.json"
    parser = NaiveParser(GENOA_POC_PATH, OUTPUT_JSON)
    parser.run()

if __name__ == "__main__":
    main()