# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken

# from authorized.api.serializers import Companyserializer
# # from user_app import models


# @api_view(['POST', ])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


# @api_view(['POST', ])
# def registration_view(request):

#     if request.method == 'POST':
#         serializer = Companyserializer(data=request.data)

#         data = {}

#         if serializer.is_valid():
#             auth = serializer.save()
#             token = Token.objects.get(user=auth).key
#             resp1 = {
#                 "Company Name": "Incretech",
#                 "message": {
#                     "name": auth.name,
#                     "mobile": auth.mobile,
#                     "email": auth.email,
#                     "designation": auth.designation,
#                 }
#             }

#             refresh = RefreshToken.for_user(auth)
#             data['token'] = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return Response(resp1, status=status.HTTP_201_CREATED)
#         else:
#             # data = serializer.errors
#             resp2 = {
#                 "code": 0,
#                 "message": "Registration UnSuccessful!",
#                 "errors": serializer.errors
#             }
#             return Response(resp2, status=status.HTTP_201_CREATED)
