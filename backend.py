users_db = {}
from flask import Flask, render_template, request, session, redirect, url_for
import random
from datetime import datetime
import time  
app = Flask(__name__)
app.secret_key = 'hamrosewa_secret_key'

LANG = {
    'en': {
        'home': 'Home',
        'contacts': 'Contacts',
        'team': 'Meet Our Team',
        'login': 'Login',
        'register': 'Register',
        'welcome': 'Welcome to',
        'enter_website': 'Enter Website',
        'customer_dashboard': 'Customer Dashboard',
        'professional_dashboard': 'Professional Dashboard',
        'book_now': 'Book Now',
        'send': 'Send',
        'confirm_booking': 'Confirm Booking',
        'quality_home_services': 'Quality home services, on demand',
        'service_available_in': 'Service available in:',
        'about': 'About Hamro Sewa',
        'how_it_works': 'How It Works',
        'featured_professionals': 'Featured Professionals',
        'why_hamro_sewa': 'Why Hamro Sewa?',
        'experts_only': 'Experts Only',
        'transparent_pricing': 'Transparent Pricing',
        'fully_equipped': 'Fully Equipped',
        'quality_assured': 'Quality Assured',
        'what_customers_say': 'What Our Customers Say',
        'register_title': 'Register',
        'login_title': 'Login',
        'contacts_title': 'Contact Us',
        'english': 'English'
    }
}

professionals = {
    'electrician': [
        {'name': 'Ram Shrestha', 'contact': '9800000001', 'rating': 4.5, 'experience': '5 years', 'image': 'https://randomuser.me/api/portraits/men/32.jpg'},
        {'name': 'Sita Gurung', 'contact': '9800000002', 'rating': 4.2, 'experience': '3 years', 'image': 'https://randomuser.me/api/portraits/women/44.jpg'},
        {'name': 'Hari Thapa', 'contact': '9800000003', 'rating': 4.8, 'experience': '7 years', 'image': 'https://randomuser.me/api/portraits/men/65.jpg'}
    ],
    'plumber': [
        {'name': 'Gopal Lama', 'contact': '9800000011', 'rating': 4.1, 'experience': '2 years', 'image': 'https://randomuser.me/api/portraits/men/12.jpg'},
        {'name': 'Manju Karki', 'contact': '9800000012', 'rating': 4.6, 'experience': '6 years', 'image': 'https://randomuser.me/api/portraits/women/36.jpg'},
        {'name': 'Bikash Rai', 'contact': '9800000013', 'rating': 4.3, 'experience': '4 years', 'image': 'https://randomuser.me/api/portraits/men/23.jpg'}
    ],
    'carpenter': [
        {'name': 'Krishna Tamang', 'contact': '9800000021', 'rating': 4.7, 'experience': '8 years', 'image': 'https://randomuser.me/api/portraits/men/41.jpg'},
        {'name': 'Puja Magar', 'contact': '9800000022', 'rating': 4.4, 'experience': '5 years', 'image': 'https://randomuser.me/api/portraits/women/22.jpg'},
        {'name': 'Ramesh KC', 'contact': '9800000023', 'rating': 4.0, 'experience': '3 years', 'image': 'https://randomuser.me/api/portraits/men/77.jpg'}
    ]
}


buys_slots_db = {}
chat_history_db = {}

subscriptions = {}


@app.route('/')
def index():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    print(f"[DEBUG] Rendering index page with language: {lang_code}")
    return render_template('index.html', lang=lang)

@app.route('/home')
def home():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    print(f"[DEBUG] Rendering home page with language: {lang_code}")
    return render_template('index.html', lang=lang)

@app.route('/team')
def team():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    print(f"[DEBUG] Rendering team page with language: {lang_code}")
    return render_template('team.html', lang=lang)

@app.route('/service/<job>')
def service(job):
    job_professionals = professionals.get(job.lower(), [])
    random.shuffle(job_professionals)
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    print(f"[DEBUG] Showing service page for job: {job} with {len(job_professionals)} professionals")
    return render_template('service.html', job=job, job_list=job_professionals, lang=lang)

