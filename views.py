from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template("index.html", name="Mayrcon", page="Home Page")

# @views.route('/profile/<username>')
# def profile(username):
#     return render_template("index.html", name=username, page="Profile Page")
# http://127.0.0.1:8000/views/profile/Teste
@views.route('/profile')
def profile():
    args = request.args
    # name = args.get('name')
    name = args.post('name')
    return render_template("index.html", name=name, page="Profile Page")
    # http://127.0.0.1:8000/views/profile
@views.route('/json')
def get_json():
    
    return jsonify({'name': 'Mayrcon', 'age': 33})
    # http://127.0.0.1:8000/views/json
@views.route('/data')
def get_data():
    data = request.json
    return jsonify(data)
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))