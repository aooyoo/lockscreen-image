from django.conf.urls import include, url
from django.contrib import admin

import apps.phone.views
import apps.upload.views
import apps.image.views
import apps.feedback.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', apps.phone.views.login),
    url(r'^callback/foreground/$', apps.upload.views.CallbackHandler.as_view()),
    url(r'^callback/background/$', apps.upload.views.CallbackHandler.as_view()),


    url(r'^foreground/hot/$', apps.image.views.ImageGetterView.as_view()),
    url(r'^foreground/new/$', apps.image.views.ImageGetterView.as_view()),
    url(r'^background/hot/$', apps.image.views.ImageGetterView.as_view()),
    url(r'^background/new/$', apps.image.views.ImageGetterView.as_view()),

    url(r'^collect/$', apps.image.views.ImagePairView.as_view()),
    url(r'^uncollect/$', apps.image.views.ImagePairView.as_view()),
    url(r'^download/$', apps.image.views.ImagePairView.as_view()),

    url(r'^collect/show/$', apps.image.views.show_collected_images),

    url(r'^foreground/category/$', apps.image.views.get_foregound_category),


    url(r'feedback/$', apps.feedback.views.feedback),
]
