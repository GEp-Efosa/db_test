from .models import DbTest
from .schemas import DbTestInputSchema, DbTestResponse
from flask import Blueprint, request, jsonify 
from marshmallow import ValidationError
from .extensions import db

db_test = Blueprint('db_test', __name__, url_prefix='/api/v1.0')
db_test_input_schema = DbTestInputSchema()
db_test_response = DbTestResponse()


@db_test.route("/db_test_input/", methods = ['POST'])
def create_db_test():
    params = {**request.json}
    try:
        db_test_data = db_test_input_schema.load(params)
        db_test_data.save()
    except ValidationError as err:
        return jsonify({'error' : err.messages}), 406
    return db_test_response.dump(db_test_data), 201


@db_test.route("/db_test/status/<text>", methods = ['GET'])
def get_db_test(text):
    print("RUnning GET request...")
    db.create_all()
    db_test = DbTest.query.filter_by(string_field=text)
    db_test = db_test.order_by(-DbTest.id).first() # recent risk assessment data
    if db_test:
        return db_test_response.dump(db_test), 200
    return jsonify({"Error" : "Assessment Not Found"}), 404