@app.route('/book/<job>/<name>', methods=['GET', 'POST'])
def book(job, name):
    prof = next((p for p in professionals.get(job.lower(), []) if p['name'] == name), None)
    if not prof:
        print(f"[ERROR] Professional {name} not found for job {job}")
        return "Professional not found", 404

    available_slots = [f"{h}:00" for h in range(9, 18)]
    date = request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
    buys_slots = buys_slots_db.get((name, date), [])

    message = ''
    if request.method == 'POST' and 'time' in request.form:
        time_slot = request.form['time']
        print(f"[DEBUG] Booking attempt for {name} at {time_slot} on {date}")
        if time_slot in buys_slots:
            message = f'{prof["name"]} is busy at {time_slot}. Please choose another time.'
            print(f"[WARN] Time slot {time_slot} already booked for {name} on {date}")
        else:
            buys_slots.append(time_slot)
            buys_slots_db[(name, date)] = buys_slots
            message = f'Booking confirmed with {prof["name"]} at {time_slot} on {date}.'
            print(f"[INFO] Booking confirmed for {name} at {time_slot} on {date}")

    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    return render_template('book.html', prof=prof, available_slots=available_slots, date=date, busy_slots=buys_slots, message=message, lang=lang)

@app.route('/chat/<job>/<name>', methods=['GET', 'POST'])
def chat(job, name):
    prof = next((p for p in professionals.get(job.lower(), []) if p['name'] == name), None)
    if not prof:
        print(f"[ERROR] Professional {name} not found for chat")
        return "Professional not found", 404

    chat_history = chat_history_db.get((name, job), [])

@app.route('/profile/<job>/<name>')
def profile(job, name):
    prof = next((p for p in professionals.get(job.lower(), []) if p['name'] == name), None)
    if not prof:
        return "Professional not found", 404
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    return render_template('profile.html', prof=prof, job=job, lang=lang)
    if request.method == 'POST':
        msg_text = request.form.get('message')
        if msg_text:
            print(f"[DEBUG] New chat message from user to {name}: {msg_text}")
            chat_history.append({'sender': 'user', 'text': msg_text})
            chat_history.append({'sender': prof['name'], 'text': "Thank you for your message. I will get back to you shortly."})
            chat_history_db[(name, job)] = chat_history

    available_slots = [f"{h}:00" for h in range(9, 18)]
    date = datetime.now().strftime('%Y-%m-%d')
    busy_slots = buys_slots_db.get((name, date), [])

    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    return render_template('chat.html', prof=prof, available_slots=available_slots, date=date, busy_slots=busy_slots, chat_history=chat_history, lang=lang)

@app.route('/login', methods=['GET', 'POST'])
def login():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    message = ''
    if request.method == 'POST':
        role = request.form.get('role')
        phone = request.form.get('phone')
        password = request.form.get('password')
        job = request.form.get('job') if role == 'professional' else None

        print(f"[DEBUG] Login attempt: role={role}, phone={phone}, job={job}")

        if not phone or not password:
            message = 'Phone and password required!'
            print("[WARN] Missing phone or password")
        else:
        
            session['role'] = role
            session['phone'] = phone
            session['job'] = job

       
            if role == 'professional':
                sub = subscriptions.get(phone, {'active': False, 'expires': None})
                session['subscription'] = sub
                print(f"[INFO] Professional logged in: {phone}, subscription: {sub}")
                return redirect(url_for('professional_dashboard', job=job))
            else:
                print(f"[INFO] Customer logged in: {phone}")
                return redirect(url_for('customer_dashboard'))

    return render_template('login.html', message=message, lang=lang)

@app.route('/customer_dashboard')
def customer_dashboard():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    print(f"[DEBUG] Rendering customer dashboard for user: {session.get('phone')}")
    return render_template('customer_dashboard.html', lang=lang)

