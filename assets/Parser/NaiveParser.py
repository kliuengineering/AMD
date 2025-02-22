import os
import re
import json
import logging
from AbstractParser import ParserInterface
from typing import List, Dict

logging.basicConfig(level=logging.INFO)

# << implementation >>
class NaiveParser (ParserInterface):
    def __init__(self, DIRECTORY: str, OUTPUT: str):
        self._directory_path: str = DIRECTORY
        self._output_path: str = OUTPUT


    def search(self, root_dir: str) -> List[str]:
        """Public: Exhaustive depth-first traversal to find .c files."""
        if not os.path.isdir(root_dir):
            logging.error(f"{root_dir} is not a valid directory.")
            return []

        c_files = []
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".c"):
                    posix_path = os.path.normpath(os.path.join(root, file)).replace("\\", "/")
                    c_files.append(posix_path)
        if not c_files:
            logging.warning("No .c files found in the directory.")
        return c_files


    def parse_function(self, file_path: str) -> List[Dict]:
        """Public: Extract function data."""
        code = self.__read_file(file_path)
        if not code:
            return []

        functions = []
        matches = self.__extract_function_signatures(code)

        for match in matches:
            functions.append({
                "signature": match.group(1).strip(),  # Ensure no extra spaces
                "file": file_path,
                "dependencies": self.__extract_dependencies(code),
                "comments": self.__extract_comments(code, match.start())  # Properly extracted comments
            })
        return functions


    def run(self) -> None:
        """Public: Main director to gather, parse, and save data."""
        c_files = self.search(self._directory_path)
        json_output = []

        for c_file in c_files:
            parsed_functions = self.parse_function(c_file)
            json_output.extend(parsed_functions)

        self.__write_json(json_output, self._output_path)


    def __extract_function_signatures(self, code: str) -> List[re.Match]:
        """Private: Extract function signatures from the code using regex."""
        function_pattern = r"^\s*(\w[\w\s\*]+\s+\w+\s*\([^)]*\))\s*{"
        return list(re.finditer(function_pattern, code, re.MULTILINE))


    def __extract_dependencies(self, code: str) -> List[str]:
        """Private: Extract #include statements."""
        include_pattern = r"#include\s+[\"<](.*?)[\">]"
        return re.findall(include_pattern, code)


    def __extract_comments(self, code: str, position: int) -> List[str]:
        """
        Private: Extracts comments above a function, handling both single-line (//) 
        and multi-line (/* ... */) comments.
        
        - Ignores blank lines.
        - Stops when it reaches a non-comment line.
        """
        comments = []
        lines = code[:position].split("\n")  # Only consider lines before function start
        in_multiline_comment = False  # Flag for multi-line comments

        for line in reversed(lines):
            stripped_line = line.strip()

            if stripped_line == "":  # Ignore blank lines
                continue

            if stripped_line.startswith("*/"):  
                in_multiline_comment = True  # Start capturing multi-line comments
                comments.append(stripped_line)
                continue

            if in_multiline_comment:
                comments.append(stripped_line)
                if stripped_line.startswith("/*"):  # End of multi-line comment
                    in_multiline_comment = False
                continue

            if stripped_line.startswith("//"):  # Capture single-line comments
                comments.append(stripped_line.lstrip("/").strip())  # Remove "//" and strip spaces
            else:
                break  # Stop at first non-comment line

        return comments[::-1]  # Ensure correct order


    def __read_file(self, file_path: str) -> str:
        """Private: Safely read a file."""
        try:
            with open(file_path, "r") as fd:
                return fd.read()
        except FileNotFoundError:
            logging.error(f"File {file_path} not found.")
        except Exception as e:
            logging.error(f"Error reading file {file_path}: {e}")
        return ""


    def __write_json(self, data: List[Dict], output_path: str) -> None:
        """Private: Safely write data to a JSON file."""
        try:
            with open(output_path, "w") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            logging.error(f"Error writing JSON to {output_path}: {e}")
