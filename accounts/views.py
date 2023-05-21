from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from rest_framework.views import APIView


class RegistrationAPIView(APIView):
    def post(self, request):

        # Create a serializer instance with the request data
        serializer = RegistrationSerializer(data=request.data)
        
        # Validate the serializer data
        if serializer.is_valid():

            # Save the user registration data
            serializer.save()

             # Return a success response
            return Response({'data':"User registration successful."},status=status.HTTP_200_OK)
        
        # Return an error response with serializer errors
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmailVerificationView(APIView):

    def get(self, request,verification_code):
        try:
            # Retrieve the user with the provided verification code
            user = User.objects.get(verification_code=verification_code)
        except:
            return Response({'error':'verification code is incorrect or expired'},status=status.HTTP_400_BAD_REQUEST)
        
        # Set the user as verified and save the changes
        user.is_verified = True
        user.save()
        return Response("Your email has been verified.",status=status.HTTP_200_OK)