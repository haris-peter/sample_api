from rest_framework.response import Response
from api_app.models import Message  # Import the model

def index(request):
    """
    A view function that fetches the "Hello, World!" message from the database.
    """
    # Fetch the first message from the database
    try:
        message = Message.objects.first()  # Assuming there's at least one record
        response = {"message": message.text if message else "No data found"}
    except Exception as e:
        response = {"error": str(e)}
    
    return Response(response)
