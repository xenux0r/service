from flask_restx import Api, fields

authorizations = {"apiKey": {"type": "apiKey", "in": "header", "name": "X-API-Key"}}

api = Api(version='1.0', title='Функциональный сервис с интеграцией API VK',
          description='Сервис для работы с API VK', doc='/docs/',
          authorizations=authorizations
          )