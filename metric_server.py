# -*-coding:utf-8-*-
import os
import time

from common import constant
from flask import Flask, request
from werkzeug.utils import secure_filename
from metric_main import metric_from_file

app = Flask("metric_server")


@app.route("/hello")
def hello():
    return "<p>Hello</p>"


@app.route("/metric_handler")
def metric_handler():
    if request.method == 'POST':
        files = []
        # context['uploaded_number'] = len(request.files)
        # get
        for i in range(len(request.files)):
            files.append(request.files['upload_file{}'.format(i)])

        # save
        cnt = 0
        for f in files:
            upload_path = os.path.join(constant.OUTPUT_DIR, f.filename)
            try:
                f.save(upload_path)
            except:
                cnt += 1
        # context['failed_number'] = cnt
        # return render_template('upload.html', **context)
        # return redirect(url_for('upload'))
    else:
        ""

    return "<p>Hello</p>"


@app.route('/metric', methods=['GET', 'POST'])
def metric():
    if request.method == 'POST':
        files = []
        # context['uploaded_number'] = len(request.files)
        # get
        for i in range(len(request.files)):
            files.append(request.files['upload_file{}'.format(i)])

        # save
        cnt = 0
        file_path_list = []
        for f in files:
            upload_path = os.path.join(constant.OUTPUT_DIR, "{}{}".format(f.filename, time.time()))
            file_path_list.append(upload_path)
            try:
                f.save(upload_path)
            except:
                cnt += 1
        print(file_path_list)
        size = -1
        result_list = metric_from_file(hypothesis=file_path_list[0], references=file_path_list[1], size=size)
        output_result = ''
        for result in result_list:
            output_result += '{} </br>'.format(result)
        # context['failed_number'] = cnt
        # return render_template('upload.html', **context)
        # return redirect(url_for('upload'))
        return '<p>{}</p>'.format(output_result)
    else:
        return app.send_static_file('metric.html')


if __name__ == "__main__":
    app.run(
        host='10.0.12.172',
        debug=True)
