from django.shortcuts import render, get_object_or_404
from .serializers import LeadSerializer
from rest_framework.views import APIView
from .models import Lead, LEAD, EXPECTATION, SET
from rest_framework.response import Response
from rest_framework import status


class LeadAPIView(APIView):
    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadDetailAPIView(APIView):
    def get(self, request, id):
        lead = get_object_or_404(Lead, id=id)
        serializer = LeadSerializer(lead)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        lead = get_object_or_404(Lead, id=id)
        serializer = LeadSerializer(instance=lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            lead = get_object_or_404(Lead, id=id)
        except:
            return Response(
                data={
                    'success': False,
                    'message': 'Lead not found'
                }
            )
        else:
            lead.delete()
            return Response(
                data={
                    'status': True,
                    'message': 'Lead successfully deleted'
                }
            )


class LeadList(APIView):
    def get(self, request):
        lead = Lead.objects.filter(lead_status=LEAD)
        serializer = LeadSerializer(lead, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ExpectationList(APIView):
    def get(self, request):
        ex = Lead.objects.filter(lead_status=EXPECTATION)
        serializer = LeadSerializer(ex, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class SetList(APIView):
    def get(self, request):
        set = Lead.objects.filter(lead_status=SET)
        serializer = LeadSerializer(set, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
