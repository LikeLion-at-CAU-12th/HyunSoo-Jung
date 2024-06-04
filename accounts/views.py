from django.shortcuts import render
from rest_framework_simplejwt.serializers import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# 8주차
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save(request)
            token = RefreshToken.for_user(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register succenss",
                    "toekn": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthView(APIView):
    def post(self, request):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data["user"]
            access_token = serializer.validated_data["access_token"]
            refresh_token = serializer.validated_data["refresh_token"]
            res = Response(
                {
                    "user": {
                        "id": user.id,
                        "email": user.email,
                    },
                    "message": "login success",
                    "token": {
                        "access_token": access_token,
                        "refresh_token": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access-token", access_token, httponly=True)
            res.set_cookie("refresh-token", refresh_token, httponly=True)
            return res
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message":"로그아웃되었습니다."}, status=status.HTTP_200_OK)
    

# 9주차
from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR, "secrets.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

GOOGLE_SCOPE_USERINFO = get_secret("GOOGLE_SCOPE_USERINFO")
GOOGLE_REDIRECT = get_secret("GOOGLE_REDIRECT")
GOOGLE_CALLBACK_URI = get_secret("GOOGLE_CALLBACK_URI")
GOOGLE_CLIENT_ID = get_secret("GOOGLE_CLIENT_ID")
GOOGLE_SECRET = get_secret("GOOGLE_SECRET")

from django.shortcuts import redirect
from json import JSONDecodeError
from django.http import JsonResponse
import requests

from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.google import views as google_view


# 구글 소셜로그인 변수 설정
state = os.environ.get("STATE")
BASE_URL = 'http://localhost:8000/'

def google_login(request):
   scope = GOOGLE_SCOPE_USERINFO # + "https://www.googleapis.com/auth/drive.readonly" 등 scope 설정 후 자율적으로 추가
   return redirect(f"{GOOGLE_REDIRECT}?client_id={GOOGLE_CLIENT_ID}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

def google_callback(request):
    code = request.GET.get("code") # Query String 으로 넘어옴
    
    # 1. 받은 코드로 구글에 access token 요청 (token_req)
    token_req = requests.post(f"https://oauth2.googleapis.com/token?client_id={GOOGLE_CLIENT_ID}&client_secret={GOOGLE_SECRET}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}")
    #  json으로 변환 & 에러 부분 파싱
    token_req_json = token_req.json()
    error = token_req_json.get("error")

    ## 에러 발생 시 종료
    if error is not None:
        raise JSONDecodeError(error)
    ## 성공 시 access_token 가져오기 (google_access_token)
    google_access_token = token_req_json.get('access_token')


    # 2. 가져온 access_token으로 이메일 값을 구글에 요청 (google_access_token)
    email_response = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={google_access_token}")
    res_status = email_response.status_code

    ## 에러 발생 시 400 에러 반환
    if res_status != 200:
        return JsonResponse({'status': 400,'message': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
    ## 성공 시 이메일 가져오기
    email_res_json = email_response.json()
    email = email_res_json.get('email')

    serializer = OAuthSerializer(data=email_res_json)

    # 3. 전달받은 이메일, access_token, code를 바탕으로 회원가입/로그인
    try:

        # 전달받은 이메일로 등록된 유저가 있는지 탐색
        user = User.objects.get(email=email)

        # FK로 연결되어 있는 socialaccount 테이블에서 해당 이메일의 유저가 있는지 확인
        social_user = SocialAccount.objects.get(user=user)

        # 구글계정이 아니면 에러
        if social_user.provider != 'google':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

        # 구글계정으로 가입된 User
        data = {'access_token': google_access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}api/user/google/login/finish/", data=data)
        accept_status = accept.status_code

        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)

        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    
        # if serializer.is_valid(raise_exception=True):

        #     user = serializer.validated_data["user"]
        #     access_token = serializer.validated_data["access_token"]
        #     refresh_token = serializer.validated_data["refresh_token"]
        #     res = JsonResponse(
        #         {
        #             "user": {
        #                 "id": user.id,
        #                 "email": user.email,
        #             },
        #             "message": "login success",
        #             "token": {
        #                 "access_token": access_token,
        #                 "refresh_token": refresh_token,
        #             },
        #         },
        #         status=status.HTTP_200_OK,
        #     )
        #     res.set_cookie("access-token", access_token, httponly=True)
        #     res.set_cookie("refresh-token", refresh_token, httponly=True)
        #     return res
        
    # except: # 회원가입이 필요함
    #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        # 기존에 가입된 User가 없는 경우
        ## 회원가입이 필요함
        data = {'access_token': google_access_token, 'code': code}
        accept = requests.post(f"{BASE_URL}api/user/google/login/finish/", data=data)
        accept_status = accept.status_code

        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        
        accept_json = accept.json()
        accept_json.pop('user', None)
        return JsonResponse(accept_json)
    
    except SocialAccount.DoesNotExist:
        # 가입된 User는 있지만 SocialAccount가 없는 경우
        return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)


class GoogleLogin(SocialLoginView):
    adapter_class = google_view.GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client