# 🎉 Birthday Email Sender

An elegant Python application that sends personalized, beautifully formatted HTML birthday emails via Gmail SMTP. Perfect for automating birthday wishes with a personal touch!

## ✨ Features

- **Personalized Birthday Messages**: Automatically fills recipient names and sender information
- **Beautiful HTML Emails**: Professionally styled HTML emails with gradient headers, emojis, and responsive design
- **Easy Template System**: Simple text template with placeholder support (`{name}` and `[Your Name]`)
- **Gmail SMTP Integration**: Secure email sending via Gmail's SMTP server
- **Environment-based Credentials**: Uses `.env` file for secure credential management
- **Fallback Plain Text**: Includes plain-text version for email clients that don't support HTML

## 📸 Output Example

Here's what the birthday email looks like when received:

![Birthday Email Screenshot](https://raw.githubusercontent.com/Dev-ini11/send_mail_template/main/image.png)

## 🏗️ Project Structure

```
Send_Mail/
├── app.py                           # Main entry point - orchestrates the email sending
├── build_html.py                    # Converts plain text to styled HTML emails
├── send.py                          # Handles SMTP connection and email delivery
├── utility.py                       # Helper functions: file reading, text substitution, credentials
├── main.ipynb                       # Jupyter notebook for development/testing
├── data/
│   ├── Birthday_Wish_Template.txt   # Email template with placeholders
│   └── products.csv                 # Additional data (for future extensions)
├── .env                             # Environment variables (credentials) - not in repo
└── README.md                        # This file
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7+
- Gmail account with [App Password](https://support.google.com/accounts/answer/185833) enabled (2FA required)

### Installation

1. **Clone or download this repository**
   ```bash
   cd /path/to/Send_Mail
   ```

2. **Install dependencies**
   ```bash
   pip install python-dotenv
   ```

3. **Create a `.env` file** in the project root:
   ```env
   my_email=your-email@gmail.com
   my_password=your-app-password
   ```
   > ⚠️ **Security Note**: Never commit `.env` to version control. Use `git ignore` to exclude it.

4. **Update the birthday template** (optional)
   
   Edit `data/Birthday_Wish_Template.txt` to customize the message. Use placeholders:
   - `{name}` - Recipient's name
   - `[Your Name]` - Your name

## 🚀 Usage

### Basic Usage

1. **Open `app.py`** and configure:
   ```python
   # Set the recipient details
   content = modify(
       read_file("data/Birthday_Wish_Template.txt"), 
       name="Ini",              # Recipient's name
       your_name="Prince"       # Your name
   )
   
   # Build the HTML email
   html = build_birthday_email(
       name="Ini", 
       body_text=content, 
       sender_name="Prince"
   )
   
   # Send the email
   send_birthday_email(
       to_email="inioluwaayetoro@gmail.com",
       subject="Happy Birthday, Ini! 🎉",
       html_content=html,
       smtp_user=email,
       smtp_password=my_password
   )
   ```

2. **Run the script**:
   ```bash
   python app.py
   ```

3. **Check the recipient's inbox** for the birthday email!

### Jupyter Notebook

For interactive development and testing, use `main.ipynb`:
```bash
jupyter notebook main.ipynb
```

## 📝 API Reference

### `build_html.py`
**`build_birthday_email(name, body_text, sender_name="")`**
- Converts plain text to styled HTML email
- Returns: HTML document string ready for email body

### `send.py`
**`send_birthday_email(to_email, subject, html_content, smtp_user, smtp_password, ...)`**
- Sends HTML email via SMTP
- Supports plain-text fallback for compatibility
- Default SMTP: Gmail (smtp.gmail.com:587)

### `utility.py`
- **`read_file(file_path)`** - Reads file with UTF-8 encoding
- **`modify(text, name, your_name)`** - Replaces placeholders in text
- **`email`** - Loaded from environment variable `my_email`
- **`my_password`** - Loaded from environment variable `my_password`

## 🎨 Email Styling

The generated HTML includes:
- 📊 **Responsive Design**: Works on mobile and desktop
- 🌈 **Gradient Header**: Eye-catching birthday banner with emojis
- 💬 **Formatted Paragraphs**: Proper spacing and typography
- 📍 **Decorative Elements**: Dividers and footer with celebration emojis
- 🎨 **Professional Color Scheme**: Warm, inviting pastels

## 🔧 Customization

### Change Email Subject
Edit the subject line in `app.py`:
```python
send_birthday_email("recipient@email.com", "Your Custom Subject 🎂", html, email, my_password)
```

### Modify Email Template
Edit `data/Birthday_Wish_Template.txt` with your custom message while keeping `{name}` and `[Your Name]` placeholders.

### Customize HTML Styling
Edit the CSS in `build_html.py`'s `build_birthday_email()` function to change colors, fonts, or layout.

## 🔒 Security Best Practices

1. **Use Gmail App Passwords** - Never use your main Gmail password
2. **Keep `.env` secret** - Add to `.gitignore` (already done)
3. **Use environment variables** - Don't hardcode credentials in source files
4. **Enable 2FA** - Required for App Password generation

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Login credentials invalid" | Verify App Password is correct; not your Gmail password |
| "SMTPAuthenticationError" | Enable 2FA on Gmail and generate an [App Password](https://support.google.com/accounts/answer/185833) |
| "Email not received" | Check spam folder; verify recipient email is correct |
| "ModuleNotFoundError: dotenv" | Run `pip install python-dotenv` |

## 📚 Future Enhancements

- [ ] Batch send birthday emails to multiple recipients from CSV
- [ ] Schedule automated birthday reminders
- [ ] Add email templates for other occasions (anniversaries, holidays)
- [ ] Web UI for easy configuration
- [ ] Support for multiple email providers

## 📄 License

This project is open source and available for personal use.

## 👨‍💻 Author

Created with ❤️ for celebrating special moments!

---

**Happy Birthday! 🎉🎂🎈**
