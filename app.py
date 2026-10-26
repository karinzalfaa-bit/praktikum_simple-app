from flask import Flask, request

app = Flask(__name__)

@app.routfrom flask import Flask, request
import sqlite3

app = Flask(__name__)

# Inisialisasi Database SQLite
def init_db():
    conn = sqlite3.connect('praktikum.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengunjung (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def hello():
    return "Halo dari Flask + Docker + Jenkins! (Database SQLite Terkoneksi)"

@app.route('/cek-db')
def cek_db():
    # Rute ini untuk membuktikan ke asprak bahwa koneksi DB berhasil
    conn = sqlite3.connect('praktikum.db')
    cursor = conn.cursor()
    cursor.execute('SELECT sqlite_version();')
    versi = cursor.fetchone()
    conn.close()
    return f"Koneksi Database Berhasil! Versi SQLite: {versi[0]}"

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.get_json(silent=True)
    print("Webhook diterima dari GitHub")
    return "Webhook received", 200

if __name__ == '__main__':
    # Berjalan di port 5001
    app.run(host='0.0.0.0', port=5001)e('/')
def hello():
    return "Halo dari Flask + Docker + Jenkins!"


@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.get_json(silent=True)

    print("Webhook diterima dari GitHub")
    print(payload)

    return "Webhook received", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
