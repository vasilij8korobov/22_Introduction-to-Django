from django.urls import path
from . import views

app_name = 'Students' # он же namespace='Students' в config.urls

urlpatterns = [
    # FBV Адреса
    path('show_data/', views.show_data, name='show_data'),
    path('submit_data/', views.submit_data, name='submit_data'),
    path('item/<int:item_id>', views.show_item, name='show_item'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/', views.index, name='index'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_details'),
    path('student_list/', views.student_list, name='student_list'),

    # CBV Адреса
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/detail/<int:pk>', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/update/<int:pk>', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodel/delete/<int:pk>', views.MyModelDeleteView.as_view(), name='mymodel_delete'),

]
