global user
global shift


class Auth:

    @staticmethod
    def set_user(user_):
        global user
        user = user_

    @staticmethod
    def user():
        return user

    @staticmethod
    def set_shift(shift_):
        global shift
        shift = shift_

    @staticmethod
    def shift():
        return shift
