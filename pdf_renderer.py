import fitz  # PyMuPDF

class PDFRenderer:
    def __init__(self):
        self.doc = None

    def open_pdf(self, filepath):
        self.doc = fitz.open(filepath)

    def get_page_count(self):
        return self.doc.page_count if self.doc else 0

    def render_page(self, page_number, zoom=1.0, rotation=0):
        if not self.doc or not (0 <= page_number < self.doc.page_count):
            return None
        page = self.doc.load_page(page_number)
        mat = fitz.Matrix(zoom, zoom).prerotate(rotation)
        pix = page.get_pixmap(matrix=mat)
        import io
        from kivy.core.image import Image as CoreImage
        data = io.BytesIO(pix.tobytes("png"))
        texture = CoreImage(data, ext='png').texture
        return texture, (texture.width, texture.height)
