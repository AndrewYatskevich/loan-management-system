from rest_framework.decorators import api_view
from rest_framework.response import Response

from loan_application.models import Manufacturer


@api_view(["GET"])
def retrieve_manufacturers_unique_id(request, pk):
    result = (
        Manufacturer.objects.filter(
            products__loan_application__contract__id=pk
        )
        .values_list("id", flat=True)
        .distinct()
    )
    return Response(result)
