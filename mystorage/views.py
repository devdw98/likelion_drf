from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer

class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    def perform_create(self, serializer):
        #직접 작성한 유저를 자동으로 저장
        serializer.save(author=self.request.user)