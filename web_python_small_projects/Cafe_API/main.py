from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
from werkzeug.exceptions import NotFound

"""i should make similar to this site https://laptopfriendly.co/london for banglore"""
#published at
"""https://documenter.getpostman.com/view/39835329/2sAYBUCriU"""

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        # #Method 1 :
        # dictionary = {}
        #
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # OR METHOD 2:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()

ALL_CAFE_LIST = []


def fetch_all_cafe():
    global ALL_CAFE_LIST
    with app.app_context():
        cafe_table = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
        ALL_CAFE_LIST = [{
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price,
        }
            for cafe in cafe_table]
    return ALL_CAFE_LIST


@app.route("/")
def home():
    # fetch_all_cafe()
    # print(ALL_CAFE_LIST)
    return render_template("index.html")


# random() route alternative
# @app.route("/random")
# def get_random_cafe():
#     result = db.session.execute(db.select(Cafe))
#     all_cafes = result.scalars().all()
#     random_cafe = choice(all_cafes)
#     # return jsonify(cafe={
#     #
#     #     "name": random_cafe.name,
#     #     "map_url": random_cafe.map_url,
#     #     "img_url": random_cafe.img_url,
#     #     "location": random_cafe.location,
#     #     "amenities": {
#     #         "seats": random_cafe.seats,
#     #         "has_toilet": random_cafe.has_toilet,
#     #         "has_wifi": random_cafe.has_wifi,
#     #         "has_sockets": random_cafe.has_sockets,
#     #         "can_take_calls": random_cafe.can_take_calls,
#     #         "coffee_price": random_cafe.coffee_price,
#     #     }
#     # })
#     return jsonify(cafe=random_cafe.to_dict())


@app.route("/random", methods=["GET", "POST"])
def random():
    fetch_all_cafe()
    cafe = choice(ALL_CAFE_LIST)
    return jsonify(cafe={"name": cafe['name'], "map_url": cafe['map_url'], "img_url": cafe['img_url'],
                         "location": cafe['location'], "seats": cafe['seats'], "coffee_price": cafe['coffee_price'],
                         "amenities":
                             {"has_toilet": cafe['has_toilet'],
                              "has_wifi": cafe['has_wifi'],
                              "has_sockets": cafe['has_sockets'],
                              "can_take_calls": cafe['can_take_calls']},

                         })


@app.route("/all", methods=["GET", "POST"])
def get_all_cafes():
    return jsonify(cafes=fetch_all_cafe())

@app.route("/search", methods=["GET", "POST"])
def get_cafe_at_location():
    loc = request.args.get("loc")
    # http://127.0.0.1:5000/search?loc=Peckham
    if not loc:
        return jsonify({"error": "location parameter missing"}), 400  # Bad Request
    with app.app_context():
        condition = Cafe.location.like(f"%{loc}%")
        location_search_result = db.session.execute(
            db.select(Cafe).where(condition).order_by(Cafe.name)).scalars().all()
        if location_search_result:
            return jsonify(cafes=[cafe.to_dict() for cafe in location_search_result])
        else:
            return jsonify(error={
                "Not Found": "Sorry, we don't have a cafe at '{}'.".format(loc)
            }), 404


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        new_cafe = Cafe(name=request.form['name'],
                        map_url=request.form['map_url'],
                        img_url=request.form['img_url'],
                        location=request.form['location'],
                        seats=request.form['seats'],
                        has_toilet=bool(request.form['has_toilet']),
                        has_wifi=bool(request.form['has_wifi']),
                        has_sockets=bool(request.form['has_sockets']),
                        can_take_calls=bool(request.form['can_take_calls']),
                        coffee_price=request.form['coffee_price'])
        db.session.add(new_cafe)
        db.session.commit()
        # print("name:", new_cafe.name, new_cafe.map_url)
        return jsonify(response={"success": "Successfully added the new cafe"})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        update_cafe_price = db.get_or_404(Cafe, ident=cafe_id)
    except NotFound:
        return jsonify({"message": "Cafe not found", "error": "404"}), 404

    new_coffee_price = request.args.get('coffee_price')
    update_cafe_price.coffee_price = new_coffee_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price"})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    try:
        cafe = db.get_or_404(Cafe, ident=cafe_id)
    except NotFound:
        return jsonify({"message": "Cafe not found", "error": "404"}), 404
    api_key = request.args.get('api-key')
    if api_key == "MyTopSecretKey":
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": f"Successfully deleted the cafe- {cafe.name}"}),200
    else:
        return jsonify(failed={"error": "Sorry , that's not allowed .Make Sure you have the correct api_key"})


# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
