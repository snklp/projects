from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/locations')
def get_locations():
    response = jsonify({
        'locations': util.get_locations()
    })
    return 'Hi'



if __name__ == '__main__':
    print('Starting Server')
    app.run(debug=True)