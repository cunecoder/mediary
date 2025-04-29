# Welcome to Mediary!

This project is a group event planning platform designed to simplify coordination among friends and family, built for practice and fun!

### Prerequisites

To run this project locally, you will need the following:

- **Git**: Version/source control
- **UV**: Virtual environment manager for Python
- **Python**: Version 3.8 or higher

### Installation

To install this project, clone the repository and run the following commands:

```bash
git clone https://github.com/yourusername/mediary.git
cd mediary
uv sync
uv run manage.py makemigrations
uv run manage.py migrate
uv run manage.py runserver
```

### Features

From there, you can create an account and start planning events! Create events, invite participants, and manage preferences all in one place. 

From the home page, you can browse public events and user profiles. When logged in, you can create events, view event details, and update event preferences!

- User registration and login
- Event creation and listing
- Event detail pages
- Responsive UI with Bootstrap 5
- Custom user model with email login
- Mobile-friendly design
- Navigation bar with authentication-aware links

### Code

There's also a collection of unit tests that utilize Django's built-in testing tool.

#### Example Test

Here is an example of a unit test for creating an event:

```python
def test_create_event(self):
    user = User.objects.create_user(email="user@example.com", password="password")
    
    event = Event(
        title="Test Event",
        description="A fun gathering",
        date="2025-06-01 15:00:00",
        organizer=user,
    )

    event.full_clean()
    event.save()
    event.refresh_from_db()

    self.assertEqual(event.title, "Test Event")
    self.assertEqual(event.description, "A fun gathering")
    self.assertIsNotNone(event.date)
    self.assertEqual(event.organizer, user)
```

### Future Ideas

- Utilize [Bandit](https://github.com/PyCQA/bandit) for security
- Use [Playwright](https://playwright.dev/docs/intro) for end-to-end testing
- Add real-time notifications for event updates
- Implement event RSVP and preference voting system