from flask import Flask, redirect, request

app = Flask(__name__)

# Define the redirect route
@app.route('/redirect')
def redirect_link():
    original_link = request.args.get('link')
    if not original_link:
        return "No link provided", 400
    return redirect(original_link)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
