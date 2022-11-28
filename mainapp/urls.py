from django.urls import path
from django.views.generic.base import RedirectView

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("news/<str:params>/", RedirectView.as_view(url="https://google.com/search?q=%(params)s")),
    path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path("courses/", views.CoursesPageView.as_view(), name="courses"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    path("login/", views.LoginPageView.as_view(), name="login"),
]
