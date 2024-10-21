from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.auth.models import User
from ..models import OTP

def send_otp_via_email(user_email, otp_code):
    subject = 'Votre code OTP'
    message = f'Voici votre code OTP : {otp_code}. Ce code est valable pendant 5 minutes.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    
    send_mail(subject, message, email_from, recipient_list)

@api_view(['POST'])
@throttle_classes([UserRateThrottle, AnonRateThrottle])
def login_with_otp(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        otp, created = OTP.objects.get_or_create(user=user)
        otp.generate_code()

        send_otp_via_email(user.email, otp.code)

        return Response({'message': 'OTP envoyé par email'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Identifiants invalides'}, status=status.HTTP_400_BAD_REQUEST)
