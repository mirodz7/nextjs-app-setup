"""
Main window UI for the Perfume Designer Application.
Includes sidebar navigation and central dynamic content area.
Applies dark theme with gold/amber accents using Qt stylesheets.
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QListWidget, QListWidgetItem, QLabel, QStackedWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from .pyramid_builder import PyramidBuilder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perfume Designer App")
        self.resize(1000, 700)

        # Main container widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Horizontal layout: sidebar + main content
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Sidebar navigation
        self.sidebar = QListWidget()
        self.sidebar.setFixedWidth(200)
        self.sidebar.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                color: #d4af37; /* gold */
                border: none;
                font-size: 16px;
            }
            QListWidget::item:selected {
                background-color: #4b3b00;
                color: white;
            }
        """)
        self.sidebar.addItem(QListWidgetItem("Perfume Pyramid Builder"))
        # Future navigation items can be added here

        main_layout.addWidget(self.sidebar)

        # Stacked widget for dynamic content area
        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        # Add pages to stack
        self.pyramid_builder_page = PyramidBuilder()
        self.stack.addWidget(self.pyramid_builder_page)

        # Connect sidebar selection to page change
        self.sidebar.currentRowChanged.connect(self.stack.setCurrentIndex)

        # Set default page
        self.sidebar.setCurrentRow(0)

        # Apply dark theme stylesheet
        self.apply_stylesheet()

    def apply_stylesheet(self):
        # Load stylesheet from resources/styles.qss
        try:
            with open("perfume_designer_app/resources/styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")
