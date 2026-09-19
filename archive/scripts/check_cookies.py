import sqlite3
import shutil
import os

for browser, path in [
    ('Chrome', os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies'),
    ('Edge', os.path.expanduser('~') + r'\AppData\Local\Microsoft\Edge\User Data\Default\Network\Cookies')
]:
    if os.path.exists(path):
        temp_path = f'temp_cookies_{browser}.db'
        try:
            shutil.copy2(path, temp_path)
            conn = sqlite3.connect(temp_path)
            cur = conn.cursor()
            cur.execute("SELECT host_key, name, value, length(encrypted_value) FROM cookies WHERE host_key LIKE '%chatgpt%' OR host_key LIKE '%openai%'")
            rows = cur.fetchall()
            print(browser, 'found', len(rows), 'cookies')
            for r in rows:
                print('  ', r[0], r[1], 'has_val:', bool(r[2]), 'enc_len:', r[3])
            conn.close()
        except Exception as e:
            print(f"Error reading {browser}: {e}")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
