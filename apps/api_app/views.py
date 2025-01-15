from rest_framework.response import Response
from apps.api_app.models import get_message  # Import the model

def index(request):
    """
    A view function that fetches the "Hello, World!" message from the database.
    """
    # Fetch the first message from the database
    try:
        response = {"message": get_message.text if get_message else "No data found"}
    except Exception as e:
        response = {"error": str(e)}
    
    return Response(response)
