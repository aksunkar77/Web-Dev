from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Category, Product


def product_list(request):
    products = Product.objects.all()
    return JsonResponse([p.to_json() for p in products], safe=False)

# 2. Нэг бүтээгдэхүүн ID-аар [cite: 3]
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return JsonResponse(product.to_json())

# 3. Бүх категори [cite: 3]
def category_list(request):
    categories = Category.objects.all()
    return JsonResponse([c.to_json() for c in categories], safe=False)

# 4. Нэг категори ID-аар [cite: 3]
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    return JsonResponse(category.to_json())

# 5. Тухайн категорийн бүх бүтээгдэхүүн [cite: 3]
def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return JsonResponse([p.to_json() for p in products], safe=False)
