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

@router.get("/{route_id}", response_model=RouteOut)
def get_route(
    route_id: int,
    current_user=Depends(get_current_user),
):
    return RouteController.get_route(route_id, current_user)

@router.put("/{route_id}", response_model=RouteOut)
def update_route(
    route_id: int,
    route: RouteUpdate,
    current_user=Depends(get_current_user),
):
    return RouteController.update_route(route_id, route, current_user)
@router.delete("/{route_id}")
def delete_route(
    route_id: int,
    current_user=Depends(get_current_user),
):
    return RouteController.delete_route(route_id, current_user)
@router.get("/", response_model=List[RouteOut])
def list_routes(
    current_user=Depends(get_current_user),
):
    return RouteController.list_routes(current_user)