# -*- coding: utf-8 -*-
class PermutiveException(Exception):
    pass


class PermutiveApiException(PermutiveException):
    """ Parse non 200 responses as API exceptions """
    def __init__(self, response, *args, **kw):
        self.status_code = response.status_code
        try:
            error = response.json().get('error', {})
            error_msg = "{message}. Cause: {cause}".format(
                message=error.get('message', ''),
                cause=error.get('cause', '')
            )
            self.message = error_msg
            self.error_status = error.get('status')
            self.error_code = error.get('code')
            self.docs = error.get('docs')
        except:
            self.message = response.text or ""

        super(PermutiveApiException, self).__init__(self.message, args, **kw)
