from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OtpToken
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User) 
def create_token(sender, instance, created, **kwargs):
    if created:
        if not instance.is_superuser:
            OtpToken.objects.create(user=instance)
            instance.save()
        
            otp = OtpToken.objects.get(user=instance)
        
            subject="OTP Verification"
            message = f"""
                <html>
                    <head>
                    <style>
                        .container {{
                        background-color: #f2f2f2;
                        padding: 20px;
                        }}
                        .otp {{
                        font-size: 24px;
                        font-weight: bold;
                        padding: 10px;
                        background-color: #ffffff;
                        border: 2px solid #007bff;
                        border-radius: 5px;
                        }}
                    </style>
                    </head>
                    <body>
                    <div class="container">
                        <p>Hi, {instance.first_name}</p>
                        <p>Your OTP for email verification is:</p>
                        <div class="otp">{otp.otp_code}</div>
                        <p>Please use it to verify.</p>
                        <p>If you did not request this OTP, please ignore this email.</p>
                        <p>Best regards,<br/>
                        EduPulse</p>
                    </div>
                    </body>
                </html>         
                                    
                """
            sender = "edupluse.contact@gmail.com"
            receiver = [instance.email]
        
            
            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False,
                    html_message=message
                )
    