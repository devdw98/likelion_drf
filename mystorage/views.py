from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters  import SearchFilter # 검색
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status

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

class ImgViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer




class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
  #parser_class 지정 
    parser_classes = (MultiPartParser, FormParser) #다양한 미디어 파일 형식을 수락할 수 있음

    #create() Overriding - post() 
    def post(self, request, *args, **kwargs): #메소드 커스터마이징 
        serializer = FilesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)