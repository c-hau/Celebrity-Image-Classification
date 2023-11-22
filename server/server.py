from flask import request,jsonify,Flask
import util

app=Flask(__name__)
@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data=request.form['image_data']
    response=jsonify(util.classify_image(image_data))
    response.headers.add('Access-control-allow-origin','*')
    return response

if __name__=="__main__":
    print("starting Python flask server for Women Celebrity Image")
    util.load_artificats()
    app.run(port=5000)
