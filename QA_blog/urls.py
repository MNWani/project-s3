from django.conf.urls import url, include
from QA_blog import views as QA_blog_views
from django.contrib.auth import views as auth_views
from QA_blog import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views

urlpatterns = [
    url(r'^QA_blog/$', views.post_list),
    url(r'^QA_blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^QA_blog/home/$', views.post_list, name='home'),
    url(r'^QA_blog/home/(?P<id>\d+)/$', views.post_detail),
    url(r'^QA_blog/reviews/$', views.article, name='reviews'),
    url(r'^QA_blog/reviews/(?P<id>[0-9]+)/$', views.article_detail),
    url(r'^QA_blog/reviewsdetail/$', QA_blog_views.reviewsdetail, name='reviewsdetail'),
    url(r'^QA_blog/reviewsdetail/(?P<id>[0-9]+)/$', views.post_article_detail),
    url(r'^QA_blog/qa_corner/$', views.videos, name='qa_corner'),
    url(r'^QA_blog/qa_corner/(?P<id>[0-9]+)/$', views.get_video, name='qa_corner'),
    url(r'^QA_blog/signup/$', QA_blog_views.signup, name='signup'),
    url(r'^QA_blog/login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^QA_blog/logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^qa-paypal-sands/', include(paypal_urls)),
    url(r'^QA_blog/paypal-return', paypal_views.paypal_return),
    url(r'^QA_blog/paypal-cancel', paypal_views.paypal_cancel),
]
