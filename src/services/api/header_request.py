class HeaderRequest:
    def contentType(self, contentType='application/json'):
        """Generates a header json with content type.

        :param contentType: by default 'application/json'
        :return: json header
        """
        return {'Content-Type': contentType}

    def token(self, token):
        return {'Authorization': token}

    def contentType_token(self, token, contentType='application/json'):
        """Generates a header json with content type + authorization.

        :param token: authorization token
        :param contentType: by default 'application/json'
        :return: json header
        """
        return {'Content-Type': contentType, 'Authorization': token}
