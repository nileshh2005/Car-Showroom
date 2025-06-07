from django.urls import path
from app1 import views


urlpatterns = [
    path('Dash',views.DashVw, name='Dash'),
    path('Cnt',views.CntVw, name='Cnt'),
    path('Cnt_dlt/<id>',views.Cnt_dltVw, name='cnt_dlt'),
    path('Cnt_updt/<id>',views.Cnt_updtVw, name='cnt_updt'),
]