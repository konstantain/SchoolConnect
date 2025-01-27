from publishing_platform.app import templates
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

import publishing_platform.auth.service as auth_service
from publishing_platform.constants import BACKEND_DOMAIN

default_routes = APIRouter()


@default_routes.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("base.html", {'request': request, 'BACKEND_DOMAIN': BACKEND_DOMAIN, })


@default_routes.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login_form.html", {'request': request, 'BACKEND_DOMAIN': BACKEND_DOMAIN, })
