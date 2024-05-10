from msuliot.docx_loader import DocxLoader
from msuliot.pdf_loader import PdfLoader
from msuliot.xlsx_loader import XlsxLoader
from msuliot.csv_loader import CsvLoader
from msuliot.rtf_loader import RtfLoader
from msuliot.pptx_loader import PptxLoader
from msuliot.html_loader import HtmlLoader

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
