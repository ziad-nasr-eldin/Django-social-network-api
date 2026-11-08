from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/v1/core/", include("apps.core.urls")),
    path("api/v1/accounts/", include("apps.accounts.urls")),
    path("api/v1/profiles/", include("apps.profiles.urls")),
    path("api/v1/posts/", include("apps.posts.urls")),
    path("api/v1/comments/", include("apps.comments.urls")),
    path("api/v1/interactions/", include("apps.interactions.urls")),
    path("api/v1/feed/", include("apps.feed.urls")),
    path("api/v1/notifications/", include("apps.notifications.urls")),
    path("api/v1/search/", include("apps.search.urls")),
    path("api/v1/dashboard/", include("apps.dashboard.urls")),
    path("api/v1/moderation/", include("apps.moderation.urls")),
]
