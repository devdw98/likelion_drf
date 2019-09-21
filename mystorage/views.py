from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters  import SearchFilter # 검색

class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body')

    def perform_create(self, serializer):
        #직접 작성한 유저를 자동으로 저장
        serializer.save(author=self.request.user)

    #현재 request 낸 유저 == self.request.user >> 유저가 쓴 글만 나타남
    def get_queryset(self): 
        qs = super().get_queryset()

        if self.request.user.is_authenticated: #login
            qs = qs.filter(author = self.request.user)
        else: #not login
            qs = qs.none

        return qs