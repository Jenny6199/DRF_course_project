import graphene
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, ToDo


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

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query)
