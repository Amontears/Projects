Project Description!


Project Type: News website with forms for adding and viewing articles.

Technologies and Tools:

Django — web framework for creating the server-side part of the application.
HTML/CSS/JavaScript — for building the user interface.
Bootstrap — for styling elements and responsive design.
Jinja (Django templates) — for dynamically generating HTML pages based on data received from the server.
CSRF Protection — for protection against Cross-Site Request Forgery (CSRF) attacks.
Project Structure
Templates:

layout.html — base template used by all pages. It contains the common HTML structure (e.g., header, footer, linking of CSS and JS files). Other templates inherit from this base template, which allows for easy management of styles and site structure.
forms.html — template for the form to add news. This template uses an HTML form to collect data from the user, such as title, text, image, date, and time of the news. It also includes CSRF protection using the {% csrf_token %} tag.
news_detail.html — displays detailed information about a specific news article. It includes the title, image, text of the news, as well as buttons for deleting or editing the article.
news_list.html — displays a list of news articles as cards. Each card contains the news title, image (if available), a brief description, and a link to the full article page. The text is truncated using CSS styling (-webkit-line-clamp) to show only part of the text.
Functionality:

Adding News — users can add news through the form on the /add_news/ page. The data is sent to the server via a POST request and saved in the database.
Viewing News — on the homepage, all added news articles are displayed as cards. Each card includes:
Image (if provided),
Title,
Truncated text,
"Read more" button to navigate to the full article page.
Full News Text — on the news detail page, the full text, image, and publication date are displayed. There are also buttons to delete and edit the news article.
JavaScript for "Read more" Button — on the news list page, JavaScript is used to allow the user to expand the full news text by clicking the "Read more" button. The truncated text is hidden, and the full text appears smoothly.
Key Parts of the Templates:

Content Blocks and Dynamic Content: Inside the {% block content %} block, dynamic data is inserted, such as news articles, errors, or messages. These data are retrieved from the server and inserted into the HTML via Django's template language.
Form for Adding News: The template for adding news displays form fields (form.title, form.text, etc.) that are automatically generated from the form defined on the server. Error handling is done by displaying errors in the error block.
Features:

CSS Styling: Bootstrap classes are used for styling elements (e.g., buttons, cards). Also, a specific CSS style is used to control the visibility of the text, which hides the text and reveals it smoothly.
Responsive Design: All pages are responsive, meaning the site looks good on both mobile devices and desktops.
News Deletion and Editing: For each news article, there are buttons to delete or edit, allowing content management on the site.
Important Points for Understanding the Code
How to Add News: To add a news article, go to the form page, enter the required data (title, text, image, date, time), and submit the form. If successful, the news will be saved in the database and will appear in the news list on the homepage.

How the News List Looks: All news articles are displayed on the homepage as cards. Each card includes:

News title,
Truncated text,
Image (if provided),
"Read more" button to navigate to the full text of the news.
Editing and Deleting News: On the news detail page, there are buttons for deleting or editing the news article. The URL with the news id is used to delete the article, and there is also a link to the edit page for making changes.




Описание проекта
Тип проекта: Сайт новостей с формами добавления и просмотра статей.

Технологии и инструменты:

Django — веб-фреймворк для создания серверной части приложения.
HTML/CSS/JavaScript — для построения интерфейса пользователя.
Bootstrap — для стилизации элементов и адаптивного дизайна.
Jinja (Django шаблоны) — для динамической генерации HTML страниц на основе данных, полученных с сервера.
CSRF защита — для защиты от атак с подделкой запросов.
Структура проекта
Шаблоны (templates):

layout.html — базовый шаблон, который используется всеми страницами. Содержит общий HTML-код (например, шапку, подвал, подключение CSS и JS файлов). Остальные шаблоны наследуются от этого базового шаблона, что позволяет легко управлять стилями и структурами сайта.
forms.html — шаблон формы для добавления новостей. Этот шаблон использует HTML-форму для сбора информации от пользователя, такую как заголовок, текст, изображение, дата и время новости. Также включает защиту от CSRF атак с помощью тега {% csrf_token %}.
news_detail.html — отображает подробную информацию о конкретной новости. Сюда включены заголовок, изображение и текст новости, а также кнопки для удаления и редактирования статьи.
news_list.html — отображает список новостей в виде карточек. Каждая карточка содержит заголовок новости, картинку (если она есть), краткое описание и ссылку на страницу с полной версией статьи. Для сокращенного текста используется стилизация с помощью CSS (-webkit-line-clamp), чтобы текст был обрезан и показывался только частично.
Функционал:

Добавление новости — пользователи могут добавлять новости через форму на странице /add_news/. Данные отправляются на сервер с помощью POST-запроса и сохраняются в базе данных.
Просмотр новостей — на главной странице отображаются все добавленные новости в виде карточек. Каждая карточка включает в себя:
Изображение (если оно задано),
Заголовок,
Обрезанный текст,
Кнопка "Read more" для перехода на подробную страницу.
Полный текст новости — на странице подробностей новости отображается полный текст, изображение и дата публикации. Также есть кнопки для удаления и редактирования новости.
JavaScript для кнопки "Read more" — на странице со списком новостей используется JavaScript, который позволяет пользователю раскрывать полный текст новости при нажатии на кнопку "Read more". При этом обрезанный текст скрывается, а полный текст появляется плавно.
Основные части шаблонов:

Блоки контента и динамическое наполнение: Внутри блока {% block content %} вставляются динамические данные, такие как новости, ошибки или сообщения. Эти данные приходят с сервера и вставляются в HTML через шаблонный язык Django.
Форма для добавления новости: В шаблоне для добавления новости отображаются поля формы (form.title, form.text, и т.д.), которые автоматически генерируются из формы, определенной на сервере. Обработка ошибок происходит через отображение ошибки в блоке error.
Особенности:

CSS-стилизация: Использование классов Bootstrap для стилизации элементов (например, кнопок, карточек). Также для управления видимостью текста используется специфический стиль, который скрывает текст и плавно его раскрывает.
Адаптивный дизайн: Все страницы поддерживают адаптивность, благодаря чему сайт хорошо выглядит на мобильных устройствах и десктопах.
Удаление и редактирование новостей: Для каждой новости есть кнопки для удаления или редактирования, что позволяет управлять контентом сайта.
Важные моменты для понимания кода
Как добавить новости: Чтобы добавить новость, нужно перейти на страницу с формой, ввести необходимые данные (заголовок, текст, изображение, дату, время) и отправить форму. В случае успеха новость будет сохранена в базе данных и появится в списке новостей на главной странице.

Как выглядит список новостей: Все новости отображаются на главной странице в виде карточек. Каждая карточка включает:

Заголовок новости,
Обрезанный текст,
Изображение (если оно задано),
Кнопку "Read more" для перехода к полному тексту новости.
Редактирование и удаление: На странице подробностей новости доступны кнопки для удаления или редактирования новости. Для удаления новости используется URL с id новости, а для редактирования — также ссылка на страницу редактирования.

