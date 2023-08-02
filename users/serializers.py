from djoser.serializers import UserSerializer as BaseUserserializer, UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'email', 'first_name', 'last_name',  'username', 'password']
        
class UserSerializer(BaseUserserializer):
    class Meta(BaseUserserializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email']