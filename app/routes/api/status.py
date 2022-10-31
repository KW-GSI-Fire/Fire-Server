from fastapi import APIRouter

from status import status_manager


# Router
router = APIRouter(
    prefix="/status",
    tags=["status"],
)


# APIs
@router.get("/temperature")
async def get_temperature_status():
    status = status_manager.readStatus('t')

    temperature = status['temperature']
    level = status['level']

    return {
        "temperature": temperature, 
        "level": level,
    }


@router.get("/box")
async def get_box_status():
    status = status_manager.readStatus('b')

    box_opened = status['box_opened']
    
    return {
        "box_opened": box_opened,
    }
