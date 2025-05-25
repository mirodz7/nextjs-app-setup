"""
SQLite database connection and schema setup for Perfume Designer Application.
Includes sample data insertion for fragrance notes.
"""

import sqlite3
from sqlite3 import Connection
from typing import List, Tuple

DB_FILE = "perfume_designer_app/db/perfume_designer.db"

class Database:
    def __init__(self, db_file: str = DB_FILE):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.create_tables()
        self.insert_sample_data()

    def create_connection(self) -> Connection:
        """Create a database connection to the SQLite database."""
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connected to SQLite database at {self.db_file}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def create_tables(self):
        """Create fragrance_notes table."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS fragrance_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            note_name TEXT NOT NULL,
            note_type TEXT CHECK(note_type IN ('Top', 'Middle', 'Base')) NOT NULL,
            scent_family TEXT,
            natural_synthetic TEXT CHECK(natural_synthetic IN ('Natural', 'Synthetic')),
            scientific_name TEXT,
            trade_name TEXT
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
            print("Created fragrance_notes table.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def insert_sample_data(self):
        """Insert sample fragrance notes if table is empty."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM fragrance_notes;")
        count = cursor.fetchone()[0]
        if count > 0:
            print("Sample data already exists, skipping insertion.")
            return

        sample_notes: List[Tuple] = [
            ("Bergamot", "Top", "Citrus", "Natural", "Citrus bergamia", "Bergamot Oil"),
            ("Lavender", "Top", "Floral", "Natural", "Lavandula angustifolia", "Lavender Oil"),
            ("Lemon", "Top", "Citrus", "Natural", "Citrus limon", "Lemon Oil"),
            ("Peppermint", "Top", "Herbal", "Natural", "Mentha piperita", "Peppermint Oil"),
            ("Jasmine", "Middle", "Floral", "Natural", "Jasminum grandiflorum", "Jasmine Absolute"),
            ("Rose", "Middle", "Floral", "Natural", "Rosa damascena", "Rose Absolute"),
            ("Ylang Ylang", "Middle", "Floral", "Natural", "Cananga odorata", "Ylang Ylang Oil"),
            ("Cinnamon", "Middle", "Spicy", "Natural", "Cinnamomum verum", "Cinnamon Oil"),
            ("Sandalwood", "Base", "Woody", "Natural", "Santalum album", "Sandalwood Oil"),
            ("Vanilla", "Base", "Gourmand", "Natural", "Vanilla planifolia", "Vanilla Absolute"),
            ("Patchouli", "Base", "Woody", "Natural", "Pogostemon cablin", "Patchouli Oil"),
            ("Amber", "Base", "Resinous", "Synthetic", "N/A", "Amber Accord"),
            ("Musk", "Base", "Animalic", "Synthetic", "N/A", "Musk Accord"),
            ("Cedarwood", "Base", "Woody", "Natural", "Cedrus atlantica", "Cedarwood Oil"),
            ("Vetiver", "Base", "Woody", "Natural", "Vetiveria zizanoides", "Vetiver Oil"),
            ("Orange Blossom", "Middle", "Floral", "Natural", "Citrus aurantium", "Neroli Oil"),
            ("Geranium", "Middle", "Floral", "Natural", "Pelargonium graveolens", "Geranium Oil"),
            ("Clove", "Middle", "Spicy", "Natural", "Syzygium aromaticum", "Clove Oil"),
            ("Benzoin", "Base", "Resinous", "Natural", "Styrax benzoin", "Benzoin Resin"),
            ("Frankincense", "Base", "Resinous", "Natural", "Boswellia carterii", "Frankincense Oil"),
        ]

        insert_sql = """
        INSERT INTO fragrance_notes (
            note_name, note_type, scent_family, natural_synthetic, scientific_name, trade_name
        ) VALUES (?, ?, ?, ?, ?, ?);
        """

        try:
            cursor.executemany(insert_sql, sample_notes)
            self.conn.commit()
            print("Inserted sample fragrance notes.")
        except sqlite3.Error as e:
            print(f"Error inserting sample data: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
