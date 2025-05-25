"""
Entry point for the Perfume Designer Application.
Initializes the PyQt6 application and shows the main window.
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow

def main():
    # Force using offscreen platform plugin
    sys.argv += ['-platform', 'offscreen']
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
