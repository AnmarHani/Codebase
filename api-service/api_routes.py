from fastapi import APIRouter, Request
import api_controllers

router = APIRouter()

router.add_api_route('/auth', methods=['GET'], endpoint=api_controllers.test)
router.add_api_route('/auth/get', methods=['GET'], endpoint=api_controllers.test_two)