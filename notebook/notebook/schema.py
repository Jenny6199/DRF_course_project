import graphene
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, ToDo
from uuid import uuid4


class UserType(DjangoObjectType):
    """Класс-схема для модели пользователя"""
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    """Класс-схема для модели проекта"""
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    """Класс-схема для модели заметки"""
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    """Класс-схема"""
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(ToDoType)

    user_by_username = graphene.Field(UserType, username=graphene.String(required=True))

    todo_by_creator = graphene.List(ToDoType, creator=graphene.String(required=False))

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    def resolve_user_by_username(self, info, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    def resolve_todo_by_creator(self, info, creator=None):
        todo = ToDo.objects.all()
        if creator:
            todo = todo.filter(creator__username=creator)
        return todo

schema = graphene.Schema(query=Query)
