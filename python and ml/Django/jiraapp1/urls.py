from django.urls import path
from . import views
from JiraSub.settings import DEBUG, STATIC_URL, STATIC_ROOT
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
from django.conf.urls import url,include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from .views import Projectviewset, Issueviewset, Commentviewset, Sprintviewset, Issuelist
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('project',Projectviewset)

router1 = DefaultRouter()
router1.register('issues',Issueviewset)

router2 = DefaultRouter()
router2.register('comments',Commentviewset ,basename='Comment')

router3 = DefaultRouter()
router3.register('sprint',Sprintviewset ,basename='Sprint')

router4 = DefaultRouter()
router4.register('issuelist',Issuelist ,basename='IssueList')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(router1.urls)),
    path('api/', include(router2.urls)),
    path('api/', include(router3.urls)),
    path('api/', include(router4.urls)),
    path('api/issues_of_project/<int:project_id>', views.Issueviewset.get_issues_by_project),
    path('api/comment_of_issue/<int:issue_id>', views.Commentviewset.get_comments_by_issue),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]

#DataFlair
# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    