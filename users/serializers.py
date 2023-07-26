from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


class UserSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name',  'username', 'password']