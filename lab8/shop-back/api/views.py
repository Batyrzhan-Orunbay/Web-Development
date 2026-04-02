import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Product, Category


def product_to_dict(p):
    return {
        'id': p.id,
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'count': p.count,
        'is_active': p.is_active,
        'category_id': p.category_id,
    }


def category_to_dict(c):
    return {
        'id': c.id,
        'name': c.name,
    }


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return JsonResponse([product_to_dict(p) for p in products], safe=False)

    # POST — create a new product
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    required = ('name', 'price', 'description', 'count', 'category_id')
    missing = [f for f in required if f not in data]
    if missing:
        return JsonResponse({'error': f'Missing fields: {", ".join(missing)}'}, status=400)

    try:
        category = Category.objects.get(pk=data['category_id'])
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    product = Product.objects.create(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        count=data['count'],
        is_active=data.get('is_active', True),
        category=category,
    )
    return JsonResponse(product_to_dict(product), status=201)


@require_http_methods(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        return JsonResponse(product_to_dict(product))
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return JsonResponse([category_to_dict(c) for c in categories], safe=False)

    # POST — create a new category
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    if 'name' not in data or not str(data['name']).strip():
        return JsonResponse({'error': 'Missing or empty field: name'}, status=400)

    category = Category.objects.create(name=data['name'].strip())
    return JsonResponse(category_to_dict(category), status=201)


@require_http_methods(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(pk=id)
        return JsonResponse(category_to_dict(category))
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)


@require_http_methods(['GET'])
def category_products(request, id):
    try:
        category = Category.objects.get(pk=id)
        products = category.products.all()
        return JsonResponse([product_to_dict(p) for p in products], safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
