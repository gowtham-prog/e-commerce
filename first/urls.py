from django.urls import path

from . import views
urlpatterns =[
      path("", views.index, name="index"),
      path("post", views.post, name="post"),
      path("about", views.about,name="about"),
      path("contact", views.contact,name="contact"),
      path("fwishlist/<int:id>",views.wishlist,name="fwishlist"),
      path("comment/<int:id>",views.addcomment,name="comment"),
      path("fshow/<int:id>", views.fshow,name="fshow"),
]