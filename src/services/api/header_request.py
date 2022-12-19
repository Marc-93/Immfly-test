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

    def contentType_deviceId(self, deviceId, contentType='application/json'):
        """Generates a header json with content type + device id.

        :param deviceId: uuid from device
        :param contentType: by default 'application/json'
        :return: json header
        """
        return {'Content-Type': contentType, 'X-Bling-Device-Id': deviceId}

    def contentType_deviceId_token(self, token, deviceId, contentType='application/json'):
        """Generates a header json with content type + device id + token.

        :param token: authorization token
        :param deviceId: uuid from device
        :param contentType: by default 'application/json'
        :return: json header
        """
        return {'Content-Type': contentType, 'Authorization': token, 'X-Bling-Device-Id': deviceId}

    def contentType_token_userAgent(self, token, userAgent="Sherwood-WebApp/1", contentType='application/json'):
        """Generates a header json with content type + authorization.

        :param token: authorization token
        :param contentType: by default 'application/json'
        :return: json header
        """
        return {'Content-Type': contentType, 'Authorization': token, 'User-Agent': userAgent}
