#Milestone Project 4 - Cardiff Magic Society

## Project aim

The aim of the project is to build a functional website for Cardiff Magic Society

## Background

Cardiff Magic Society is club based in cardiff for magicians and people interested in magic. The club holds regular monthly meetings which involve performances, lectures, social gatherings, workshops and other events. The society also has its own magic supply for members to buy magic items. As the working of magic is secret the society only allows the genral public access to certain areas of the societies activities for example some meetings are members only meetings.

### Why a website

The society use to have a website for members or anyone interested detailing when the meetings were and how to join. Members had issues with the site as it was hard to update and manage, didnt have much useful information and didnt look like a creditable site. Recently they switched to just using social media, however they have run into issues with this approach. Not all members on social media, and not all members on social media use the same platforms meaning more social media accounts are needed to be maintained and updated regularly.
A new functional website will give all members or anyone interested one location to find all the information about the society.

## Website features

### Research

To find out what they want for the website I had a meeting with the society board members and general mebers about what they would like to see from a website for the club. The main reoccuring points were :

- up to date calender on society upcoming events
- mordern looking website which is easy to navigate
- up to date news on the magic world
- access to magic shop
- access to videos of past lectures
- to advertise members private performnce services
- how to join the society 
- Gallery of photos taken at meetings
- An easy to maintain website, easily updateable calender, gallery, news

### Website Needs

To incorporate what the society wants from a website I have broken down the requirements into website pages for the site

- About : describing the society and what its about
- Contact : how to get in contact with the society and where it meets
- How to join : how to join the society
- Gallery : pictures from society meetings
- Magicians for hire : advertisements of magic services from members
- Profile : a private individual area for members to update their own information.
- shop : to sell society product online

### Design Needs

- Modern looking : proffesional looking website
- Easy Navigation : the website should be intuitive to navigate
- Easy to update : Key areas that regularly change need to be easy for a user to modify eg. calender, latest news
- Restricted Access : members only information restricted from public access
- All devices : Website should function on all size screens

### User Needs

Due to the nature of the society I have identified three different types of users who would be accessing the website each with their own user story:

- The General Public : Anyone browsing the internet, or looking for magic content/information
- Assoiciate Member : Someone with a keen inerest in or performs magic,
- Admin Member : A member of the society who is in charge of updating calender and events

#### General public

As a general user I want to :
- To understand what the society is about : So I know what its about
- see visual representation of what the society is like : So I can get a feel for what it like
- understand the process to join the society : So I know how to join
- find a magician to hire : So I can hire entertinment for an event
- see when the next meeting is : So I can attend
- contact the society : To make enquires
- sign up as a member : to join the society 

#### Assoiciate Member

As an assoiciate user I want to :
- see latest news : so I know what is currently happening in the magic world
- access the shop : so I can purchase magic goods
- see my previous shop order : so I know what I have previously brought 
- put up an advertisement : to advertise my magic performance to the general public
- edit my advert : to update my advert with my latest info

#### Admin Member

As an admin user I want to :
- update calender : to add, delete or make changes to up coming events
- update gallery : add new images to show current look and feel of society

## Action Plan

To achieve the requirements of the society I'm going to build a website consisting of 11 pages with 3 levels of access
public , assoiciate , admin. Each level will have the appropriate pages hidden from them up to member which has access to all pages. Admin user will have member level access with the additional edit buttons to update relevant pages.

website pages :

- Home : will contain information about society and contact information
- How to join : will contain information on how to join the society
- Gallery : will contain images from society nights
- Magician's for hire : Will contain adverts from members for their private performance services
- sign in/ register : Where you can fill in form and sign up or sign in to the Society
- Profile : Personal page for user once signed up to edit details, see purchase history, create advert
- Latest News : containing latest magic world news
- Shop : containing society products for sale


Public Access : Home, How to Join, Gallery, Magician's for Hire, sign in/register

Assoiciate Member : Home, How to Join, Gallery, Magician's for Hire, sign in/register, Profile, Latest News, Shop

Admin member will have the ability to edit : Magician's for Hire,  Latest News, Shop, Gallery 

Website will be built using : Django framework, Python, Javascript, CSS, HTML, MySQL


## Design Layout

### Sketched Layout

### Main Page View - large monitor

<img src="media/readme_images/main_sketch.jpeg">

### Main Page View - tablet

<img src="media/readme_images/tablet_sketch.jpeg">

### Main Page View - mobile

<img src="media/readme_images/mobile_sketch.jpeg">


### Actual Layout


## Code Structure

Django apps :
- bag -------------- contains html templates and models.py for shopping bag found in navbar under profiles
templates - bag.html
- calender --------- contains html templates and models.py for calender and editing calender 
templates - calender.html  add_event.html   edit_event.html
- checkout --------- contains html templates and models.py for checkout and stripe payment system
templates - checkout.html checkout_success.html confirmation emails - confirmation_email_body.txt confirmation_email_subject.txt
- gallery ---------- contains html templates and models.py for gallery and editing gallery
templates - gallery.html  add_image.html
- home ------------- contains html templates and models.py for home page, maintenance page and how to join page
templates - index.html(home page)  join.html  maintenance.html  
- magician --------- contains html templates and models.py for Hire a magician page, and editing
templates - add_hire.html  edit_hire.html  magic_hire.html
- management ------- contains html template for site management page, which has edit button links to other apps
templates - mangement.html
- profiles --------- contains html templates and models.py for users profile page, and editing address/advert
templates - order_history.html  profile.html
- shop-------------- contains html templates and models.py for shop and editing products
templates - shop.html  add_product.html  product_detail.html  edit_product.html

- media ----------- contains images for the shop products
- templates ------- contains base.html template for website, allauth, includes- toasts for website
- Static----------- contains base.css for website

#### templates/Base.html

- is the main template for the website, it contains a title, navbar and footer which are used on every page throughout the site.

#### static/css/base.css

- contains primary css styling for the base.html and the website. The checkout app has its own css file for specfic features,(also has its own js as well).

base.css structure :

- font style for buttons
- blank space filling for maintenace page and log in page
- Header 
- home page images
- bootstrap toasts 
- media queries title
- Allauth form formatting
- Galley


## Coding Bugs

- title stuck fixed to top of screen
- toasts x not working 
 - subtotal code not working
  <p class="my-0 small text-muted">${{ item.product.price | calc_subtotal:item.quantity }}</p> 
- unable to connect static files to s3
- s3 acl settings keep reverting
- media files not uploading correctly to s3
- email not working
                        

### fixed 

### unfixed


## Testing 


## Deployment


## Credit 


## Evaluation


## Future Changes
