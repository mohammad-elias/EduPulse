from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import OtpToken

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','mobile','password','confirm_password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def save(self):
        email = self.validated_data['email']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        mobile = self.validated_data['mobile']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists!"})
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched!"})
        
        user = User.objects.create_user(email=email,first_name=first_name,last_name=last_name,mobile=mobile)
        user.set_password(password)
        user.save()
        return user



class EmailVerificationSerializer(serializers.Serializer):
    otp_code = serializers.CharField(max_length=6)
    user_id = serializers.IntegerField()

    def validate(self, data):
        user_id = data.get('user_id')
        otp_code = data.get('otp_code')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user ID.")

        try:
            otp_token = OtpToken.objects.get(user=user, otp_code=otp_code)
        except OtpToken.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP code.")

        return data

    def save(self):
        user_id = self.validated_data['user_id']
        user = User.objects.get(id=user_id)
        user.is_active = True
        user.save()

        # Token.objects.filter(user=user).delete()
        
        token, created = Token.objects.get_or_create(user=user)

        return user, token.key


