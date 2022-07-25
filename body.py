import numpy as np
from flask import Flask, render_template, request, url_for ,send_file
import pickle as pk

app= Flask(__name__)

knn_u=pk.load(open('models/KNnUTS.pkl','rb'))
knn_f=pk.load(open('models/KNnFS.pkl','rb'))
knn_y=pk.load(open('models/KNnYS.pkl','rb'))

rf_u=pk.load(open('models/RF_UTS.pkl','rb'))
rf_f=pk.load(open('models/RF_FS.pkl','rb'))
rf_y=pk.load(open('models/RF_YS.pkl','rb'))

svm_u=pk.load(open('models/SVM_UTS.pkl','rb'))
svm_f=pk.load(open('models/SVM_FS.pkl','rb'))
svm_y=pk.load(open('models/SVM_YS.pkl','rb'))

@app.route("/")
def home ():
    return render_template("home.html")


@app.route("/a")
def about():
    return render_template("about.html")

@app.route('/download')
def download():
    a= 'Vedant Utpat.pdf'
    return send_file(a, as_attachment=True)

@app.route("/edu")
def education():
    return render_template("edu.html")


@app.route("/portf")
def portfolio():
    return render_template("portfolio.html")


@app.route("/cont",methods=['POST', 'GET'])
def contact():
    return render_template("contact.html")

@app.route("/alg")
def algopage():
    return render_template("algo.html")

@app.route("/prop_knn")
def prop_knn():
    return render_template("mtl_prop_knn.html")

@app.route("/prop_svm")
def prop_svm():
    return render_template("mtl_prop_svm.html")

@app.route("/prop_rf")
def prop_rf():
    return render_template("mtl_prop_rf.html")


@app.route("/svmu" ,methods=['POST', 'GET'])
def SVM_U(pred="0"):

    if request.method=='POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n=np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9])

        predi= svm_u.predict(n.reshape(1,9))
        title="The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred=predi[0]
        pred = float(pred)
        unit="Mpa"
        return render_template("predict - svm-u.html", title=title, U=U, output_predU=pred, unit1=unit)

    return render_template("predict - svm-u.html")


@app.route("/svmf",methods=['POST', 'GET'])
def SVM_F():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = svm_f.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - svm-f.html", title=title, U=F, output_predU=pred, unit1=unit)

    return render_template("predict - svm-f.html")


@app.route("/svmy",methods=['POST', 'GET'])
def SVM_Y():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = svm_y.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - svm-y.html", title=title, U=Y, output_predU=pred, unit1=unit)
    return render_template("predict - svm-y.html")

@app.route("/knnu",methods=['POST', 'GET'])
def KNN_U():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = knn_u.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - knn-u.html", title=title, U=U, output_predU=pred, unit1=unit)
    return render_template("predict - knn-u.html")

@app.route("/knnf",methods=['POST', 'GET'])
def KNN_F():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = knn_f.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - knn-f.html", title=title, U=F, output_predU=pred, unit1=unit)
    return render_template("predict - knn-f.html")

@app.route("/knny",methods=['POST', 'GET'])
def KNN_Y():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = knn_y.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - knn-y.html", title=title, U=Y, output_predU=pred, unit1=unit)
    return render_template("predict - knn-y.html")


@app.route("/rfu",methods=['POST', 'GET'])
def RF_U():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = rf_u.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - rf-u.html", title=title, U=U, output_predU=pred, unit1=unit)
    return render_template("predict - rf-u.html")

@app.route("/rfy",methods=['POST', 'GET'])
def RF_Y():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = rf_y.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - rf-y.html", title=title, U=Y, output_predU=pred, unit1=unit)
    return render_template("predict - rf-y.html")

@app.route("/rff",methods=['POST', 'GET'])
def RF_F():
    if request.method == 'POST':
        a1 = float(request.form["Al"])
        a2 = float(request.form["Cu"])
        a3 = float(request.form["Si"])
        a4 = float(request.form["n4"])
        a5 = float(request.form["n5"])
        a6 = float(request.form["n6"])
        a7 = float(request.form["n7"])
        a8 = float(request.form["n8"])
        a9 = float(request.form["n9"])

        n = np.array([a1, a2, a3, a4, a5, a6, a7, a8, a9])

        predi = rf_f.predict(n.reshape(1, 9))
        title = "The Predicted Strengths are - "
        U = "Ultimate Tensile Strength :"
        Y = "Yield Strength :"
        F = "Fatigue Strength :"
        pred = predi[0]
        pred = float(pred)
        unit = "Mpa"
        return render_template("predict - rf-f.html", title=title, U=F, output_predU=pred, unit1=unit)
    return render_template("predict - rf-f.html")



if __name__ == "__main__" :
    app.run(debug=True)