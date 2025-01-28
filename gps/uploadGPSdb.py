import sqlite3
import json

#sample data
gps_data = {
    "coordinates": [
       {
            "coordinate_id": 49529,
            "lat": "0.5875065",
            "long": "35.2040687",
            "created_at": "2025-01-01 06:09:03",
            "updated_at": "2025-01-01 06:09:03",
            "captured_at": "2025-01-01 05:45:03",
            "user_id": 2
        },
        {
            "coordinate_id": 49530,
            "lat": "0.5879936",
            "long": "35.2041785",
            "created_at": "2025-01-01 06:09:03",
            "updated_at": "2025-01-01 06:09:03",
            "captured_at": "2025-01-01 06:09:01",
            "user_id": 2
        },
        {
            "coordinate_id": 49531,
            "lat": "0.5879936",
            "long": "35.2041785",
            "created_at": "2025-01-01 06:44:03",
            "updated_at": "2025-01-01 06:44:03",
            "captured_at": "2025-01-01 06:29:00",
            "user_id": 2
        },
    ]
}

# Database setup
def setupDB():

    db_path = "./inforangeApp.sqlite"

    # Connect to the database
    conn = sqlite3.connect(db_path)


    # Enable SpatiaLite extension
    conn.enable_load_extension(True)
    conn.load_extension("mod_spatialite")

    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coordinates (
            coordinate_id INTEGER PRIMARY KEY,
            latitude REAL,
            longitude REAL,
            created_at TEXT,
            updated_at TEXT,
            captured_at TEXT,
            user_id INTEGER
        );
    ''')
    cursor.execute('''SELECT AddGeometryColumn('coordinates', 'geom', 4326, 'POINT', 'XY')''')

    # Commit and close connection
    conn.commit()
    conn.close()

def uploadData(brian):
    db_path = "./inforangeApp.sqlite"
    # Connect to the database
    conn = sqlite3.connect(db_path)
    # Enable SpatiaLite extension
    conn.enable_load_extension(True)
    conn.load_extension("mod_spatialite")
    cursor = conn.cursor()

    # Parse and brian data
    for entry in brian["coordinates"]:
        coordinate_id = entry["coordinate_id"]
        lat = float(entry["lat"])
        long = float(entry["long"])
        created_at = entry["created_at"]
        updated_at = entry["updated_at"]
        captured_at = entry["captured_at"]
        user_id = entry["user_id"]

        print (coordinate_id, lat, long, created_at, updated_at, captured_at, user_id, long, lat)
    #   Insert data with a spatial geometry
        cursor.execute('''
        INSERT INTO coordinates (coordinate_id, latitude, longitude, created_at, updated_at, captured_at, user_id, geom)
        VALUES (?, ?, ?, ?, ?, ?, ?, MakePoint(?, ?, 4326));
        ''', (coordinate_id, lat, long, created_at, updated_at, captured_at, user_id, long, lat))

    # Commit and close connection
    conn.commit()
    conn.close()

    print(f"Data successfully uploaded to {db_path}.")

# setupDB()
# uploadData(gps_data)
