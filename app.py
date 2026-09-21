import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class EmailDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        mime_data = event.mimeData()

        print("Available drag formats:", mime_data.formats())
        print("Has URLs:", mime_data.hasUrls())

        print("Reading URLs...")
        urls = mime_data.urls()
        print("URL count:", len(urls))

        for url in urls:
            print("Dragged URL:", url.toString())

        if mime_data.hasUrls():
            event.acceptProposedAction()
            print("Drag entry accepted.")
        else:
            event.ignore()
            print("Drag entry rejected.")

    def dropEvent(self, event):
        mime_data = event.mimeData()

        for url in mime_data.urls():
            if url.isLocalFile():
                file_path = url.toLocalFile()
                print("Dropped local path:", file_path)

def main():
    app = QApplication(sys.argv)

    window = EmailDropWindow()
    window.setWindowTitle("Mail-Ablage")
    window.resize(600, 400)

    instruction_label = QLabel("Ziehen Sie Ihre E-Mails hierher.")
    instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    layout = QVBoxLayout()
    layout.addWidget(instruction_label)
    window.setLayout(layout)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

