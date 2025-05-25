# Perfume Designer Application

## Overview
This is a fully offline, desktop-based perfume design application built with Python and PyQt6. It features a modern, dark-themed UI with gold/amber accents to evoke luxury.

## Features (Phase 1)
- Main application window with sidebar navigation and central dynamic content area.
- Perfume Pyramid Builder with drag-and-drop interface for Top, Middle, and Base fragrance notes.
- Percentage controls for each note.
- Local SQLite database storing fragrance note data with sample entries.
- Modular code structure for easy future expansion.

## Project Structure
```
perfume_designer_app/
├── main.py                  # Application entry point
├── ui/
│   ├── main_window.py       # Main window UI
│   └── pyramid_builder.py   # Perfume pyramid builder UI
├── db/
│   └── database.py          # SQLite database connection and schema
├── resources/
│   └── styles.qss           # Qt stylesheet for dark theme with gold/amber accents
└── README.md                # Project overview and instructions
```

## Requirements
- Python 3.11+
- PyQt6
- SQLite3 (bundled with Python)

## Running the Application
1. Install PyQt6 if not already installed:
   ```
   pip install PyQt6
   ```
2. Run the application:
   ```
   python perfume_designer_app/main.py
   ```

## Future Phases
- AI assistant integration
- PDF reporting
- Inventory tracking
- User roles and permissions
- Moodboards and inspiration tools

## License
MIT License
