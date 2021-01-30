from main import api,app
from Controller.UserApi import UserApi
from Controller.UserListApi import UserListApi
from Controller.ScoreApi import ScoreApi
from Controller.ScoreBoardApi import ScoreBoardApi

api.add_resource(ScoreApi,"/scoreboard/<string:userguid>")
api.add_resource(ScoreBoardApi,"/scoreboard")

api.add_resource(UserApi,"/user/<string:userguid>")
api.add_resource(UserListApi,"/userlist")

if __name__ == '__main__':
    app.run(debug=True)