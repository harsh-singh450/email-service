# Email Sending Service

## 1. Install the required dependencies

```bash
pip install -r requirements.txt
```

## 2. Configure your environment

## Step 1: Get Your SMTP Settings

Check with your IT/admin or hosting provider. Common setups:

### Google Workspace (Gmail business)
```ini
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
MAIL_USERNAME=contact@intelation.com
MAIL_PASSWORD=AppPasswordOrAccountPassword
```

### Microsoft 365 / Outlook Business
```ini
MAIL_SERVER=smtp.office365.com
MAIL_PORT=587
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
MAIL_USERNAME=contact@intelation.com
MAIL_PASSWORD=YourPasswordOrAppPassword
```

### cPanel / Custom Hosting (GoDaddy, Hostinger, etc.)
Usually:
```ini
MAIL_SERVER=mail.intelation.com
MAIL_PORT=465   # (SSL) or 587 (TLS)
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
MAIL_USERNAME=contact@intelation.com
MAIL_PASSWORD=YourMailboxPassword
```


Create a file named **.env** in the root directory and populate it with your SMTP server credentials.  
You can copy the structure below.

**.env file:**

```ini
MAIL_USERNAME=your_smtp_username
MAIL_PASSWORD=your_smtp_password
MAIL_FROM=yourcompany@example.com
MAIL_PORT=587
MAIL_SERVER=smtp.mailtrap.io
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
```

## 3. Running the Application

Start the development server using **Uvicorn**:

```bash
uvicorn main:app --reload
```

The application will be running at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 📚 API Usage & Endpoints

Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the interactive Swagger UI and test the endpoints directly from your browser.

### Transactional Emails

#### **POST** `/transactional/send/password-reset`
Sends a templated HTML email for password resets.

**Request Body:**

```json
{
  "recipients": ["user@example.com"],
  "subject": "Your Password Reset Link",
  "body": {
    "name": "Jane Doe",
    "reset_link": "https://yourapp.com/reset/some-unique-token"
  }
}
```

#### **POST** `/transactional/send/simple`
Sends a simple, non-templated plain text email.

**Request Body:**

```json
{
  "recipients": ["user@example.com"],
  "subject": "An Important Update",
  "body": "Hello, this is a plain text message regarding your account."
}
```

---

### Newsletters

#### **POST** `/newsletters/send`
Sends a templated HTML newsletter to a list of subscribers.

**Request Body:**

```json
{
  "recipients": ["subscriber1@example.com", "subscriber2@example.com"],
  "subject": "This Week's Newsletter",
  "body": {
    "name": "Valued Reader",
    "title": "Our Top Stories This Week",
    "content": "<h1>Headline 1</h1><p>Content for the first story...</p>"
  }
}
```

---

### Marketing & Product Updates

#### **POST** `/marketing/send/campaign`
Sends a templated HTML email for a marketing campaign or product update.

**Request Body:**

```json
{
  "recipients": ["customer@example.com"],
  "subject": "Our Summer Sale is Here!",
  "body": {
    "name": "Alex",
    "headline": "Don't Miss Out on 50% Off!",
    "promo_text": "Everything in our store is on sale for a limited time.",
    "cta_link": "https://yourstore.com/sale"
  }
}
```

---

### System Notifications

#### **POST** `/system/send/alert`
Sends a templated HTML alert to administrators or users about a system event.

**Request Body:**

```json
{
  "recipients": ["admin@yourcompany.com"],
  "subject": "High CPU Usage Detected",
  "body": {
    "severity": "critical",
    "severity_color": "red",
    "message": "Server 'prod-db-1' has exceeded 95% CPU utilization.",
    "timestamp": "2025-09-18 16:30:00 UTC"
  }
}
```

---