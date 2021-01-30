from main import api,app
from Controller.UserApi import UserApi
from Controller.UserListApi import UserListApi
from Controller.ScoreBoardApi import ScoreBoardApi

api.add_resource(ScoreBoardApi,"/scoreboard/<string:userguid>")
api.add_resource(UserListApi,"/user")
api.add_resource(UserApi,"/user/<string:userguid>")
if __name__ == '__main__':
    app.run(debug=True)