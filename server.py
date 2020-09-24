from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

#home route
@app.route('/')
def my_home():  #default parameters
    #return 'Hellooooooo!'
    return render_template('index.html')


@app.route('/<pagename>')
def load_page(pagename):
    # show the corrosponding page for that user
    return render_template(pagename)

#store the data sent to server through contact form
def write_to_file(data):
     with open ('database.txt','a') as database:
            email = data['email']
            subject = data['subject']
            message = data['message']
            file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
     with open ('database.csv', newline='', mode='a') as database2:
            email = data['email']
            subject = data['subject']
            message = data['message']
            
            csv_writer = csv.writer(database2, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == "POST":
        try:

            #get the form data as dictionary
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Did not save to database"
    return 'Something went wrong..Try again!!'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

