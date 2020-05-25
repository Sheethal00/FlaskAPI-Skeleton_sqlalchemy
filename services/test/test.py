# from __main__ import app
from __main__ import api, config, dev_config, debug
from flask_restful import Resource
from flask import request
import json
import sys
from DB.test.hello_db import db, Get_Post

class test(Resource):
    def get(self):
        try:
            ret_obj = {
                "status" : "success",
                "success" : True,
                "data" : {
                    "test" : "Test Successful"
                }
            }
            ret_status = 200
            return ret_obj, ret_status
        except Exception as e:
            ret_obj = {
                "status" : "failure",
                "success" : False,
                "error" : {
                    "id" : "",
                    "message" : str(e)
                }
            }
            ret_status = 500
            return ret_obj, ret_status


class hello(Resource):        
    def get(self):
        print(Get_Post.query.all())
        row = Get_Post.query.all()[0]
        print(Get_Post.query.all())
        try:
            ret_obj = {
                "status" : row.status,
                "success" : bool(row.success),
                "data" : {
                    row.data_key : row.data_value
                }
            }
            ret_status = row.return_code
            return ret_obj, ret_status

        except Exception as e:

            ret_obj = {
                "status" : "failure",
                "success" : False,
                "error" : {
                    "id" : "",
                    "message" : str(e)
                }
            }
            ret_status = 500

            return ret_obj, ret_status

    def post(self):
        try:
            st = "success"
            succ = 1
            dt_key = "Hello"
            dt_value = "Hello Bro"
            rt_code = 200
            obj = Get_Post(status = st,success = succ,data_key = dt_key,data_value = dt_value,return_code = rt_code)
            db.session.add(obj)
            db.session.commit()
            ret_obj = {
                "status" : st,
                "success" : succ,
                "data" : {
                    dt_key : dt_value
                },
                "message" : "Data posted successfully"
            }
            ret_status = rt_code
            return ret_obj,ret_status
        except Exception as e:
            ret_obj = {
                "status" : "failure",
                "success" : False,
                "error" : {
                    "id" : "",
                    "message" : str(e)
                }
            }
            ret_status = 500
            return ret_obj, ret_status

class hello_name(Resource):
    def get(self, name):
        try:
            ret_obj = {
                "status" : "success",
                "success" : True,
                "data" : {
                    "hello" : "Hello "+name
                }
            }
            ret_status = 200

            return ret_obj, ret_status
        except Exception as e:
            ret_obj = {
                "status" : "failure",
                "success" : False,
                "error" : {
                    "id" : "",
                    "message" : str(e)
                }
            }
            ret_status = 500

            return ret_obj, ret_status



api.add_resource(test, '/test', resource_class_kwargs={})
api.add_resource(hello, '/hello', resource_class_kwargs={})
api.add_resource(hello_name, '/hello/<string:name>', resource_class_kwargs={})
