from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-ip', methods=['POST'])
def save_ip():
    ip_address = request.form['ip_address']
    df = pd.DataFrame({'IP Address': [ip_address]})
    df.to_excel('ip_addresses.xlsx', index=False, mode='a', header=not os.path.isfile('ip_addresses.xlsx'))
    return 'IP address saved successfully'

# Rest of the code...

if __name__ == '__main__':
    app.run()
