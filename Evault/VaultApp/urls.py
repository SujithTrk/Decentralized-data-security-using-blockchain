from django.urls import path

from . import views

urlpatterns = [path("", views.index, name=""),
               path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),	      
               path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
               path("CheckVaultAction", views.CheckVaultAction, name="CheckVaultAction"),
               path("CheckVault.html", views.CheckVault, name="CheckVault"),
               path("AddDocument.html", views.AddDocument, name="AddDocument"),	      
               path("AddDocumentAction", views.AddDocumentAction, name="AddDocumentAction"),
	       path("ViewDocument", views.ViewDocument, name="ViewDocument"),
	       path("DownloadAction", views.DownloadAction, name="DownloadAction"),
]
