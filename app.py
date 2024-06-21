from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

def create_wifi_qr(ssid, password, encryption):
    wifi_format = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_format)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_data = None
    if request.method == 'POST':
        ssid = request.form['ssid']
        password = request.form['password']
        encryption = request.form['encryption']
        img = create_wifi_qr(ssid, password, encryption)
        buffer = io.BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        qr_code_data = f"data:image/png;base64,{img_base64}"
    return render_template('index.html', qr_code_data=qr_code_data)

if __name__ == '__main__':
    app.run(debug=True)
