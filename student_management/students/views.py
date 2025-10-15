from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class StudentDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk=None):
        if pk:
            try:
                student=Student.objects.get(id=pk)

            except:
                return Response({'message': 'Student doesnt exists'}, status=status.HTTP_404_NOT_FOUND)

            serializer = StudentSerializer(student)
            return Response(serializer.data)

        else:
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)





    def post(self,request):
        data=request.data
        serializer=StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'new student detail is added'},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):
        data=request.data
        try:
           student=Student.objects.get(id=data['id'])
           serializer=StudentSerializer(student,data=data,partial=False)
        except:
            return Response({'message':'Student doesnt exists'},status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Student details updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    def delete(self,request):
        data=request.data
        try:
           student=Student.objects.get(id=data['id'])
        except:
            return Response({'message':'Student doesnt exists'},status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({'message':'Student details deleted'},status=status.HTTP_200_OK)


