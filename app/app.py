import qrcode
import image
from flask import redirect, render_template, request, Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'GET':
        return redirect(url_for('generate_qr'))
    return render_template('index.html')

@app.route('/generate_qr', methods=['GET'])
def generate_qr():

    qr = qrcode.QRCode(
        version = 15,
        box_size = 10,
        border = 5
    )

    data = request.args.get('data')
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill='black', back_color = 'white')
    img.save('static/req_img.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)