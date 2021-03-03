# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (
        songplay_id INT PRIMARY KEY NOT NULL,
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR NOT NULL,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT NOT NULL,
        location VARCHAR NOT NULL,
        user_agent VARCHAR NOT NULL,
        UNIQUE (songplay_id)
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
        user_id INT PRIMARY KEY NOT NULL,
        first_name VARCHAR NOT NULL,
        last_name VARCHAR NOT NULL,
        gender VARCHAR NOT NULL,
        level VARCHAR NOT NULL,
        UNIQUE (user_id)
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (
        song_id VARCHAR PRIMARY KEY NOT NULL,
        title VARCHAR NOT NULL,
        artist_id VARCHAR NOT NULL,
        year INT NOT NULL,
        duration NUMERIC(10,5) NOT NULL,
        UNIQUE (song_id)
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (
        artist_id VARCHAR PRIMARY KEY NOT NULL,
        artist_latitude NUMERIC(10,5),
        artist_longitude NUMERIC(10,5),
        artist_location VARCHAR,
        artist_name VARCHAR NOT NULL,
        UNIQUE (artist_id)
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (
        start_time TIMESTAMP NOT NULL,
        hour INT NOT NULL,
        day INT NOT NULL,
        week INT NOT NULL,
        month INT NOT NULL,
        year INT NOT NULL,
        weekday INT NOT NULL
    )
""")


# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO NOTHING
""")

song_table_insert = ("""
    INSERT INTO songs (artist_id, song_id, title, duration, year)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id)
    DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, artist_latitude, artist_longitude, artist_location, artist_name)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO NOTHING
""")

time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
    SELECT
        s.song_id,
        s.artist_id
    FROM
        songs AS s
    JOIN
        artists AS a
    ON
        a.artist_id = s.artist_id
    WHERE
        s.title = %s
    AND 
        a.artist_name = %s
    AND 
        s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]