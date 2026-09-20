import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


def main():
    app = QApplication(sys.argv)

    window = QWidget()
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

    