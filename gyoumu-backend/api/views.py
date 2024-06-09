# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class TestApiView(APIView):
#     def get(self, request):
#         return Response(data="Hello, World!", status=status.HTTP_200_OK)
    
from rest_framework.response import Response
from rest_framework.views import APIView
from .snowflake_connection import get_snowflake_connection

class SnowflakeDataView(APIView):
    def get(self, request):
        try:
            conn = get_snowflake_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CMS_TABLE")
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            return Response(data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)