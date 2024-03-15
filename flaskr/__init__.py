"""
Application factory
__init__.py serves double duty here: contains the application factory, and it \
  tells Python that the flaskr directory should be treated as a package.
"""
import os

from flask import Flask


"""
Unlike of creating a Flask instance globally, we will create it inside a \
  function. This function is known as the application factory. Any \
  configuration, registration, and other setup the application needs will \
  happen inside the function, then the application will be returned.
"""


def create_app(test_config=None):
    # create and configure the app

    """
    __name__ is the name of the current Python module. The app needs to know \
      where it’s located to set up some paths, and __name__ is a convenient \
      way to tell it that.

    instance_relative_config=True tells the app that configuration files are \
      relative to the instance folder. The instance folder is located outside \
      the flaskr package and can hold local data that shouldn’t be committed \
      to version control, such as configuration secrets and the database file.
    """
    app = Flask(__name__, instance_relative_config=True)
    """
    app.config.from_mapping() sets some default configuration that the app \
      will use:

    SECRET_KEY is used by Flask and extensions to keep data safe. It’s set to \
      'dev' to provide a convenient value during development, but it should \
      be overridden with a random value when deploying.

    DATABASE is the path where the SQLite database file will be saved. It’s \
      under app.instance_path, which is the path that Flask has chosen for \
      the instance folder. You’ll learn more about the database in the next \
      section.
    """
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    """
    app.config.from_pyfile() overrides the default configuration with values \
      taken from the config.py file in the instance folder if it exists. For \
      example, when deploying, this can be used to set a real SECRET_KEY.

    test_config can also be passed to the factory, and will be used instead \
      of the instance configuration. This is so the tests we have in the \
      tutorial can be configured independently of any development values you \
      have configured.
    """
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    """
    os.makedirs() ensures that app.instance_path exists. Flask doesn’t create \
      the instance folder automatically, but it needs to be created because \
      your project will create the SQLite database file there.
    """
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    """
    @app.route() creates a simple route so you can see the app working \
      before getting into the rest of the tutorial. It creates a connection \
      between the URL /hello and a function that returns a response, the \
      string 'Hello, World!' in this case.
    """
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register db commands in the app
    from . import db
    db.init_app(app)

    # register the app blueprints
    from . import auth
    app.register_blueprint(auth.bp)

    return app
