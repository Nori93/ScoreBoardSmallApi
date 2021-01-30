
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with 
from Repository.dbConnector import User,db

class UserListApi(Resource):
   

    scoreList_fields = {
        'id': fields.Integer,
        'score_value':fields.Float,
        'date':fields.DateTime,
        'user_id':fields.Integer
    }

    userList_fields = {        
            'id': fields.Integer,
            'name': fields.String,
            'clientGuid': fields.String,
            'userGuid': fields.String,
            'score_list': fields.List(fields.Nested(scoreList_fields))
    }

    @marshal_with(userList_fields)
    def get(self):
        result = User.query.options(db.lazyload('score_list')).all()
        return result;

   