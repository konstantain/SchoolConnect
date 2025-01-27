from fastapi import FastAPI
from fastapi.responses import JSONResponse

from publishing_platform.articles.views import articles_router
from publishing_platform.auth.views import auth_router
from publishing_platform.comments.views import comments_router
from publishing_platform.files.views import files_router
from publishing_platform.forms.views import forms_router
from publishing_platform.tasks.views import tasks_router
from publishing_platform.users.views import users_router
from front.lk import default_routes

__all__ = ["init_routes"]


def init_routes(app: FastAPI):
    include_route = app.router.include_router

    include_route(
        auth_router, default_response_class=JSONResponse, tags=["Auth"], prefix="/api/auth",
    )

    include_route(
        users_router, default_response_class=JSONResponse, tags=["Users"], prefix="/api/users",
    )

    include_route(
        forms_router, default_response_class=JSONResponse, tags=["Forms"], prefix="/api/forms",
    )

    include_route(
        tasks_router, default_response_class=JSONResponse, tags=["Tasks"], prefix="/api/tasks",
    )

    include_route(
        default_routes, default_response_class=JSONResponse, tags=["Front"], prefix="/api/test",
    )