@app.route('/professional_dashboard/<job>', methods=['GET', 'POST'])
def professional_dashboard(job):
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    sub = session.get('subscription', {'active': False, 'expires': None})
    message = ''


    all_requests = [
        {'customer': 'Suman P.', 'service': 'Electrician', 'date': '2025-09-05', 'time': '10:00', 'message': 'Need urgent help with wiring!'},
        {'customer': 'Rina K.', 'service': 'Plumber', 'date': '2025-09-06', 'time': '14:00', 'message': 'Can you fix my kitchen tap?'},
        {'customer': 'Prakash T.', 'service': 'Electrician', 'date': '2025-09-07', 'time': '11:00', 'message': 'My lights are flickering.'}
    ]
    all_messages = [
        {'customer': 'Suman P.', 'service': 'Electrician', 'text': 'Thank you for your quick response!'},
        {'customer': 'Rina K.', 'service': 'Plumber', 'text': 'Looking forward to your visit.'},
        {'customer': 'Prakash T.', 'service': 'Electrician', 'text': 'Can you come today for the lights?'}
    ]


    requests = [r for r in all_requests if r['service'].lower() == job.lower()]
    messages = [m for m in all_messages if m['service'].lower() == job.lower()]

    if request.method == 'POST':
        plan = request.form.get('plan')
        code = request.form.get('code')
        phone = session.get('phone')
        now = int(time.time())

        print(f"[DEBUG] Subscription form submitted: plan={plan}, code={code}")

        if code == '990099':
            sub = {'active': True, 'expires': now + 30*24*3600}
            subscriptions[phone] = sub
            session['subscription'] = sub
            message = 'Redeem code applied! Subscription active for 1 month.'
            print(f"[INFO] Redeem code applied for {phone}")
        elif plan == 'week':
            sub = {'active': True, 'expires': now + 7*24*3600}
            subscriptions[phone] = sub
            session['subscription'] = sub
            message = 'Subscribed for 1 week (Rs 50).'
            print(f"[INFO] Weekly subscription activated for {phone}")
        elif plan == 'month':
            sub = {'active': True, 'expires': now + 30*24*3600}
            subscriptions[phone] = sub
            session['subscription'] = sub
            message = 'Subscribed for 1 month (Rs 300).'
            print(f"[INFO] Monthly subscription activated for {phone}")
        else:
            message = 'Invalid selection.'
            print("[WARN] Invalid subscription selection")

    if sub['active'] and sub['expires']:
        if sub['expires'] < int(time.time()):
            sub = {'active': False, 'expires': None}
            phone = session.get('phone')
            subscriptions[phone] = sub
            session['subscription'] = sub
            message = 'Subscription expired.' 
            print(f"[INFO] Subscription expired for {phone}")

    return render_template('subscription.html', lang=lang, subscription=sub, message=message, requests=requests, messages=messages)

@app.route('/register', methods=['GET', 'POST'])
def register():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    message = ''
    if request.method == 'POST':
        role = request.form.get('role')
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        job = request.form.get('job') if role == 'professional' else None
        cert_file = request.files.get('certificate') if role == 'professional' else None

        print(f"[DEBUG] Registration attempt: role={role}, name={name}, phone={phone}, job={job}")

       
        phone_verified = phone and phone.startswith('98') and len(phone) == 10

        cert_filename = None
        if cert_file and cert_file.filename:
            cert_filename = f"certs/{name}_{cert_file.filename}"
            cert_file.save(cert_filename)
            print(f"[INFO] Certificate uploaded: {cert_filename}")

    
        message = f"Registered as {role}. "
        if role == 'professional':
            message += f"Job: {job}. Certificate: {'Uploaded' if cert_filename else 'Not uploaded'}. "
        message += f"Phone Verified: {'Yes' if phone_verified else 'No'}"
        print(f"[INFO] Registration completed for {name}")

        return render_template('register.html', message=message, lang=lang)

    return render_template('register.html', lang=lang)

@app.route('/contacts', methods=['GET', 'POST'])
def contacts():
    lang_code = session.get('lang', 'en')
    lang = LANG.get(lang_code, LANG['en'])
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        print(f"[DEBUG] Contact form submitted by {name} with subject '{subject}'")
      
        return render_template('contacts.html', message="Thank you for contacting us! We'll get back to you soon.", lang=lang)
    return render_template('contacts.html', lang=lang)





if __name__ == '__main__':
    print("[INFO] Starting Flask app in debug mode")
    app.run(debug=True)
