# MaidEase 🧹👩‍🍳

**MaidEase** is a secure and user-friendly web application that allows users to find, book, and manage reliable domestic help such as maids for cleaning, cooking, babysitting, and elder care. Built with Flask (Python) and MySQL on the backend, and HTML, CSS, JS, and Bootstrap on the frontend.

---

## 🚀 Features

- ✅ Maid registration and profile verification  
- 🔐 Secure user authentication (Bcrypt encryption)  
- 📆 Maid booking system with OTP-based verification  
- 🧾 Admin dashboard for managing maids, users, and payments  
- 🌐 Responsive UI with Bootstrap  
- 📲 Notifications and booking confirmation  
- ⭐ User reviews and ratings  

---

## 🧩 Tech Stack

| Layer      | Technology                     |
|------------|--------------------------------|
| Frontend   | HTML, CSS, JavaScript, Bootstrap |
| Backend    | Flask (Python)                 |
| Database   | MySQL                          |
| Security   | Bcrypt for password hashing    |
| Deployment | Render (Backend) + GitHub Pages / Netlify (Frontend) |

---

## 📁 Project Structure

/maidease
├── /static # CSS, JS, images
├── /templates # HTML templates (Jinja2)
├── app.py # Main Flask application
├── models.py # SQLAlchemy models
├── routes/
│ ├── auth.py # Login and registration
│ ├── booking.py # Maid booking routes
│ └── admin.py # Admin functionality
├── utils/
│ └── otp.py # OTP generation and validation
├── config.py # Configuration variables
└── requirements.txt # Python dependencies


---

## 🛠️ Installation & Setup

```bash
git clone https://github.com/your-username/maidease.git
cd maidease
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Set up .env with DB and secret config
flask run

🧪 Demo & Loom Walkthrough
🔗 Live Demo

📹 Loom Video Walkthrough

📦 Deployment
Backend: Deployed using Render

Frontend: Deployed using GitHub Pages or Netlify

.env used for environment variables

CORS and static file handling configured in app.py

🧠 Challenges Faced
Integrating a secure OTP-based booking confirmation system

Ensuring smooth user experience across different services

Implementing session-based auth and role separation (user, admin)

📈 Future Improvements
Convert frontend to React.js for a more interactive UX

Add role-based access control with JWT for APIs

Integrate payment gateway (e.g., Razorpay, Stripe)

Add multilingual support for broader reach

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

📄 License
This project is licensed under the MIT License.
---
## 📸 Screenshots
---
👤 Author
Vaibhav Rahane
📧 Vaibhavrahane37@gmail.com
📱 +91 8806142916
🔗 LinkedIn


---

✅ Just replace the following with your actual links:
- `https://github.com/your-username/maidease.git`
- `https://your-live-link.com`
- `https://loom.com/share/your-video-link`

Let me know if you also want a `.env.example` or `requirements.txt` template!
