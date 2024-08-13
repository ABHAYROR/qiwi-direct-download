from flask import Flask, request, redirect, render_template_string
import bs4
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        try:
            # Fetch the content of the URL
            text = requests.get(url).text
            soup = bs4.BeautifulSoup(text, 'html.parser')

            # Extract file extension from h1 tag
            ext = soup.find('h1').text.split('.')[-1] if soup.find('h1') else 'html'

            # Construct new URL
            domain = 'https://spyderrock.com/'
            newurl = domain + url.split('/file/')[1] + '.' + ext

            # Redirect to the new URL
            return redirect(newurl, code=302)
        except Exception as e:
            return f"An error occurred: {str(e)}", 500

    # If it's a GET request or first load, show the form
    return render_template_string('''
    <form method="post">
        <label for="url">Enter link:</label>
        <input type="text" id="url" name="url" required>
        <input type="submit" value="Submit">
    </form>
    ''')

# This route can be used to update the domain if needed
@app.route('/update_domain', methods=['POST'])
def update_domain():
    global domain
    new_domain = request.form.get('new_domain')
    if new_domain:
        domain = new_domain
        return "Domain updated successfully", 200
    return "No domain provided", 400

if __name__ == '__main__':
    app.run(debug=True)
