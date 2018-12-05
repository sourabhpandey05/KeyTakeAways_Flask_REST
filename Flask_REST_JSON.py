from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
   return jsonify({
   	      "idea" :"Do coding with Flask and Android"
       
       }
    )

if __name__ == '__main__':
   app.run()