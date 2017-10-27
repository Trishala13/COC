from django.conf.urls import url

from users import views as user_views
from employee import views as emp_views
from info import views as info_views

urlpatterns = [
    url(r'user_site', user_views.user_site),
    url(r'sign-in', user_views.sign_in),
    url(r'sign-up', user_views.sign_up),
    url(r'complaint', user_views.complaint),
    url(r'zone', info_views.zone),
    url(r'division', info_views.division),
    url(r'official-login', emp_views.official_login),
    url(r'official_login_form', emp_views.official_login_form),
    url(r'employee_site', emp_views.emp_site),

]
