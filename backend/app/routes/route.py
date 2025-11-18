from .schemas import RouteCreate, RouteUpdate, RouteOut
from .controller import RouteController 
from fastapi import APIRouter, Depends
from backend.app.dependencies import get_current_user


@router = APIRouter(prefix="/routes", tags=["routes"])  
@router.post("/", response_model=RouteOut)
def create_route(
    route: RouteCreate,
    current_user=Depends(get_current_user),
):
    return RouteController.create_route(route, current_user)