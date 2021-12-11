import falcon
from commons.jsonconfig import JsonConfig
from commons.loggy import set_up_logging
from controller.docxController import docxController

logger = set_up_logging()
config = JsonConfig("app.config")

app = falcon.API()
# Attach routes
app.add_route('/export/doc', docxController())