
## TODO:
- make constraing on review (one user can add one review) coding ??

## video 30 :
- related don't add to db as (calculated field)
- design db 




## video 27 Django Template & API
- using rest API in 3 cases :
  - mobile App
  - JS framework (react ,angular ,vue)
  - microservice archetecture.
- Monolithic architecture -->simple or general of using building website (usint one DB)
- Micrservice architecture----> complex (using on big website and very cost) (divide website to multible service every service using ther DB)
- SAAS & Multitennant
- api file instead of views file (for arrange code)
- serializer file is like form file (responsible for convert data to json)


## video 28 Django API part2
- querysert ----> the model what you want to apply api on it .


## video 31 build view and add dummy_data

- understand using of fake library to add data .
- add image manualy to media and added path using fake to db .
- in the up of file must add tow lines to django know that file belong to him as we using in it ORM .

## video 33

- add logic from template make loading on browser and make website slow.
- add logic from view or model make your website faster .
- best practice add logic in view as you can use it in every place in your project until(API)
- when work with pagination in CBV in template don't make space in url.
- fat model thin view .

## Class based view

- context {}:(return or workin with extra data )(relationship in table)
  - option  -->doing some thing clear don't need data from any place
    - هعمل حاجه واضحه وصريحه مش محتاج داتا من اي مكان
  - method (override change behaviour on it) --> when doing big logic
- queryset: product.object.all()  (working with maing query) (fields on table )
  - option
  - method

- queryset -->list & detail product (filter on list) return maing query and doing filter on it {post}
- context --> review &images in detail (user from product list){comments}

## video 34 API

- make two files api (view) serialzers (form)
- add api for product ,brand list and detail.
- any change on data doing from serializers.
- make method in serialzers and using object.(name_of_relation).all()
- find all reviews in product.
- add method in serialzers to calculate avg_rate and review count.
- the name of method must start with get_lsdj() , and using the name lsdj as acolumn in db .

## video 35

- django queryset api .
- add simple class meta in model .
  
## video 36

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
- the best server to using cacching is reddis.
- if u have problem to setup reddis in windows no problem when usin docker it will be fine as reddis built on linux.
- setup redis on your pc and redis for python on Virtual Envirmonent and add redis setting for django .
- using caching decorator to add function to cache.
- when using caching with context processor you using manually caching.
- explain about salary of build a project for client.

## video 37

- using taggit restframework to show it in api.
- import in setting.view  what we want to show in home (product ,reviews,brand)
- we can using another technology to generat api (ninja build on new tech in python pendatic(fast& like fast api) ,grpc)
- finish home page.
- how can we add review on product .
- when want form to send data using method post and add csrf token.
- the action in front end in form detect where you want to sent data from form.
- to recieve data from form fields all fields must have name.
- if i have an integer field in (model db) when recieve it from front-end the field must have a value .
- using in template user.is authenticated to show login or image of user.
- create app for order.
- create app account to build model address to using it in order.
- when i have multible fields repeated and other not repeated it best practice to build it in tow model like(product & prouct_images ,product & reviews ,orders & order_detail)
- when i build a function and i probably using it in more places it's best practic to create folder  
  (utils/name_function.py)
- save price of product on order as the price maybe will change on the future.
- when i want tow add 7 day on datefield we must using timedelta .
- (autonow & autonow_add) apear only only on data base so when i using to date to apear for admin u must using default.


## video 38 (Orders part2 )
- lazy django ORM -> meanin if i have tow operatin like(filter & order_by) and i will apply them on the DB, Django ORM merge them on one query and apply them on DB.
-  queyset cache -> the variable that contain the result of applying the query on DB & can apply on it another query ,then result come from the variable don't go to DB.
-  example: 
      -  data = products.objects.all()
      -  data2 =data.filter('name') --->here I am using queryset cach
- using data inside cart(model) to create order object when payment.
- the price in cart come from DataBase(product.price) as the price maybe change befor payment.
- the price in orders come from (orders.price) as i will payment immediately . 
- create model delivery fee in setting app.
- build views for order app .
- get or create cart for user logged in .
- build simple view (get_cart_data) and using in context processor to check if user have a cart or create new one for hem.
- show cart_detain in base as I return data from context processor.
- add function on model to calculate total price and make it @property to using it any where as acolumn.
- build view add-to-cart to add object to cart .


## video 39 (orders-part3)
- show produts detail from cart in checkout page.
- how can apply copoun?
- null---> apply on Data Base.
- blank--> apply on django form.

---------- API---------
I want to show in api what i showed in views(orders list,detail,applycoupon)
- it is best to recieve user in url when using API.--> path('api/<str:username>/orders' ,OrderListAPI.as_view())
- how can you override on query order.objects.all() and apply filter with username?
  - using get_query_set() why??
    - (working with maing query) as return maing query and doing filter on it.

- in order_detail_api --> no update no filter no delete no search as i bought the products and I was payment.
- how can I get user??
  - In django it's best to using request.user.
  - In rest it's best to using url (from mobile app)
  - ممكن المستخدم ما يكونشي ظاهر في الريكويست معنديش حد عامل login
- I can send one varible or tow in url.
- but in request.body I can send alot of data.


## video 40 (Cart API):

- add if condition in product_detail.html in form (add to cart) to check if the product.quantity>0 show it else (out of stock)


## video 41 (user part 1):
- I am work on app Account(Address , Profile , ContactNumber)
- create DB (profile for user)
- create view for signup 
- when user signup It will create new user automatically from django user and I will use signal to create( new profile)
- then i will send email to activate(using send_maile function to send email & add configuration in setting file) .
- after activate i will redirect to login page.

- in minute 48 talke aboute drage drop component of html online.
- django by default login only by username .
- so we will create file(backend.py) and create class to login by usernane or email this class inherite from (ModelBackend).
- add in settin file configuration for send gmail.


## video 42 (user part2)
- add authentication for django for urls.(accounts)
- add frond end for authentication(mozila developer)
- add all authentication files in regestiration inside template.
- add password_change_form.html .
- connect django regisstration pages to temaplate  i have 3 ways:
  -  using django bootstrap5 .
  -  render form manual for every field (lose django validation ).
  -  inside djngo form(but in my way i don't have django form) customize on forms.py and give it css classes.
-  in minute 43 talk abount permition of api and token.
- how using token authentication in api?
  - add it in installed app.
  - add in setting of rest.
  - add in my api class     permission_classes = [IsAuthenticated]

- from minute 54 test endpoint on post man and make docs.(not applied)
  
  



## video 43 (Auth API and chart ):(no applied)
- we added out of stock in product detail now we will add it in product list.
- will add out of stock as obtion in adminpanel to filter products based on quntity in session of adminpanel.
- TOKEN:
  - jwt token best than django token. ------------ name of library(django simple jwt).
  - i can get only user from django token.
  - but i can get alot of information from jwt token.
  - jwt token is secure than django token & encryption is better.
  - jwt token divide to 3 parts.
  - (the last part in jwt token is to ensure that the token don't change)
- full authentication system (login-->get token).------------------------name of library(dj_rest_auth(for API))(django all auth(without API))
- what is access token and refresh token(minute 18).
- using docs to add signup to authentication (registration).
- make all end point secure (add in setting ).
- chartjs ( minute 27 ) make dashboard
----translation (notapplied)


## video 45 (docker part1 ):
- when using postgres with django u must install (psycopg2-binary)
ASK:
  - ممكن المستخدم ما يكونشي ظاهر في الريكويست معنديش موقع معنديش حد عامل login