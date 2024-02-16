# CinemaPlus Project Overview

## Chapter 1: Project Overview and Django Models

### Project Overview:
The CinemaPlus project aims to develop a comprehensive movie website with various functionalities to cater to both administrators and regular internet users. It encompasses features such as presenting basic movie information, showcasing contributors, and allowing users to navigate through a diverse collection of movies.

### Participants:
The project involves the following participants:
- Petros Strigkas
- Thanos Goulianos
- Kiki Delimichali

### Django Models Explanation:
This section provides an in-depth breakdown of the Django models implemented in the application:
- **Director Model:** Describes a director with attributes like first name, last name, and birth date.
- **Genre Model:** Defines a genre of a movie with a single attribute, the name.
- **Movie Model:** Represents a movie with features such as title, duration, release date, IMDb URL, image, summary, director, and genre.
- **Actor Model:** Characterizes an actor with fields like first name, last name, and birth date.
- **Play Model:** Establishes a connection between actors and the movies they appear in.
- **Review Model:** Captures reviews for movies, including attributes like author, rating, and comment.

### Summary:
In summary, the CinemaPlus project endeavors to create an extensive movie website using Django, managing data related to directors, genres, movies, actors, and reviews through Django models. These models provide a structured foundation for the website's functionalities and user interactions.

## Chapter 2: Django Admin Configuration and Views

### Django Admin Configuration:
The provided code resides in the `admin.py` file of the Django application and is utilized to register models with the Django admin interface. Django admin enables easy management of database data through a web-based interface.

### Views Explanation:
This section includes various views for the Django application, each serving a distinct purpose:
- **home View:** Retrieves parameters from the URL query string, filters movies based on specified criteria, and renders the home page template with the retrieved movies for display.
- **movie_detail View:** Retrieves data of a specific movie, fetches reviews for the movie, handles review submissions, and calculates the average rating.
- **aboutus View:** Renders the 'About Us' page.
- **user_login View:** Handles the user login process.
- **register View:** Manages the user registration process.

### URLs Configuration:
The provided Django code defines URL patterns for the website, associating each pattern with a view function and a unique name. Additionally, it includes settings for handling static and media files during development.

### URL Patterns:
Defines URL patterns for different functionalities such as user login, home page, movie details, and about us page. Utilizes path converters to extract dynamic data from URLs.

### Serving Media Files during Development:
Dynamically adds settings for serving media files to urlpatterns, enabling media file handling during development.

## Chapter 3: Home Page Template (home.html)

### Template Inheritance:
The `home.html` template extends the base template named `bootBase.html`, inheriting its layout and structure.

### HTML Document Structure:
Includes the document's title, character set declaration, and viewport settings for responsiveness. Imports external CSS and JavaScript libraries like Bootstrap for enhanced styling and functionality.

### Content Block:
Defines a content block named `content`, serving as a placeholder for dynamic content on the home page.

### Search Form:
Provides a search form allowing users to search for movies, comprising a text input field and a submit button wrapped inside Bootstrap grid columns for layout consistency.

### Carousel for Movie Display:
Features a carousel dynamically displaying movies fetched from the database. Utilizes Bootstrap's carousel functionality for smooth transitions between movie images and details.

### Carousel Controls:
Previous and Next controls are provided to navigate through the carousel slides, enhancing user experience and interaction.

## Chapter 4: Movie Detail Template (movie_detail.html)

### Template Inheritance:
The `movie_detail.html` template extends the base template named `base.html`, inheriting its overall layout and structure.

### Content Block:
Defines a content block named `content`, serving as a placeholder for the main content of the page.

### Movie Details:
Displays detailed information about a specific movie, including its title, image (if available), summary, and genre. Provides a hyperlink to navigate back to the home page filtered by the movie's genre.

### User Reviews:
Presents user reviews in an unordered list, including the author, rating, and comment for each review. Displays a message if no reviews are available.

### Add Review Form:
Includes a form for users to add new reviews, with fields for rating (1 to 10) and comments. Utilizes the POST method for secure submission and prevents CSRF attacks.

### Average Rating:
Displays the average rating of the movie based on user reviews at the bottom of the page.
