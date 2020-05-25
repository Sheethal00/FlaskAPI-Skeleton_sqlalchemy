from __main__ import api
from flask_restful import Resource
from flask import request
import json
import sys
from DB.home.home_db import db, Get_Post


class home(Resource):    
    def get(self):
        print(Get_Post.query.all())
        row = Get_Post.query.all()[0]
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

api.add_resource(home, '/', resource_class_kwargs={})
