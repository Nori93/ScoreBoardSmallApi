
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with 
from Repository.dbConnector import User,db
import uuid 

user_args = reqparse.RequestParser()
user_args.add_argument("username",type=str, help="username is requested",required=True)
user_args.add_argument("clientGuid",type=str, help="guid is requested", required=True)


class UserApi(Resource):
   

    scoreList_fields = {
        'id': fields.Integer,
        'score_value':fields.String,
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

   
    def put(self,userguid):
        _args = user_args.parse_args()        
        if(User.query.filter_by(clientGuid=_args['clientGuid']).scalar() is not None):
            abort(500,message='clientGuid is taked')

        _guid = uuid.uuid1()
        _user = User(name=_args['username'],clientGuid=_args['clientGuid'],userGuid =str(_guid))
        db.session.add(_user)
        db.session.commit()
        return {'key':str(_guid)},201

    @marshal_with(userList_fields)
    def get(self,userguid):
        result = User.query.filter_by(userGuid=userguid).options(db.lazyload('score_list')).all()
        return result;

   