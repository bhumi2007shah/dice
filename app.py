import logging
import sentry_sdk

from flask import Flask, jsonify

from CustomException.CustomException import CustomWebException

from Config import config

from controller.CvProcessController import cv_process_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(cv_process_api)
    

    # formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    #
    # handler = TimedRotatingFileHandler('logs/cvparser.log',
    #                                    when='midnight',
    #                                    backupCount=1)
    #
    # handler.setFormatter(formatter)
    # logger = logging.getLogger(__name__)
    # logger.addHandler(handler)

    logging.basicConfig(filename="logs/cvparser.log", filemode="a+", level=logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

    app.config.from_object('config')

    @app.errorhandler(CustomWebException)
    def web_exception(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        logging.info(response)
        return response

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1', port=config.PORT, debug=True)
    logging.info('Started app in ' + config.APP_ENV + 'environment')
