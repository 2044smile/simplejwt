from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)  # 인증 된 사용자만

    def get(self, request):
        content = {'message': 'Hello, World'}
        return Response(content)
