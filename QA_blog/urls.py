from django.conf.urls import url, include
from QA_blog import views as QA_blog_views
from django.contrib.auth import views as auth_views
from QA_blog import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^home/$', views.post_list, name='home'),
    url(r'^home/(?P<id>\d+)/$', views.post_detail),
    url(r'^reviews/$', views.article, name='reviews'),
    url(r'^reviews/(?P<id>[0-9]+)/$', views.article_detail),
    url(r'^reviewsdetail/$', QA_blog_views.reviewsdetail, name='reviewsdetail'),
    url(r'^reviewsdetail/(?P<id>[0-9]+)/$', views.post_article_detail),
    url(r'^qa_corner/$', views.videos, name='qa_corner'),
    url(r'^qa_corner/(?P<id>[0-9]+)/$', views.get_video, name='qa_corner'),
    url(r'^signup/$', QA_blog_views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^qa-paypal-sands/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]
