# App product
## (class) product:  
- brand (relation)
- product image (relation)                           
- discription
- related item
- name                                       
- image                                    
- flag (salenew)    
- price                                                         
- review count                               
- sku                                        
- subtitle                                   
- tags           

- Note 
    - add slug to product class.
    
## (class) product-images:
  - images
  - product ( relation )
  

## (class) brand:
  - image
  - name
  - item count (can make len on item do't save in db)   

## (class) reviews:
- product (relation)
- content
- rate
- name and image 
    - i will get it from django user(relation)
- created at
- number of review

# function:
- product list 
- product detail
- brand list    
- brand det     
- search
- filter
- add to cart   
- add wishlist  

## Note :
- add translation to my model.
  ----------------------------------------------------------------------------------------------------------------

# App order :
## class Order
- user (relation with user django)
- code 
- Status ('Recieved' , 'Processed' ,'Shipped' ,'Delivered' )
- Discount
- Order Time
- Delivery Time
- Delivery address
- cpupon (relation forienkey) 
- total_with_coupon

## class OrderDetail 
- Order (relation ship)
- product (relation)
- Quantity
- Total
- Price

## class Coupon 
- code 
- start date
- end date
- quatity
- discount  

---------------------------------------------------------------------------------------------------------------------
# App account
## class 
- user 
- address 