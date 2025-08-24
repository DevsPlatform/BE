from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from apps.users.models import Provider

User = get_user_model()


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        GitHub와 Google 로그인만 허용
        """
        if sociallogin.account.provider not in ['github', 'google']:
            raise ValueError("Only GitHub and Google login are allowed")
    
    def save_user(self, request, sociallogin, form=None):
        """
        소셜 로그인 시 사용자 저장 로직
        """
        user = sociallogin.user
        provider_name = sociallogin.account.provider
        
        # Provider 객체 가져오기 또는 생성
        provider, created = Provider.objects.get_or_create(
            name=provider_name,
            defaults={'display_name': provider_name.title()}
        )
        
        # 소셜 계정의 고유 ID를 CI로 사용
        ci = str(sociallogin.account.uid)
        
        # 기존 사용자 확인
        existing_user = User.objects.filter(
            ci=ci,
            provider=provider
        ).first()
        
        if existing_user:
            return existing_user
        
        # 새 사용자 생성
        user.provider = provider
        user.ci = ci
        user.email = sociallogin.account.extra_data.get('email', '')
        user.nickname = sociallogin.account.extra_data.get('name', '')
        user.profile_image = sociallogin.account.extra_data.get('avatar_url', '')
        
        user.save()
        return user