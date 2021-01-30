from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with ,inputs
from Repository.dbConnector import User, Score, db
import uuid 

request_args = reqparse.RequestParser()
request_args.add_argument("userGuid", type=str, help="userGuid is requested",required=True)
request_args.add_argument("score", type=str, help="Score is requested",required=True)
request_args.add_argument("date", type=inputs.datetime_from_iso8601, help="date is requested",required=True)


class ScoreBoardApi(Resource):

   

    resorce_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'clientGuid': fields.String,
        'userGuid': fields.String
    }

    def put(self):
        _args = request_args.parse_args()
        _user = User.query.filter_by(userGuid=_args['userGuid']).scalar()
        if(_user is None):
            abort(500,message='userGuid not found.')
        
        _score = Score(score=_args['score'],date=_args['date'],user_id =_user.id)
        db.session.add(_score)
        db.session.commit()
     
        return {'scoreID':str(_score.id)}, 201

    @marshal_with(resorce_fields)
    def get(sefl):
       # userID_abort(userID)
        print(userID)
        result = User.query.filter_by(userGuid=userID).first()   
        #args = request_args.parse_args()    
        return result

  