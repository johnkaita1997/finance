# Create your views here.
import uuid

from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from utils import SchoolIdMixin, UUID_from_PrimaryKey
from .models import VoteHead
from .serializers import VoteHeadSerializer, VoteHeadCreateSerializer


class VoteHeadCreateView(SchoolIdMixin,  generics.CreateAPIView):
    serializer_class = VoteHeadCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        school_id = self.check_school_id(self.request)
        if not school_id:
            return JsonResponse({'detail': 'Invalid school_id in token'}, status=401)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['school_id'] = school_id
            try:
                self.perform_create(serializer)
            except Exception as exception:
                return Response({'detail': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail': 'VoteHead created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class VoteHeadListView(SchoolIdMixin, generics.ListAPIView):
    serializer_class = VoteHeadSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        school_id = self.check_school_id(self.request)
        if not school_id:
            return VoteHead.objects.none()
        queryset = VoteHead.objects.filter(school_id=school_id)
        account_type = self.request.query_params.get('account_type', None)
        if account_type and account_type != "" and account_type != "null":
            queryset = queryset.filter(account_type__id = account_type)
        return queryset
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            if not queryset.exists():
                return JsonResponse([], safe=False, status=200)
            serializer = self.get_serializer(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as exception:
            return Response({'detail': str(exception)}, status=status.HTTP_400_BAD_REQUEST)


class VoteHeadDetailView(SchoolIdMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = VoteHead.objects.all()
    serializer_class = VoteHeadCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        primarykey = self.kwargs['pk']
        try:
            id = UUID_from_PrimaryKey(primarykey)
            return VoteHead.objects.get(id=id)
        except (ValueError, VoteHead.DoesNotExist):
            raise NotFound({'detail': 'Record Not Found'})

    def update(self, request, *args, **kwargs):
        school_id = self.check_school_id(request)
        if not school_id:
            return JsonResponse({'detail': 'Invalid school_id in token'}, status=401)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.validated_data['school_id'] = school_id
            try:
                self.perform_update(serializer)
            except Exception as exception:
                return Response({'detail': str(exception)}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail': 'VoteHead updated successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        school_id = self.check_school_id(request)
        if not school_id:
            return JsonResponse({'error': 'Invalid school_id in token'}, status=401)

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'Record deleted successfully'}, status=status.HTTP_200_OK)
