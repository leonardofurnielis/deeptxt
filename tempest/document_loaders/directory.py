import glob
import os
from pathlib import Path
from typing import List, Optional, Type

from tempest.core.document import Document
from tempest.core.document_loaders import BaseLoader


def _loading_default_supported_loaders():
    from tempest.document_loaders import DocxLoader, HTMLLoader, PDFLoader

    return {
    ".docx": DocxLoader,
    ".html": HTMLLoader,
    ".pdf": PDFLoader,
}


class DirectoryLoader(BaseLoader):
    """Simple directory loader.

    Args:
        required_exts: (List[str], optional): List of file extensions to only load files with those extensions.
        recursive (str, optional): Whether to recursively search for files. Defaults to ``False``.
    """
    
    required_exts: List[str] = [".pdf", ".docx", ".html"]
    recursive: Optional[bool] = False
    file_loader: Optional[dict[str, Type[BaseLoader]]] = None

    def load_data(self, input_dir: str, extra_info: Optional[dict] = None) -> List[Document]:
        """Loads data from the specified directory.
        
        Args:
            input_dir (str): Directory path from which to load the documents.
        """
        if not os.path.isdir(input_dir):
            raise ValueError(f"`{input_dir}` is not a valid directory.")
        
        if self.file_loader is None:
            self.file_loader = _loading_default_supported_loaders()
        
        input_dir = Path(input_dir)
        documents = []
        
        pattern_prefix = "**/*" if self.recursive else ""

        for extension in self.required_exts:
            files = glob.glob(os.path.join(input_dir, pattern_prefix + extension), recursive=self.recursive)
            
            for file_dir in files:
                loader_cls = self.file_loader.get(extension)
                if loader_cls:
                    try:
                        #TO-DO add `file_loader_kwargs`
                        doc = loader_cls().load_data(file_dir)
                        documents.extend(doc)
                    except Exception as e:
                        raise f"Error reading {file_dir}: {e}"
                else:
                    #TO-DO add `unstructured file` support
                    raise f"Unsupported file type: {extension}"

        return documents
