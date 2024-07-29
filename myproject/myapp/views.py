from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DynamicModel
from .serializers import DynamicModelSerializer

@api_view(['POST'])
def import_data(request):
    """Import JSON data into the database."""
    try:
        data = request.data
        if not isinstance(data, list):
            return Response({"error": "Invalid data format. Expected a list."}, status=status.HTTP_400_BAD_REQUEST)

        for item in data:
            if not isinstance(item, dict):
                return Response({"error": "Invalid data format. Each item should be a dictionary."}, status=status.HTTP_400_BAD_REQUEST)

            for model_name, details in item.items():
                if not isinstance(details, dict):
                    return Response({"error": f"Invalid data format for model {model_name}. Details should be a dictionary."}, status=status.HTTP_400_BAD_REQUEST)

                DynamicModel.objects.create(model_name=model_name, data=details)

        return Response({"status": "Data imported successfully"}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_records(request, model_name):
    """List all records for a given model name."""
    try:
        records = DynamicModel.objects.filter(model_name=model_name)
        if not records.exists():
            return Response({"error": "No records found for the specified model name."}, status=status.HTTP_404_NOT_FOUND)

        serializer = DynamicModelSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_record(request, model_name, id):
    """Retrieve a specific record by ID for a given model name."""
    try:
        record = DynamicModel.objects.get(model_name=model_name, id=id)
        serializer = DynamicModelSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except DynamicModel.DoesNotExist:
        return Response({"error": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
