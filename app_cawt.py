
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#from app import app
import subprocess
from subprocess import Popen
import sys
import cgi, cgitb
import pdb

# from prediction import predict_element


@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
@app.route('/static/assets/vendor/bootstrap/css/bootstrap.min.css')
@app.route('/static/assets/vendor/jquery/jquery.min.js')
@app.route('/static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js')
@app.route('/static/assets/vendor/bootstrap/js/bootstrap.bundle.min.js')
@app.route('/static/assets/vendor/counterup/counterup.min.js')
@app.route('/static/assets/vendor/php-email-form/validate.js')
@app.route('/static/assets/vendor/waypoints/jquery.waypoints.min.js')
@app.route('/static/assets/vendor/jquery.easing/jquery.easing.min.js')
@app.route('/static/assets/vendor/isotope-layout/isotope.pkgd.min.js')
@app.route('/static/assets/vendor/venobox/venobox.min.js')
@app.route('/static/assets/vendor/owl.carousel/owl.carousel.min.js')
@app.route('/static/assets/js/main.js')
@app.route('/static/assets/vendor/icofont/icofont.min.css')
@app.route('/static/assets/vendor/boxicons/css/boxicons.min.css')
@app.route('/static/assets/vendor/venobox/venobox.css')
@app.route('/static/assets/vendor/owl.carousel/assets/owl.carousel.min.css')
@app.route('/static/assets/css/style.css')
@app.route('/static/assets/img/about.png')
@app.route('/static/assets/img/hero-img.png')
@app.route('/static/assets/vendor/jquery.easing/jquery.easing.min.js')
@app.route('/static/assets/vendor/php-email-form/validate.js')
@app.route('/static/assets/vendor/waypoints/jquery.waypoints.min.js')
@app.route('/static/assets/vendor/isotope-layout/isotope.pkgd.min.js')
@app.route('/static/assets/vendor/venobox/venobox.min.js')
@app.route('/static/assets/vendor/owl.carousel/owl.carousel.min.js')
@app.route('/static/assets/js/main.js')
@app.route('/static/assets/img/apple-touch-icon.png')
@app.route('/static/assets/img/about.png')
@app.route('/static/assets/img/favicon.png')

def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    #render_template('index.html', title='Home', user=user, posts=posts)
    return render_template('index.html')

@app.route('/hadoop_new_folder', methods=['POST'])
@cross_origin()
def hadoop_new_folder():
    path=request.get_json()["path"]
    full_command = 'hadoop dfs -mkdir ' + path
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200


@app.route('/hadoop_delete_folder', methods=['POST'])
@cross_origin()
def hadoop_delete_folder():
    path=request.get_json()["path"]
    full_command = 'hadoop dfs -rm -r '+ path
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200


@app.route('/hadoop_upload_data', methods=['POST'])
@cross_origin()
def hadoop_upload_data():
    local_path=request.get_json()["local_path"]
    hdfs_path=request.get_json()["hdfs_path"]
    full_command = 'hadoop dfs -put '+ "/home/"+local_path+ ' ' + hdfs_path
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200

    
@app.route('/hadoop_upload_data2', methods=['POST'])
@cross_origin()
def hadoop_upload_data2():
    # Example: /local_path/new_data  /hdfs_path
    # hadoop dfs -put /home/ubuntu/data_covid/csv_covi19 /test_new_delete
    print(request.get_json())
    file = request.files['File']
    print(file.name)
    file.save("/home/"+file.name)
    hdfs_path=request.get_json()["hdfsPath"]
    full_command = 'hadoop dfs -put '+ "/home/"+file.name + ' ' + hdfs_path
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200


@app.route('/hadoop_download_folder', methods=['POST'])
@cross_origin()
def hadoop_download_folder():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    local_path=request.get_json()["local_path"]
    hdfs_path=request.get_json()["hdfs_path"]
    full_command = 'hadoop dfs -get '+ hdfs_path + ' ' + local_path
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200


@app.route('/ElemNet_code', methods=['POST'])
@cross_origin()
def ElemNet_code():
    # Example: remember to have the corret path, <full_path>/name_file.py e.i. ~/ElemNet/elemnet/dl_regressors.py
    # and <initial_path>/sample/sample-run.config   e.i. ~/ElemNet/elemnet/sample/sample-run.config 
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = '/opt/hadoopspark/spark-3.0.2-bin-hadoop3.2/bin/spark-submit --master yarn --deploy-mode client 
/home/chemical-compunt-analysis/elemnet/dl_regressors.py --config_file 
/home/chemical-compunt-analysis/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200

@app.route('/IrNet_code', methods=['POST'])
@cross_origin()
def IrNet_code():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = '/opt/hadoopspark/spark-3.0.2-bin-hadoop3.2/bin/spark-submit --master yarn --deploy-mode client 
/home/chemical-compunt-analysis/elemnet/dl_regressors_irnet.py --config_file 
/home/chemical-compunt-analysis/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200

@app.route('/IrNet6_code', methods=['POST'])
@cross_origin()
def IrNet6_code():
    full_command = '/opt/hadoopspark/spark-3.0.2-bin-hadoop3.2/bin/spark-submit --master yarn --deploy-mode client 
/home/chemical-compunt-analysis/elemnet/irnet6.py '
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200


@app.route('/SVM_code', methods=['POST'])
@cross_origin()
def SVM_code():
    # Example: /ocal_path/new_data  /hdfs_path
    # hadoop dfs -get /test_new_delete/csv_covi19  /home/ubuntu
    #local_path = request.form['dpath_localFile']
    #hdfs_path = request.form['dpath_hdfsFile']
    full_command = 'spark-submit --master yarn --deploy-mode client ~/ElemNet/elemnet/dl_regressors_svm_spark.py --config_file 
~/ElemNet/elemnet/sample/sample-run.config'
    p = Popen(full_command , shell=True)
    return jsonify(Message="Command executed."), 200             


@app.route('/execute_command', methods=['POST'])
@cross_origin()
def execute_command():
    command=request.get_json()["command"]
    full_command = command
    try:
        p = Popen(full_command, stdout=subprocess.PIPE,shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        print("Command output : ",output.decode())
        return jsonify(Message="Success",output=output.decode()), 200
    except ValueError:
        print("--------error",ValueError)
        return jsonify(Message="Error"), 500
    


@app.route('/predict', methods=['POST'])
@cross_origin()
def prediction():
    elements=request.get_json()["elements"]
    values=request.get_json()["values"]
    print(elements,values)    
    try:
        p = Popen(["/root/anaconda3/bin/conda","run","-n","env","python","prediction.py",str(elements),str(values)],
          stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
        (output, err) = p.communicate()
        p_status = p.wait()
        index = output.find(b"error")
        if index != -1:
            return jsonify(Message="Error"), 500
            
        print("Command output : ",output.decode())
        return jsonify(Message="Success",output=output.decode()), 200
    except ValueError:
        print("--------error",ValueError)
        return jsonify(Message="Error"), 500
    


