"""
Perfume Pyramid Builder UI component.
Provides drag-and-drop interface for assigning fragrance notes to Top, Middle, Base layers.
Includes percentage controls for each note.
Visual layout represents the fragrance pyramid structure.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QSlider, QFormLayout, QGroupBox, QAbstractItemView, QLineEdit, QPushButton, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize

class PyramidBuilder(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumWidth(600)
        self.setStyleSheet("""
            QLabel {
                color: #d4af37; /* gold */
                font-weight: bold;
                font-size: 18px;
            }
            QListWidget {
                background-color: #2e2e2e;
                color: white;
                border: 1px solid #d4af37;
            }
            QSlider::handle:horizontal {
                background: #d4af37;
                border-radius: 5px;
                width: 15px;
                margin: -5px 0;
            }
        """)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        title = QLabel("Perfume Pyramid Builder")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # Search/filter input
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search fragrance notes...")
        self.search_input.textChanged.connect(self.filter_notes)
        search_layout.addWidget(self.search_input)
        main_layout.addLayout(search_layout)

        # Horizontal layout for notes list and pyramid layers
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Fragrance notes list (draggable)
        self.notes_list = QListWidget()
        self.notes_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.notes_list.setDragEnabled(True)
        self.notes_list.setFixedWidth(200)
        content_layout.addWidget(self.notes_list)

        # Pyramid layers container
        layers_layout = QVBoxLayout()
        content_layout.addLayout(layers_layout)

        # Create Top, Middle, Base layers
        self.top_layer = self.create_layer("Top Notes")
        self.middle_layer = self.create_layer("Middle Notes")
        self.base_layer = self.create_layer("Base Notes")

        layers_layout.addWidget(self.top_layer)
        layers_layout.addWidget(self.middle_layer)
        layers_layout.addWidget(self.base_layer)

        # Load sample notes (placeholder, to be replaced with DB data)
        self.load_sample_notes()

    def create_layer(self, title):
        group_box = QGroupBox(title)
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        # List widget for notes in this layer (droppable)
        list_widget = QListWidget()
        list_widget.setAcceptDrops(True)
        list_widget.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        list_widget.setDefaultDropAction(Qt.DropAction.MoveAction)
        list_widget.setStyleSheet("""
            QListWidget {
                background-color: #1e1e1e;
                color: #d4af37;
                border: 1px solid #d4af37;
                min-height: 100px;
            }
        """)
        layout.addWidget(list_widget)

        # Percentage control slider
        slider = QSlider(Qt.Orientation.Horizontal)
        slider.setRange(0, 100)
        slider.setValue(0)
        slider.setTickInterval(10)
        slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        slider.setStyleSheet("""
            QSlider::handle:horizontal {
                background: #d4af37;
                border-radius: 5px;
                width: 15px;
                margin: -5px 0;
            }
        """)
        layout.addWidget(slider)

        # Label to show percentage value
        percent_label = QLabel("0%")
        percent_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(percent_label)

        # Connect slider to label update
        slider.valueChanged.connect(lambda val, lbl=percent_label: lbl.setText(f"{val}%"))

        # Store references for later use
        group_box.list_widget = list_widget
        group_box.slider = slider
        group_box.percent_label = percent_label

        return group_box

    def load_sample_notes(self):
        # Placeholder sample notes - to be replaced with DB query results
        sample_notes = [
            "Bergamot", "Lavender", "Jasmine", "Sandalwood", "Vanilla",
            "Patchouli", "Rose", "Lemon", "Cedarwood", "Amber",
            "Musk", "Ylang Ylang", "Cinnamon", "Vetiver", "Orange Blossom"
        ]
        self.notes_list.clear()
        for note in sample_notes:
            item = QListWidgetItem(note)
            item.setSizeHint(QSize(180, 30))
            self.notes_list.addItem(item)

    def filter_notes(self, text):
        for i in range(self.notes_list.count()):
            item = self.notes_list.item(i)
            item.setHidden(text.lower() not in item.text().lower())
