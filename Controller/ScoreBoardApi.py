from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with ,inputs
from Repository.dbConnector import User, Score, db
import uuid 

request_args = reqparse.RequestParser()
request_args.add_argument("userGuid", type=str, help="userGuid is requested",required=True)
request_args.add_argument("score", type=str, help="Score is requested",required=True)
request_args.add_argument("date", type=inputs.datetime_from_iso8601, help="date is requested",required=True)


class ScoreBoardApi(Resource): 

    scoreboard_fields = {
        'id': fields.Integer,
        'score_value': fields.Float,
        'date': fields.String,
        'user_id': fields.String
    }

    @marshal_with(scoreboard_fields)
    def get(sefl):     
        
        _score = Score.query.order_by(Score.score_value).all()
        #args = request_args.parse_args()    
        return _score

  