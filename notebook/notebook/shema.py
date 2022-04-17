import graphene


class Query(graphene.ObjectType):
    """Класс-схема"""
    hello = graphene.String(default_value='Hi!')

schema = graphene.Schema(query=Query)
