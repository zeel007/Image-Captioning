from flask import Flask
#from pic import checkValidFace
from flask import request
#import codes
import os
from flask import send_from_directory

app = Flask(__name__)

import week6_final_project_image_captioning_clean as caption

#cvf = checkValidFace()


app.config['UPLOAD_FOLDER'] = "uploads/"

@app.route('/check_pic', methods = ['POST'])
def hello_world():
    if 'file' not in request.files:
        return "File not uploaded :("
    file = request.files['file']
    if file.filename == '':
        return "File not selected"

    if file:
        filename = file.filename
        filedest = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        file.save(filedest)
        pic_path = request.args.get('path', None)
        #caption.apply_model_to_image_raw_bytes()
        print("Getting caption!!")
        cap = caption.apply_model_to_image_raw_bytes(open(filedest, "rb").read())
        print("Got Caption")
        return cap
    else:
        return "Internal Error"


@app.route('/')
def root():
    root_dir = os.path.dirname(os.getcwd())
    dir = os.path.join(root_dir, "week6")
    print(dir)
    return send_from_directory(dir, "index.html")

    #return app.send_static_file('index.html')


if __name__ == '__main__':
    print("Starting WebApp")
    app.run(threaded=True)
