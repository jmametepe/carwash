from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,

    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
)

urlpatterns = [
    path('create-worker/', create_supplier, name='create-worker'),
    path('create-customer/', create_buyer, name='create-customer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('add-car/', create_product, name='add-car'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('worker-list/', SupplierListView.as_view(), name='worker-list'),
    path('customer-list/', BuyerListView.as_view(), name='customer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('car-list/', ProductListView.as_view(), name='car-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
]