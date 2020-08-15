from flask import Flask, render_template, request, redirect, url_for
import test

app = Flask('__name__')

@app.route('/', methods=['POST','GET'])
def webScraperInput():
    if request.method == 'POST':
        keywords = str(request.form['keywords'])
        language = str(request.form['language'])
        nbr = str(request.form['nbr'])
        df = test.get_info(keywords, int(nbr), language, 'output.csv',
                           ['facebook', 'instagram', 'youtube', 'twitter', 'wiki'])
        return render_template('results.html', tables=[df.to_html(classes='data', header="true")])
    else: 
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
