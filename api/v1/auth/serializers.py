from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from users.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','name','password','email']
#         extra_kwargs = {
#             'password':{'write_only':True},
#         }

#     def create(self,validated_data):
#         password = validated_data.pop('password', None)
#         instance=self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'],
            password = clean_data['password'])
        user_obj.username = clean_data['username']
        user_obj.save()
        return user_obj
    

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def check_user(self,clean_data):
        user=authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise serializers.ValidationError('user not found')
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: UserModel
        fields = ('email', 'username')