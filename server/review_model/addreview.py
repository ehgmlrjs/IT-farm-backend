import csv
import os
import django
import re

import sys
from pathlib import Path

current_path = Path(__file__).resolve()
project_root =current_path.parent.parent

sys.path.append(str(project_root))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_app.settings")
os.environ["DJANGO_ALLOWS_ASYNC_UNSAFE"] = "true"
django.setup()

from order.models import Review, Order

review = Review()
review_list = []

with open('real_reviews_db.csv', encoding='utf8') as csv_file_review:
    rows = csv.reader(csv_file_review)
    next(rows, None)
    for row in rows:
        
        product_id = row[0]
        nickname = row[1]
        content = row[2]
        score = row[4]
        order_id = row[6]
        
        try:
            order_instance = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            print(f"Order with order_id {order_id} does not exist.")
            continue
        review = Review(product_id=product_id,
                        nickname=nickname,
                        content=content,
                        score=score,
                        order=order_instance)

        review_list.append(review)

Review.objects.bulk_create(review_list)
Review.objects.all().count()