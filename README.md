
# Django E-commerce Project

A full-featured e-commerce application built with Django,Django REST framework,Django-template..., designed to deliver a seamless shopping experience. The project includes REST API endpoints,This project includes features like custom user authentication, profile management, dynamic cart updates with AJAX, Stripe integration for secure payment processing, coupon functionality, and order tracking. It leverages Django templates to create an intuitive frontend experience and follows a structured backend architecture for scalability.


---

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
  - [Web Views](#web-views)
  - [API Endpoints](#api-endpoints)
- [Models and Relationships](#models-and-relationships)
- [Custom Authentication Backend](#custom-authentication-backend)
- [Signals](#signals)
- [Forms](#forms)
- [Utilities](#utilities)
- [Templates and AJAX](#templates-and-ajax)
- [Stripe Integration](#stripe-integration)

---

## Project Structure

```plaintext
.
├── accounts/                        # User account management
│   ├── models.py                    # User Profile, Contact Numbers, Addresses
│   ├── views.py                     # Signup, Activation, Dashboard views
│   ├── urls.py                      # Account endpoints
│   ├── forms.py                     # Signup and Activation forms
├── orders/                          # Order and cart management
│   ├── models.py                    # Order, OrderDetail, Cart, CartDetail, Coupon
│   ├── views.py                     # Order views
│   ├── urls.py                      # Order-related endpoints
│   ├── api.py                       # REST API endpoints for orders, cart, and coupons
├── utils/                           # Utility scripts and functions
│   ├── generate_code.py             # Code generator for coupons and profiles
│   ├── backends.py                  # Custom backend for email/username login
├── products/                        # Placeholder for product and brand models
├── settings.py                      # Django project settings with required libraries
└──...
```

---

## Features

1. **User Authentication and Profile Management**
   - **Registration & Activation**: Users sign up with a custom `SignupForm`, and a profile is created automatically using Django signals. A verification code is emailed for activation.
   - **Profile Management**: Users can manage profile details, including multiple contact numbers and addresses.

2. **Dynamic Cart Management with AJAX**
   - **Cart Functionality**: Users can add products to the cart and dynamically update quantities. The cart total updates automatically with AJAX, creating a smoother shopping experience.
   - **Coupon Support**: Users can apply discount codes to their cart, and the total recalculates instantly.

3. **Order Processing**
   - **Order Tracking**: Each order has a status (Received, Processed, Shipped, Delivered) and delivery time calculated automatically.
   - **Order History**: Users can view their past orders with details on items, quantity, price, and order status.

4. **Stripe Integration for Payments**
   - **Secure Payment Processing**: Stripe is integrated for handling payments. After checkout, users are redirected to Stripe for payment and back to the app for success/failure updates.

5. **API Endpoints for Cart, Orders, and Coupons**
   - Provides RESTful API endpoints for managing cart items, creating orders, viewing orders, and applying coupons.



---

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

---

## Usage

1. **Create a superuser for accessing Django’s admin interface:**
   ```bash
   python manage.py createsuperuser
   ```
   
2. **Access the admin dashboard:**
   - Go to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

3. **User Signup and Profile Activation:**
   - Users sign up through `/accounts/signup`, and an activation email is sent to the provided email address.
   - Users can activate their account with the code at `/accounts/<username>/activate`.

---

## Endpoints

### Web Views

| Endpoint                       | Description                          |
|--------------------------------|--------------------------------------|
| `/accounts/signup`             | User registration and profile creation. |
| `/accounts/<username>/activate` | Activate user account with a code.  |
| `/accounts/dashboard`          | Dashboard view showing product, brand, and review counts. |
| `/orders`                      | List of all orders for the user.     |
| `/checkout`                    | Checkout page.                       |
| `/add-to-cart`                 | Add items to the shopping cart.      |
| `/checkout/payment-process`    | Process payment.                     |
| `/checkout/payment/success`    | Payment success page.                |
| `/checkout/payment/failed`     | Payment failure page.                |

### API Endpoints

| Endpoint                                | Method | Description                           |
|-----------------------------------------|--------|---------------------------------------|
| `/api/<username>/orders`                | GET    | List all orders for a user.           |
| `/api/<username>/orders/<pk>`           | GET    | Retrieve details of a specific order. |
| `/api/<username>/apply-coupon`          | POST   | Apply a coupon to an order.           |
| `/api/<username>/cart`                  | POST, PUT, DELETE | Add, update, or remove items from the cart. |
| `/api/<username>/order/create`          | POST   | Create a new order.                   |

---

## Models and Relationships

### Accounts Models

1. **Profile**
   - Linked to `User` via a one-to-one relationship.
   - Includes fields like `image` and `code` (activation code).
   
2. **ContactNumber**
   - Stores multiple contact numbers for a user with types (Primary, Secondary).

3. **Address**
   - Stores multiple address entries for a user with types (Home, Office, Business, etc.).

### Orders Models

1. **Order**
   - Stores order details including status, order time, delivery time, and total amounts.
   
2. **OrderDetail**
   - Stores individual line items for each order, linked to a `Product`.

3. **Cart**
   - Holds cart information with total cost, coupon, and a status indicator.

4. **CartDetail**
   - Stores details of each cart item.

5. **Coupon**
   - Stores coupon codes with start and end dates, quantity, and discount amount.

---

## Custom Authentication Backend

The `UsernameOrEmailLogin` backend allows users to log in using either their email or username. It tries to find a user by email first and falls back to username if email is not found.

**Code Example:**
```python
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class UsernameOrEmailLogin(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
        return None
```

---

## Signals

Django signals are used to automatically create a `Profile` instance whenever a new `User` is created. This ensures that each user has an associated profile right after registration.

**Code Example:**
```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

## Forms

1. **SignupForm**
   - A form for registering a new user with username, email, and password fields.

2. **ActivateUserForm**
   - A form for entering an activation code to activate a user account.

**Code Example:**
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ActivateUserForm(forms.Form):
    code = forms.CharField(max_length=10)
```

---

## Utilities

1. **`generate_code.py`**
   - Contains a function to generate unique codes for user profiles, orders, and coupons.

2. **`backends.py`**
   - Holds custom authentication backends such as `UsernameOrEmailLogin`.



## Templates and AJAX

- **AJAX Cart Updates**: AJAX is used to refresh the cart total dynamically when items are added or removed, without reloading the page.
- **Templates**: The application uses Django templates to render views. Key templates include:
  - `cart.html` for displaying cart details
  - `checkout.html` for processing orders
  - `dashboard.html` for user account management

---

## Stripe Integration

1. **Checkout Process**: Users are redirected to Stripe for secure payment.
2. **Payment Confirmation**: Upon successful payment, users are redirected back to the application to view their order confirmation.
3. **Error Handling**: Failed payments are also handled with appropriate notifications.

