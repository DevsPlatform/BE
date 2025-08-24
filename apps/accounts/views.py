from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['GET'])
def profile(request):
    """Get current user profile"""
    if request.user.is_authenticated:
        user_data = {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'provider': request.user.provider,
            'avatar_url': request.user.avatar_url,
            'bio': request.user.bio,
        }
        return Response(user_data)
    return Response({'error': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)