# 🤖 ChatGPT Clone

A modern, responsive ChatGPT clone built with Django and OpenAI API. Features a beautiful chat interface with real-time messaging, typing indicators, and mobile-responsive design.

![ChatGPT Clone](https://img.shields.io/badge/Django-5.2.6-green) ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-blue) ![Responsive](https://img.shields.io/badge/Responsive-Yes-purple)

## ✨ Features

### 🎨 **Modern UI/UX**
- **Beautiful Gradient Design** - Purple-blue gradient backgrounds
- **Chat Bubbles** - WhatsApp-style message bubbles
- **Real-time Typing Indicators** - Animated dots when AI is responding
- **Smooth Animations** - Professional hover effects and transitions
- **Mobile Responsive** - Works perfectly on all devices

### 🚀 **Technical Features**
- **Django Backend** - Robust and scalable web framework
- **OpenAI Integration** - GPT-4o-mini model for intelligent responses
- **AJAX Communication** - No page refresh needed
- **Environment Variables** - Secure API key management
- **Error Handling** - Graceful error messages and debugging

### 📱 **Responsive Design**
- **Mobile First** - Optimized for smartphones
- **Tablet Support** - Perfect for iPad and Android tablets
- **Desktop Ready** - Beautiful on large screens
- **Cross-Browser** - Works on all modern browsers

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- OpenAI API key

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd chatgpt_site
```

### Step 2: Install Dependencies
```bash
pip install django openai python-dotenv
```

### Step 3: Environment Setup
1. Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your-openai-api-key-here
```

2. Get your OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Step 4: Run the Server
```bash
python manage.py runserver
```

### Step 5: Access the Application
Open your browser and go to: `http://127.0.0.1:8000/`

## 📁 Project Structure

```
chatgpt_site/
├── .env                     # Environment variables (API keys)
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
├── chatbot/                # Main app directory
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py            # Chat logic and API integration
│   ├── tests.py
│   └── templates/
│       └── chatbot/
│           └── chat.html    # Main chat interface
├── chatgpt_site/           # Django project settings
│   ├── __init__.py
│   ├── settings.py         # Django configuration
│   ├── urls.py            # URL routing
│   ├── wsgi.py
│   └── asgi.py
└── README.md              # This file
```

## 🎯 Usage

### Basic Chat
1. **Open the website** in your browser
2. **Type your message** in the input field
3. **Press Enter** or click "Send"
4. **Wait for AI response** - Watch the typing indicator
5. **Continue the conversation** - Chat naturally with the AI

### Features Overview
- **Real-time Messaging** - Instant responses from OpenAI
- **Message History** - See your conversation in the chat
- **Typing Indicators** - Visual feedback when AI is thinking
- **Error Handling** - Clear error messages if something goes wrong
- **Mobile Friendly** - Perfect experience on phones and tablets

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root with:
```env
OPENAI_API_KEY=sk-your-actual-api-key-here
```

### Django Settings
The project uses default Django settings with:
- **Debug Mode**: Enabled for development
- **Database**: SQLite (default)
- **Static Files**: Configured for production
- **CSRF Protection**: Enabled for security

## 🚀 Deployment

### Local Development
```bash
python manage.py runserver
```

### Production Deployment
1. **Set DEBUG = False** in settings.py
2. **Configure ALLOWED_HOSTS** for your domain
3. **Set up a production database** (PostgreSQL recommended)
4. **Configure static files** for your web server
5. **Set up environment variables** on your hosting platform

### Recommended Hosting Platforms
- **Heroku** - Easy Django deployment
- **Railway** - Modern cloud platform
- **DigitalOcean** - VPS hosting
- **AWS** - Enterprise-grade hosting

## 🎨 Customization

### Changing Colors
Edit the CSS in `chat.html`:
```css
/* Change gradient colors */
background: linear-gradient(135deg, #your-color-1 0%, #your-color-2 100%);
```

### Adding Features
- **User Authentication** - Add Django's built-in auth system
- **Message History** - Store conversations in database
- **Multiple Models** - Support different AI models
- **File Uploads** - Add image/document sharing
- **Voice Messages** - Integrate speech-to-text

## 🐛 Troubleshooting

### Common Issues

#### "API key not configured" Error
- **Solution**: Make sure your `.env` file is in the project root
- **Check**: Verify the API key format (no spaces around `=`)
- **Restart**: Restart the Django server after adding the key

#### "Network error" Messages
- **Check**: Internet connection
- **Verify**: OpenAI API key is valid and has credits
- **Debug**: Check browser console for specific errors

#### Mobile Display Issues
- **Test**: Use browser dev tools to simulate mobile
- **Check**: Viewport meta tag is present
- **Verify**: CSS media queries are working

### Debug Mode
Enable Django debug mode to see detailed error messages:
```python
# In settings.py
DEBUG = True
```

## 📱 Browser Support

- ✅ **Chrome** 90+
- ✅ **Firefox** 88+
- ✅ **Safari** 14+
- ✅ **Edge** 90+
- ✅ **Mobile Safari** (iOS)
- ✅ **Chrome Mobile** (Android)

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **OpenAI** - For the amazing GPT models
- **Django** - For the robust web framework
- **Contributors** - Thanks to all who help improve this project

## 📞 Support

If you encounter any issues or have questions:

1. **Check the troubleshooting section** above
2. **Search existing issues** in the repository
3. **Create a new issue** with detailed information
4. **Contact the maintainers** for urgent issues

---

**Made with ❤️ using Django and OpenAI**

*Happy Chatting! 🚀*
