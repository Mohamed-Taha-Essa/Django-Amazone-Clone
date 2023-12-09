# 4 classes
- product:
    - brand (one to many)
    - name
    - flag
    - price
    - image
    - review-count
    - sku
    - related
    - description
    - subtitle
    - tags

- reviews:
    - product(one to many)
    - name 
    - image 
    - review
    - date
    - rate

- brand :
    - name 
    - image
    - item-count

- images-product:
    - product(one to one)
    - images
  
   