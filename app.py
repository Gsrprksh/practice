from flask import Flask, render_template, request, url_for, redirect, Response, send_file, jsonify
import pandas as pd
import pyodbc
import numpy as np


app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods = ['POST','GET'])
def result():
    x = request.form['user_id']
    y = request.form['password']
    conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'SURYA\SQLEXPRESS', database = 'user_information', trusted_connection ='yes')
    query = 'SELECT* from user_information.dbo.USERSINFORMATION'
    df = pd.read_sql(query, con = conn)
    z = df.values.tolist()
    for i in range(len(z)):
        if (z[i][0] == x) & (z[i][1] == y):
            return render_template('result.html')
    return render_template('create.html')


@app.route('/create', methods = ['POST','GET'])
def create():
    x1 = request.form['user_id']
    y1 = request.form['password']
    z1 = [x1, y1]
    conn = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',host = 'SURYA\SQLEXPRESS', database = 'user_information', trusted_connection ='yes')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO user_information.dbo.USERSINFORMATION VALUES (?,?)''',z1)
    cursor.commit()
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug = True)