import sqlite3 as sq

async def create_db() -> None:
    try:
        global db, cur
        db = sq.connect(r'databases\database.db')
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS User_Data (
                                user_id INTEGER PRIMARY KEY,
                                ch_token TEXT,
                                char_id TEXT, 
                                chat_id TEXT            
                            )''')
        db.commit()
        return db, cur
    except Exception as e:
        print(f"Error initializing database: {e}")
        return None, None


async def add_data(user_id: int, ch_token: str, char_id: str, chat_id: str) -> None:
    try:
        query = "INSERT OR REPLACE INTO User_Data (user_id, ch_token, char_id, chat_id) VALUES (?, ?, ?, ?)"
        cur.execute(query, (user_id, ch_token, char_id, chat_id))
        db.commit()
    except Exception as e:
        print(f"Error adding user: {e}")


async def get_data(user_id: int, param: str) -> str | int:
    try:
        query = f"SELECT {param} FROM User_Data WHERE user_id = ?"
        cur.execute(query, (user_id,))
        result = cur.fetchone()
        return result[0] if result else None
    except Exception as e:
        print(f"Error getting user: {e}")
        return None