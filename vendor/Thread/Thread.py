from .Request import Request


class Thread:
    def __init__(self, function):
        if not callable(function):
            raise TypeError(f'{function} must be a function').with_traceback(None)

        self.__function = function
        self.__thead = None
        self.__event = {
            'response': self.__thead_function
        }
        self.__callbacks = {}

    def on_start(self, callback):
        if callable(callback):
            self.__event['started'] = callback
            return self
        raise TypeError(f'{callback} must be a function').with_traceback(None)

    def on_finish(self, callback):
        if callable(callback):
            self.__event['finished'] = callback
            return self
        raise TypeError(f'{callback} must be a function').with_traceback(None)

    def on_success(self, callback):
        if callable(callback):
            self.__callbacks['success'] = callback
            return self
        raise TypeError(f'{callback} must be a function').with_traceback(None)

    def on_fail(self, callback):
        if callable(callback):
            self.__callbacks['fail'] = callback
            return self
        raise TypeError(f'{callback} must be a function').with_traceback(None)

    def send(self):
        self.__thead = Request(function=self.__function)
        for signal, slot in self.__event.items():
            self.__thead.__getattribute__(signal).connect(slot)
        self.__thead.start()
        return self

    def do(self, function):
        if callable(function):
            self.__function = function
            return self


    def __thead_function(self, response):
        if response['status']:
            if 'success' in self.__callbacks.keys():
                self.__callbacks['success'](response)
        else:
            if 'fail' in self.__callbacks.keys():
                self.__callbacks['fail'](response)
