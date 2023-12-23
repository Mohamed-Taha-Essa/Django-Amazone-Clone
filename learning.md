# video 31 build view and add dummy_data:
  - understand using of fake library to add data .
  - add image manualy to media and added path using fake to db .
  - in the up of file must add tow lines to django know that file belong to him as we using in it ORM .


# video 33

- add logic from template make loading on browser and make website slow.
- add logic from view or model make your website faster .
- best practice add logic in view as you can use it in every place in your project until(API)
- when work with pagination in CBV in template dom't make space in url.
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
  - make to files api (view) serialzers (form)
  - add api for product ,brand list and detail.
  - any change on data doing from serializers.
  - make method in serialzers and using object.name of relation.all()

