import typing as t
import flask
import sqlalchemy as sa
from flask_restx import Resource, Namespace
from service.api.external_service.user import groups_user, groups_user_followed
from service.api.models.base import db
from service.api.models.user import Request
from service.api.serializes.user import UserGroup, UserGroupSchema

api_service = Namespace('service/user', description='Функциональные запросы')


@api_service.route("/<int:user_id>/group")
class UserGroups(Resource):
    @api_service.doc(security="apiKey")
    @api_service.param('name', 'Введите подстроку названия группы для поиска')
    def get(self, user_id):
        """
        Получить группы пользователя.
        :param user_id: id пользователя
        """
        params = flask.request.args
        if params:
            exp: UserGroup = UserGroupSchema().load(params)
            data = groups_user(user_id, params=params)
            if data.get('groups'):
                r = Request(value_name=exp.name, groups=data['groups'])
                db.session.add(r)
                db.session.commit()

        return groups_user(user_id, params=params)


@api_service.route("/<int:user_id>/group/follow")
class UserGroupsFollowed(Resource):
    @api_service.doc(security="apiKey")
    @api_service.param('name', 'Введите подстроку названия группы для поиска')
    def get(self, user_id):
        """
        Получить группы пользователя и его подписчиков.
        :param user_id: id пользователя
        """
        params: t.Dict = flask.request.args

        return groups_user_followed(user_id, params=params)


@api_service.route("/requests")
class MonitoringRequest(Resource):
    @staticmethod
    def get():
        """
        Возвращает все когда-либо найденные с использованием метода 2 группы (сообщества).
        """
        subq = db.session.query(
            db.func.json_array_elements(Request.groups).label('row')
        ).subquery()
        stmt = db.session.query(db.func.json_agg(subq.c.row).label('aggregated'))
        result: sa.engine.Row = stmt.first()
        return flask.jsonify(result[0])



