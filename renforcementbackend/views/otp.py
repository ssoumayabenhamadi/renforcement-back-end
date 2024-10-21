from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from service.otp_service import generate_otp, verify_otp
@login_required
def send_otp(request):
    secret_key = 'base32secret3232'  
    otp = generate_otp(secret_key)
    
    return JsonResponse({'otp': otp}, status=200)

@login_required
def verify_user_otp(request):
    user_input_otp = request.GET.get('otp')
    secret_key = 'base32secret3232' 

    if verify_otp(secret_key, user_input_otp):
        return JsonResponse({'message': 'OTP vérifié avec succès'}, status=200)
    else:
        return JsonResponse({'message': 'OTP invalide'}, status=400)
