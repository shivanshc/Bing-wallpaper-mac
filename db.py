import sqlite3
import subprocess
conn = sqlite3.connect('/Users/Chandnanis/Library/Application Support/Dock/desktoppicture.db')
image = '~/Documents/projects/bing-wallpaper/hello.jpg'
c = conn.cursor()

c.execute('UPDATE data SET value=?', (image,))

conn.commit()
conn.close()
subprocess.run(['killall', 'Dock'])
