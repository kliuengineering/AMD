from typing import List, Dict
from abc import ABC, abstractmethod

# << interface >>
class ParserInterface(ABC):
    """
    This is the interface class for the Parser. Implementations of this interface
    should define methods for:
    1. search() - Search strategy for locating files to parse.
    2. parse_function() - Parsing strategy for extracting function metadata.
    3. run() - Orchestrates the search, parse, and output process.
    """
    @abstractmethod
    def search ( self, root_dir:str ) -> List[str]:
        """Encapsulates the search strategy of this parser implementation."""
        pass

    @abstractmethod
    def parse_function ( self, file_path:str ) -> List[Dict]:
        """Encapsulates the parsing strategy of this parser implementation."""
        pass

    @abstractmethod
    def run ( self ) -> None:
        """Encapsulates the start signal of the parser."""
        pass