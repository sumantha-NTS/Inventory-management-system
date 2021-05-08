from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

scalar_week = pickle.load(open('pickle_files/scale_week.pkl','rb'))
scalar_month = pickle.load(open('pickle_files/scale_month.pkl','rb'))
scalar_quarter = pickle.load(open('pickle_files/scale_quarter.pkl','rb'))

week_model = pickle.load(open('pickle_files/week.pkl','rb'))
month_model = pickle.load(open('pickle_files/month.pkl','rb'))
quarter_model = pickle.load(open('pickle_files/quarter.pkl','rb'))


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/analysis',methods=['POST'])
def analysis():
    global y;
    y = request.form['analysis']
    if y == 'weekly':
        return render_template('week.html')

    elif y == 'monthly':
        return render_template('month.html')

    else:
        return render_template('quarter.html')

@app.route('/predict',methods=['POST'])
def predict():
    if y == 'weekly':
        week = request.form["Week"]
        month = request.form["Month"]
        product = request.form["product_type"]
        promotion = request.form["promotion"]
        holiday = request.form["Holiday"]
        x = [int(product), int(promotion), int(holiday),int(week), int(month)]

        # scaling the input
        input = pd.DataFrame(scalar_week.transform([x]),
                             columns=['Product_type','Promotion_applied', 'Generic_Holiday','updated_week','updated_month'])

        # predicting
        result = np.round(np.exp(week_model.predict(input)) * 1.1, 0)
        return render_template('predict.html',res=[product,int(result)])

    elif y == 'monthly':
        month = request.form["Month"]
        product = request.form["product_type"]
        promotion = request.form["promotion"]
        holiday = request.form["Holiday"]
        x = [int(month), int(product), int(holiday),int(promotion) ]

        # scaling the input
        input = pd.DataFrame(scalar_month.transform([x]),
                             columns=['updated_month', 'Product_type', 'Generic_Holiday','Promotion_applied'])

        # predicting
        result = np.round(np.exp(month_model.predict(input)) * 1.1, 0)
        return render_template('predict.html',res=[product,int(result)])

    else:
        quarter = request.form["Quarter"]
        product = request.form["product_type"]
        promotion = request.form["promotion"]
        holiday = request.form["Holiday"]
        x = [int(quarter), int(product), int(holiday),int(promotion) ]

        # scaling the input
        input = pd.DataFrame(scalar_quarter.transform([x]),
                             columns=['quarter', 'Product_type', 'Generic_Holiday','Promotion_applied'])

        # predicting
        result = np.round(np.exp(quarter_model.predict(input)) * 1.1, 0)
        return render_template('predict.html',res=[product,int(result)])


if __name__ == "__main__":
    app.run(debug=True)