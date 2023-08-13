from ryu.base import app_manager

class TestApp(app_manager.RyuApp):
    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        print("Ryu is installed correctly.")

app_manager.require_app('TestApp')