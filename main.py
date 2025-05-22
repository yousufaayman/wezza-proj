from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, User,Venue,Admin,Makeupartist,Weddingplanner,Hairdresser,Venuedetails  # adjust import path if needed

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

app.secret_key = "your_secret_key"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()



# html routes


@app.route("/")
def home():
    return render_template("home_page.html") 

@app.route("/booking")
def booking():
    return render_template("booking.html")

@app.route("/hairdresser")
def hairdresser():
    return render_template("hair_dresser.html")

@app.route("/weddingplanner")
def weddingplanner():
    return render_template("wedding_planner.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/makeupartist")
def makeupartist():
    return render_template("makeup_artist.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/venuedetails/<string:name>')
def venue_details(name):
    venues = Venue.query.all()
    print("All usernames:", [v.username for v in venues])
    print("Requested:", name)
    venue = Venue.query.filter_by(username=name).first()
    if venue:
        return render_template('venue_details.html', venue=venue)
    else:
        return "Venue not found", 404

@app.route('/hairdresserdetails/<string:name>')
def hairdresser_details(name):
    print("Requested venue username:", name)
    hairdresser = Hairdresser.query.filter_by(username=name).first()
    if hairdresser:
        print("hairdresser found:", hairdresser.username)
        return render_template('hairdresser_details.html', hairdresser=hairdresser)
    else:
        print("hairdresser not found in DB for username:", name)
        return "hairdresser not found", 404

@app.route('/makeupartistdetails/<string:name>')
def makeupartist_details(name):
    print("Requested venue username:", name)
    makeupartist = Makeupartist.query.filter_by(username=name).first()
    if makeupartist:
        print("makeup found:", makeupartist.username)
        return render_template('makeupartist_details.html', makeupartist=makeupartist)
    else:
        print("makeup not found in DB for username:", name)
        return "makeup not found", 404
    
@app.route('/weddingplannerdetails/<string:name>')
def weddingplanner_details(name):
    print("Requested venue username:", name)
    weddingplanner = Weddingplanner.query.filter_by(username=name).first()
    if weddingplanner:
        print("wedding found:", weddingplanner.username)
        return render_template('weddingplanner_details.html', weddingplanner=weddingplanner)
    else:
        print("wedding not found in DB for username:", name)
        return "wedding not found", 404

@app.route("/venue")
def venue():
    #YOUSUF
    venues = Venue.query.all()
    return render_template("venue.html", venues=venues)














# controller routes 




@app.before_request
def log_request_info():
    print("----- New Request -----")
    print(f"Method: {request.method}")
    print(f"URL: {request.url}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Body: {request.get_data(as_text=True)}")
    print("------------------------")

@app.route('/login_user', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    role_model = {
        "user": User,
        "venue": Venue,
        "hair_dresser": Hairdresser,
        "makeup_artist": Makeupartist,
        "wedding_planner": Weddingplanner,
        "admin": Admin
    }.get(role)

    if not role_model:
        return jsonify({"result": "Invalid role"}), 400

    user = role_model.query.filter_by(username=username, password=password).first()

    if user:
        session['username'] = user.username
        return jsonify({"result": "success"})
    else:
        return jsonify({"result": "Invalid username or password"}), 401


@app.route('/register_user', methods=['POST'])
def register_user():


    select_value= request.json.get('select_value')
    print(request.json)
    print("heeree kkk",select_value)
    if select_value == "user":
        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        email = request.json.get('email')

        new_user = User(
            
            username=username,
            password=password,
            email=email,
            phone_number=phone_number,
           
        )
        db.session.add(new_user)
        db.session.commit()

        print (username,password,phone_number,email)
        return {'type': "user"}
    

    elif select_value == "admin":

        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        email = request.json.get('email')

        print (username,password,phone_number,email)
        new_user = Admin(
            username=username,
            password=password,
            email=email,
            phone_number=phone_number,
           
        )
        db.session.add(new_user)
        db.session.commit()
        return {'type': "admin"}


    elif select_value == "venue":

        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        description = request.json.get('description')
        location = request.json.get('location')
        price = request.json.get('price')
        media = request.json.get('media')


        print (username,password,phone_number,description,location,price,media)

        new_user = Venue(
           
            username=username,
            password=password,
            phone_number=phone_number,
            description=description,
            location=location,
            price=price,
            media=media
           
        )
        db.session.add(new_user)
        db.session.commit()
        return {'type': "venue"}

    elif select_value == "hair_dresser":

        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        description = request.json.get('description')
        location = request.json.get('location')
        price = request.json.get('price')
        media = request.json.get('media')
        

        print (username,password,phone_number,description,location,price,media)

        new_user = Hairdresser(
            username=username,
            password=password,
            phone_number=phone_number,
            description=description,
            location=location,
            price=price,
            media=media
           
        )
        db.session.add(new_user)
        db.session.commit()

        return {'type': "hair-dresser"}


    elif select_value == "wedding_planner":

        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        description = request.json.get('description')
        price = request.json.get('price')
        media = request.json.get('media')
        

        print (username,password,phone_number,description,price,media)
        new_user = Weddingplanner(
            username=username,
            password=password,
            phone_number=phone_number,
            description=description,
            price=price,
            media=media
           
        )
        db.session.add(new_user)
        db.session.commit()
        return {'type': "wedding-planner"}
    
    elif select_value == "makeup_artist":

        username= request.json.get('username')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        description = request.json.get('description')
        location = request.json.get('location')
        price = request.json.get('price')
        media = request.json.get('media')
        

        print (username,password,phone_number,description,location,price,media)
        new_user = Makeupartist(
            username=username,
            password=password,
            phone_number=phone_number,
            description=description,
            location=location,
            price=price,
            media=media
           
        )
        db.session.add(new_user)
        db.session.commit()
        print("alii")
        return jsonify({"success": True, "message": "Welcome to our dashboard"})

    
    return jsonify({"success": True, "type": select_value})




if __name__ == '__main__':
    app.run(debug=True, port=5001)


