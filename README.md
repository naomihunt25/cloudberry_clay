# Milestone Project 4 - Cloudberry Clay  

![Mockup of website](documentation/cloudberry-mockup.png)

# Table of Contents
1. [Project description](#project-description)
2. [User Experience (UX)](#user-experience)
3. [Design Choices](#design-choices)
4. [Wireframes](#wireframes)


## Project Description

Cloudberry Clay is a full-stack e-commerce website built for **Code Institute Portfolio Project 4**. It represents a fictional small-batch ceramics brand specialising in colourful, handmade clay art pieces such as vases, dishes, ring holders and other decorative homeware.

The site provides a complete online shopping experience including:
- A responsive front-end with a clean, pastel, creative brand identity  
- Full product catalogue featuring multiple categories  
- Individual product pages with detailed descriptions and images  
- A session-based shopping bag with update/remove functionality  
- Secure checkout using Stripe
- User accounts powered by Django Allauth
- Order history and saved delivery details  
- Admin CRUD management for products  
- AWS S3 hosting for images & static files  

The project is deployed on Heroku with a PostgreSQL database and uses Django to handle routing, authentication, product management, ordering logic, profile storage and secure transactions.

[Return to Table of Contents](#table-of-contents)

## User Experience (UX)
Cloudberry Clay has been designed as a warm, playful and inviting online shopping experience for users who appreciate handmade ceramic art. 

The UX process for this project follows the five planes of user experience:  
Strategy → Scope → Structure → Skeleton → Surface, ensuring decisions made during development were supported by clear user needs and business goals.

### Strategy Plane

Cloudberry Clay aims to connect users with a clay artist's handmade work in a simple, beautiful and trustworthy way. The primary purpose is to allow customers to browse, purchase, and return to view their orders with ease.

#### Business Goals

- Provide a visually appealing and professional online shop for a ceramics brand.  
- Enable easy product creation, editing and removal by the store owner.  
- Build trust through clear layouts, photography and secure payments.  
- Encourage return visits through user accounts and stored delivery info.

#### User Goals

- Browse products quickly and intuitively.  
- View high-quality images and detailed descriptions.  
- Easily manage a shopping bag and adjust quantities.  
- Complete a secure checkout process with Stripe.  
- Create and manage an account with order history.  

### Target Audience

Cloudberry Clay is designed for:
- People who enjoy handmade pottery and unique decorative items  
- Gift shoppers looking for something personal  
- Fans of soft pastel colour palettes and minimal but warm aesthetics  
- Customers familiar with small online craft shops  
- Younger audiences who appreciate Instagram/TikTok-style homeware  

### Personas

To ensure the site meets user needs, three personas were developed to represent typical Cloudberry Clay customers:

#### Persona 1 - Claudia, 24: Creative home stylist

**Goals:**  
- Find unique decor items for her bedroom and living space  
- Easily browse categories and see details of products
- Save time by storing her address for future orders

**Frustrations:**  
- Cluttered websites  
- Confusing checkout processes  
- Low-quality product photos

**How Cloudberry Clay supports Claudia:**  
- Clean product grid & pastel design  
- High-quality images on product pages  
- Saved profile details for quick checkout  

#### Persona 2 - Natalie, 32: Gift Buyer

**Goals:**  
- Purchase a special handmade gift  
- View product dimensions, price and quality clearly  
- Receive email confirmation and clear delivery info  

**Frustrations:**  
- Unclear product information  
- Complicated payment steps

**How Cloudberry Clay supports Natalie:**  
- Product descriptions  
- Clear delivery charge and thresholds  
- Secure, simple Stripe checkout with confirmation  

#### Persona 3 - Mark, 28: Small Business Supporter

**Goals:**  
- Support independent artists  
- Learn the story behind the brand  
- Purchase ethically-made items  

**Frustrations:**  
- Impersonal or overly corporate websites  

**How Cloudberry Clay supports Mark:**  
- Warm “About” page sharing story   
- Personalised brand tone and photography  
- Simple navigation and clear user journey  

### User Stories

User stories were developed to guide features and prioritise functionality using Agile methods. Please visit the GitHub project board [here.](https://github.com/users/naomihunt25/projects/9)


### **Owner Goals**

As a **store owner**, I want to:
- Add, edit, and delete products so I can maintain an accurate catalogue.  
- View orders through Django admin.  
- Ensure user ordering is smooth and secure.  
- Provide clear product information to reduce confusion.  

### **User Goals**

As a **site user**, I want to:
- View the homepage and understand what the store offers.  
- Browse all products quickly and filter them.  
- Click a product to view its full details.  
- Add items to a shopping bag.  
- Update or remove items from the bag.  
- View my bag total, delivery cost, and free delivery threshold.  
- Checkout securely with a card.  
- Create an account to save my details.  
- View and repeat past orders.  
- Log out securely.

### MoSCoW Prioritisation

#### **Must Have**
- Product browsing and detail pages  
- Shopping bag with update/remove  
- Stripe checkout and webhook  
- Order history  
- Profile with saved delivery info  
- Admin product CRUD  
- Responsive layout  

#### **Should Have**
- Toast messages for feedback  
- Custom error pages  
- Search bar  
- Product sorting  

#### **Could Have**
- Wishlist  
- Review system  
- Newsletter
- Multi-image product galleries  

#### **Won’t Have (for now)**
- Live stock levels  
- Gift cards  
- Subscription model  

### UX Structure

The site’s structure follows a clear hierarchy:
- Homepage introduces the brand  
- Navigation gives direct access to products, account, and bag  
- Product catalogue offers sorting and filtering  
- Product detail pages provide images and information  
- Bag & checkout maintain transparency and clarity  
- Profile page gathers all user information and orders  

### Skeleton Plane

Key wireframe decisions included:
- Clean card layouts for products  
- Clear, vertical checkout form structure  
- Prominent “Add to Bag” button  
- Consistent spacing and margins  
- Mobile-first considerations for small screens  

### Surface Plane

Cloudberry Clay’s final UI embraces:

- Pastel pink and blue accents  
- White backgrounds for clarity  
- Rounded UI elements  
- High-quality product imagery  
- Minimal text for readability  

The result is an aesthetically pleasing shopping experience that stays true to the handmade brand concept.

[Return to Table of Contents](#table-of-contents)

## Design Choices

Cloudberry Clay’s design reflects the brand’s focus on handmade ceramics and creative home décor. The aesthetic combines soft pastel tones, generous white space, and clean typographic choices to highlight product photography and create a welcoming shopping experience.

### Typography

- **Roboto Mono**  
  Ensures clarity and readability throughout the site, especially on product descriptionsa and checkout pages.

- **DM Serif Display**  
  Brings an elegant, artistic feel that suits the handcrafted ceramic theme. Its soft curves and high-contrast strokes create a boutique, studio-like atmosphere, giving the brand a refined but warm personality.

### Colour Palette

The colour scheme is based around soft pastel tones that support the brand’s warm and creative identity:

- **Pink (#FF95DE)**  
  Used for primary buttons, promotional highlights, and call-to-action elements. This adds a sense of charm and playfulness to the interface.

- **Blue (#7AA4FF)**  
  Used for secondary accents, category labels, and subtle UI elements. This introduces calmness and contrast without competing with product photography.

### Visual Style & Imagery

- **High-quality product photos** with clean, minimal backgrounds ensure the textures, shapes, and colours of each ceramic piece are clearly visible.  
- **Rounded buttons** and soft shadows echo the organic forms of handcrafted clay.  
- **Grid-based product layouts** create structure while allowing each item to stand out.  
- **Hero imagery** sets a warm, creative tone, instantly communicating the brand identity.  
- **Minimal UI clutter** keeps focus on the ceramics and improves user navigation.

### Accessibility & Responsiveness

- Font sizes, spacing, and contrasts were chosen to ensure readability across devices.  
- Interactive elements include clear hover states and feedback via toast messages.  
- Alt text is applied to product imagery for accessibility.  
- The layout adapts gracefully across desktop, tablet, and mobile screens.

[Return to Table of Contents](#table-of-contents)

## Wireframes

Wireframes were created during the planning stage to map out the structure and layout of each key page. The aim was to ensure a simple, intuitive shopping experience while keeping focus on product imagery and clear navigation. Below are the wireframes used to guide development.

### Home Page Wireframe

The homepage introduces the brand through a hero image, a short tagline, and clear navigation to products and categories. Featured items help guide users into the catalogue.
![Home page wireframe](documentation/wireframes/home-wireframe.png)

### Products Page Wireframe

The products page uses a grid layout to display all available items with filtering and sorting options.
![Products page wireframe](documentation/wireframes/products-wireframe.png)

### Product Detail Page Wireframe

This page shows a large product image, detailed description, price, quantity selector and the “Add to Bag” button. The aim is clarity and a strong visual focus on the ceramic piece.
![Product detail wireframe](documentation/wireframes/product-detail-wireframe.png)

### Shopping Bag Wireframe

The shopping bag displays item images, quantities, totals and options to update or remove items before checkout.
![Shopping bag wireframe](documentation/wireframes/bag-wireframe.png)

### Checkout Page Wireframe

The checkout form collects delivery details and integrates with Stripe for payment. The layout keeps everything simple and linear to reduce friction.
![Checkout wireframe](documentation/wireframes/checkout-wireframe.png)

### Login / Signup Wireframes

These forms allow users to create an account or access existing profiles.
![Login wireframe](documentation/wireframes/login-wireframe.png)  
![Signup wireframe](documentation/wireframes/signup-wireframe.png)

[Return to Table of Contents](#table-of-contents)