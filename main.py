from flask import Flask, render_template, request, jsonify
import math
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])  # This will be called from UI
def math_operation():
    if (request.method=='POST'):
        try:
            operation=request.form['operation']
            num1=int(request.form['num1'])
            num2 = int(request.form['num2'])
        except:
            return "enter the valid number"
        if (operation == 'add'):
            try:
                r = num1 + num2
                result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Addition"
        if (operation == 'subtract'):
            try:
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Subtraction"
        if (operation == 'multiply'):
            try:
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Multiplication"
        if (operation == 'divide'):
            try:
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Division"
        if (operation == 'power of'):
            try:
                r = num1 ** num2
                result = 'the value when ' + str(num1) + ' is powered of by ' + str(num2) + ' the value is ' + str(r)
            except:
                return "Enter the appropriate numbers for powering of"
        if (operation == 'greater than'):
            try:
                if num1 > num2:
                    r = num1 - num2
                    result = str(num1) + ' is greater than ' + str(num2) + ' by ' + str(r)
                else:
                    r = num2 - num1
                    result = str(num2) + ' is greater than ' + str(num1) + ' by ' + str(r)
            except:
                return "Enter the appropriate numbers for finding greater of"
        if (operation == 'lesser than'):
            try:
                if num1 < num2:
                    r = num2 - num1
                    result = str(num1) + ' is lesser  than ' + str(num2) + ' by ' + str(r)
                else:
                    r = num1 - num2
                    result = str(num2) + ' is lesser than ' + str(num1) + ' by ' + str(r)
            except:
                return "Enter the appropriate numbers for finding lesser than"
        if (operation == 'equal to'):
            try:
                if num1 == num2:
                    result = str(num1) + ' is equal to ' + str(num2)
                else:
                    result = str(num1) + ' is not equal to ' + str(num2)
            except:
                return "Enter the appropriate numbers for finding equal to"
        if (operation == 'square root'):
            try:
                result1 = math.sqrt(num1)
                result2 = math.sqrt(num2)
                result = "The Square root of Value1 and Value2 is " + str(result1) + ' and ' + str(
                    result2) + ' respectively '
            except:
                return "Enter the appropriate numbers for finding square root"
        if (operation == 'cube root'):
            try:
                result1 = round(math.pow(num1, 1 / 3))
                result2 = round(math.pow(num2, 1 / 3))
                result = "The Cube root of Value1 and Value2 is " + str(result1) + ' and ' + str(result2) + ' respectively '
            except:
                return "Enter the appropriate numbers for finding cube root"
        if (operation == 'percent of'):
            try:
                result1 = round((num1 / num2) * 100)
                result = "The Value1 is " + str(result1) + ' % of ' + 'Value2'
            except:
                return "Enter the appropriate numbers for finding the percentage of"
        if (operation == 'difference'):
            try:
                result1 = abs(num1 - num2)
                result = "The difference between Value1 and Value2 is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == '(a+b)2'):
            try:
                result1 = (num1 ** 2 + num2 ** 2 + 2 * num1 * num2)
                result = "The (Value1+Value2)^2 value is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == '(a-b)2'):
            try:
                result1 = (num1 ** 2 + num2 ** 2 - 2 * num1 * num2)
                result = "The (Value1-Value22)^2 value is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == 'cube of'):
            try:
                result1 = (num1 * num1 * num1)
                result2 = (num2 * num2 * num2)
                result = "The Cube value of Value1 and Value2 is " + str(result1) + ' and ' + str(result2) + ' respectively'
            except:
                return "Enter the valid number"
        return render_template('results.html',result=result)

@app.route('/via_postman', methods=['POST']) # for calling the API from Postman/SOAPUI
def math_operation_via_postman():
    if (request.method=='POST'):
        try:
            operation=request.json['operation']
            num1=int(request.json['num1'])
            num2 = int(request.json['num2'])
        except:
            return "enter the valid number"
        if(operation=='add'):
            try:
                r=num1+num2
                result= 'the sum of '+str(num1)+' and '+str(num2) +' is '+str(r)
            except:
                return "Enter the appropriate numbers for Addition"
        if (operation == 'subtract'):
            try:
                r = num1 - num2
                result = 'the difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Subtraction"
        if (operation == 'multiply'):
            try:
                r = num1 * num2
                result = 'the product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Multiplication"
        if (operation == 'divide'):
            try:
                r = num1 / num2
                result = 'the quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
            except:
                return "Enter the appropriate numbers for Division"
        if (operation == 'power of'):
            try:
                r = num1 ** num2
                result = 'the value when ' + str(num1) + ' is powered of by ' + str(num2) + ' the value is ' + str(r)
            except:
                return "Enter the appropriate numbers for powering of"
        if (operation == 'greater than'):
            try:
                if num1 > num2:
                    r = num1 - num2
                    result = str(num1) + ' is greater than ' +str(num2) + ' by ' +str(r)
                else:
                    r = num2 - num1
                    result = str(num2) + ' is greater than ' + str(num1) + ' by ' + str(r)
            except:
                return "Enter the appropriate numbers for finding greater of"
        if (operation == 'lesser than'):
            try:
                if num1 < num2:
                    r = num2 - num1
                    result = str(num1) +' is lesser  than ' + str(num2) +' by ' +str(r)
                else:
                    r = num1 - num2
                    result = str(num2) + ' is lesser than ' + str(num1) + ' by ' + str(r)
            except:
                return "Enter the appropriate numbers for finding lesser than"
        if (operation == 'equal to'):
            try:
                if num1 == num2:
                     result = str(num1) + ' is equal to ' + str(num2)
                else:
                     result = str(num1) + ' is not equal to ' + str(num2)
            except:
                return "Enter the appropriate numbers for finding equal to"
        if (operation == 'square root'):
            try:
                result1 = math.sqrt(num1)
                result2 = math.sqrt(num2)
                result = "The Square root of Value1 and Value2 is " + str(result1) + ' and '+ str(result2) + ' respectively '
            except:
                return "Enter the appropriate numbers for finding square root"
        if (operation == 'cube root'):
            try:
                result1 = round(math.pow(num1, 1/3))
                result2 = round(math.pow(num2, 1/3))
                result = "The Cube root of Value1 and Value22 is " + str(result1) + ' and ' + str(result2) + ' respectively '
            except:
                return "Enter the appropriate numbers for finding cube root"
        if (operation == 'percent of'):
            try:
                result1 = round((num1/num2) * 100)
                result = "The Value1 is " + str(result1) + ' % of ' + 'Value22'
            except:
                return "Enter the appropriate numbers for finding the percentage of"
        if (operation == 'difference'):
            try:
                result1 = abs(num1-num2)
                result = "The difference between Value1 and Value2 is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == '(a+b)2'):
            try:
                result1 = (num1**2 + num2**2 + 2*num1*num2)
                result = "The (Value1+Value2)^2 value is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == '(a-b)2'):
            try:
                result1 = (num1**2 + num2**2 - 2*num1*num2)
                result = "The (Value1-Value2)^2 value is " + str(result1)
            except:
                return "Enter the valid number"
        if (operation == 'cube of'):
            try:
                result1 = (num1*num1*num1)
                result2 = (num2*num2*num2)
                result = "The Cube value of Value1 and Value2 is " + str(result1) + ' and '+ str(result2) + ' respectively'
            except:
                return "Enter the valid number"
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
