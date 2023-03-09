from fastapi import APIRouter
from . import user_controllers
router = APIRouter(
    prefix='/user'
)

router.add_api_route('/create', endpoint=user_controllers.create_user, methods=['POST'])
router.add_api_route('/get', endpoint=user_controllers.get_user, methods=['GET'])