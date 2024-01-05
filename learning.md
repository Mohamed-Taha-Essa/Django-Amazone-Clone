# video 31 build view and add dummy_data:
  - understand using of fake library to add data .
  - add image manualy to media and added path using fake to db .
  - in the up of file must add tow lines to django know that file belong to him as we using in it ORM .


# video 33
  - add logic from template make loading on browser and make website slow.
  - add logic from view or model make your website faster .
  - best practice add logic in view as you can use it in every place in your project until(API)
  - when work with pagination in CBV in template don't make space in url.
  - fat model thin view .

# Class based view:
  - context {}:(return or workin with extra data )(relationship in table)
      - option  -->doing some thing clear don't need data from any place
        -  هعمل حاجه واضحه وصريحه مش محتاج داتا من اي مكان
      - method (override change behaviour on it) --> when doing big logic
  - queryset: product.object.all()  (working with maing query) (fields on table )
      - option 
      - method

- queryset -->list & detail product (filter on list) return maing query and doing filter on it {post}
- context --> review &images in detail (user from product list){comments}


# video 34 API
  - make two files api (view) serialzers (form)
  - add api for product ,brand list and detail.
  - any change on data doing from serializers.
  - make method in serialzers and using object.(name_of_relation).all() 
  - find all reviews in product.
  - add method in serialzers to calculate avg_rate and review count.
  - the name of method must start with get_lsdj() , and using the name lsdj as acolumn in db .
# video 35 :
  - django queryset api .
  - add simple class meta in model .
  

# video 36 :
  - add instance method in model .
  - call this method in any where in your project.
  - call method in seraializers to show it . 
  - delete method from serializers and using that in model .
  - add property decorator to show the method as field in db .
  - to show the instance method in serializers must using fields = [name of methods]
  - any project must have settings app .
  - must start with finish home page in your project .
  - to return the data that show on all pages in your project must using [context_processor]
  - when usin [context_processor] to return data it return in almost page in project and the data don't change for long time so we cand using caching to solve this probelm.
  - using library on caching or use it manually.