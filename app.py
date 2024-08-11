from flask import Flask, request, render_template_string
import bs4
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def scrape():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        try:
            text = requests.get(url).text
            soup = bs4.BeautifulSoup(text, 'html.parser')
            ext = soup.find('h1').text.split('.')[-1]  # Get the file extension
            domain = 'https://spyderrock.com/'  # This will probably need to be updated frequently
            newurl = domain + url.split('/file/')[1] + '.' + ext
            result = newurl
        except Exception as e:
            result = f"An error occurred: {str(e)}"

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Web Scraper</title>
        </head>
        <body>
            <h1>Web Scraper</h1>
            <form method="post">
                <input type="text" name="url" placeholder="Enter link">
                <input type="submit" value="Scrape">
            </form>
            {% if result %}
            <h2>Result:</h2>
            <p>{{ result }}</p>
            {% endif %}
        </body>
        </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
