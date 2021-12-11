# -----------------------------------------------------
#
#
# -----------------------------------------------------
# {Modification Log}
# -----------------------------------------------------
# Author: {author}
# Maintainer: {maintainer}
# Created At:
# Last Modified:
# Status: {dev_status}
# -----------------------------------------------------
from commons.loggy import set_up_logging
logger = set_up_logging()


class AuthMiddleware(object):

    def process_request(self, req, resp):
        logger.info(req)

    def process_resource(self, req, resp, resource, params):
        logger.info(resp)

    def process_response(self, req, resp, resource, req_succeeded):
        logger.info("process_response")
        #delattr(resp.media["data"], "password")
        #r = json.loads(resp.media["data"])
        #delattr(r, "password")
        #resp.media["data"] = r
        #resp.media["data"] = {"name":"senthil"}
        #logger.info(resp.media["data"]["password"])
        return

