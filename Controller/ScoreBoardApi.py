from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with ,inputs
from Repository.dbConnector import User, Score, db
from sqlalchemy import func
import uuid 

request_args = reqparse.RequestParser()
request_args.add_argument("userGuid", type=str, help="userGuid is requested",required=True)
request_args.add_argument("score", type=str, help="Score is requested",required=True)
request_args.add_argument("date", type=inputs.datetime_from_iso8601, help="date is requested",required=True)


class ScoreBoardApi(Resource): 

    scoreboard_fields = {      
        'username':fields.String,  
        'score_value': fields.Float,
        'date': fields.String        
    }

    @marshal_with(scoreboard_fields)
    def get(sefl):     
        
        _score = Score.query.order_by(Score.score_value.desc()).group_by(Score.user_id).having(func.max(Score.score_value)).all()
        for sc in _score:
            _user = User.query.filter_by(id=sc.user_id).scalar();
            sc.username = _user.name
        return _score

  