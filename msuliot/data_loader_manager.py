from docx_loader import DocxLoader
from pdf_loader import PdfLoader
from xlsx_loader import XlsxLoader
from csv_loader import CsvLoader
from rtf_loader import RtfLoader
from pptx_loader import PptxLoader
from html_loader import HtmlLoader

class DataLoaderManager:
    def __init__(self):
        self.loaders = {
            'docx': DocxLoader(),
            'pdf': PdfLoader(),
            'xlsx': XlsxLoader(),
            'csv': CsvLoader(),
            'rtf': RtfLoader(),
            'pptx': PptxLoader(),
            'html': HtmlLoader()
        }

    def load_data(self, data_path, file_type):
        loader = self.loaders.get(file_type.lower())
        if loader:
            return loader.load_data(data_path)
        else:
            raise ValueError(f"No data loader available for file type: {file_type}")
        
    def get_supported_data_loaders(self):
        return list(self.loaders.keys())
